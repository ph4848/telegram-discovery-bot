from random import randint, uniform
import requests

def get_movie_info_by_name(movie_name):
    url = f'https://moviesapi.ir/api/v1/movies'
    params_dict = {
        'q': movie_name
    }
    response = requests.get(url, params=params_dict)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        result = response['data'][0]
        title = result['title']
        year = result['year']
        country =  result['country']
        imdb_rate = result['imdb_rating']
        return (title, country , year, imdb_rate)

def get_movie_info_by_random_id():
    random_id = randint(1, 251)
    url = f'https://moviesapi.ir/api/v1/movies/{random_id}'
    response = requests.get(url)
    if response.status_code != 200:
        return 'ERROR'
    else:
        response = response.json()
        title = response['title']
        country = response['country']
        director = response['director']
        year = response['year']
        imdb_rate = response['imdb_rating']

        return (title, country , director, year, imdb_rate)

def get_location_info_by_name(city_name):
    weather_api_key = "23e4132af9af50a0bb57a6527c7d2894"
    geocoding_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={weather_api_key}"
    geo_response = requests.get(geocoding_url)
    if geo_response.status_code != 200:
        return 'ERROR'
    else:
        geo_response = geo_response.json()
        lat = geo_response[0]["lat"]
        lon = geo_response[0]["lon"]
        return(lat, lon)

def get_random_location():
    lat = round(uniform(-90, 90), 2)
    lon = round(uniform(-180, 180), 2)
    return (lat, lon)

def quote_getter(text):
    edited_text = ""
    for i in text:
        if ord(i) >= ord('0') and ord(i) <= ord('z'):
            edited_text += i
        else:
            edited_text += '+'
    quote_url = f"https://api.quotable.io/search/quotes?query={edited_text}&fields=content"
    q_response = requests.get(quote_url)
    if q_response.status_code != 200:
        return 'ERROR'
    else:
        q_response = q_response.json()
        results = q_response["__info__"]["results"]
        result_list = list()
        for quote in results:
            result_list.append(quote["content"])
        return result_list

def random_quote():
    quote_url = "https://api.quotable.io/quotes/random"
    q_response = requests.get(quote_url)
    if q_response.status_code != 200:
        return 'ERROR'
    else:
        q_response = q_response.json()
        random_quote = q_response[0]["content"]
        return random_quote


#Geocoding url = http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={API key}
#https://api.quotable.io/quotes/random
#https://api.quotable.io/search/quotes?query=every+good+technology+is+basically+magic&fields=content