import telebot
import app_api

token = ""

bot = telebot.TeleBot(token)

user_search_query = {}

@bot.message_handler(commands=["start"])
def welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(row_width=1)

    btn_1 = telebot.types.ReplyKeyboardButton(text="Search")
    btn_2 = telebot.types.ReplyKeyboardButton(text="Random")
    btn_3 = telebot.types.ReplyKeyboardButton(text="Help")

    markup.add(btn_1, btn_2, btn_3)

    bot.send_message(message.chat.id, text="Welcome! Please choose an option.", reply_markup=markup)

@bot.message_handler(func=lambda message:True)
def handle_all_messages_1(message):
    if message.text == "Search":
        msg = bot.send_message(message.chat.id, text=" Please enter the name you want to search.")
        bot.register_next_step_handler(msg, get_info)
    elif message.text == "Random":
        r_location_result = app_api.get_random_location()
        r_quote_result = app_api.random_quote()
        r_movie_result = app_api.get_movie_info_by_random_id()
        bot.send_message(message.chat.id, text=f"Latitude, Longitude : {r_location_result}\nMovie: {r_movie_result}\n{r_quote_result}")
    elif message.text == "Help":
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text="select search and enter a keyword, such as a city name, movie title, or quote topic to get results", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="Sorry, I can't undrestand what you say. Please use the buttons.")

def get_info(message):
    user_search_query[message.chat.id] = message.text
    markup = telebot.types.InlineKeyboardMarkup(row_width=1)
    btn_1 = telebot.types.InlineKeyboardButton(text="location result", callback_data="location")
    btn_2 = telebot.types.InlineKeyboardButton(text="quote result", callback_data="quote")
    btn_3 = telebot.types.InlineKeyboardButton(text="movie result", callback_data="movie")
    markup.add(btn_1, btn_2, btn_3)
    bot.send_message(message.chat.id, text="Select one result", reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def show_info(call):
    query = user_search_query.get(call.message.chat.id)
    if not query:
        bot.answer_callback_query(call.id, "Error, Please try again.")
        return

    if call.data == "location":
        location_result = app_api.get_location_info_by_name(query)
        bot.send_message(call.message.chat.id, f"location: {location_result}")
    elif call.data == "quote":
        quote_result = app_api.quote_getter(query)
        bot.send_message(call.message.chat.id, f"quotes: {quote_result}")
    elif call.data == "movie":
        movie_result = app_api.get_movie_info_by_name(query)
        bot.send_message(call.message.chat.id, f"movie: {movie_result}")

    bot.answer_callback_query(call.id)

if __name__ == "__main__":
    bot.infinity_polling()
