# Telegram Discovery Bot

A Python-powered Telegram bot that combines city location lookup, movie discovery, and quote search in one interactive application.

Users can search for a keyword and choose whether to retrieve location coordinates, movie information, or related quotes. The bot also offers a Random feature for exploring random locations, movies, and quotes.

## Features

- **Location Search:** Find latitude and longitude coordinates for a city.
- **Movie Search:** Search for movie information by title.
- **Quote Search:** Find quotes related to a keyword or topic.
- **Random Discovery:** Get a random location, movie, and quote.
- **Interactive Menus:** Use Telegram reply keyboards and inline buttons.
- **Help Menu:** Display instructions for using the bot.

## Technologies

- Python
- pyTelegramBotAPI
- Requests
- OpenWeather Geocoding API
- Movies API
- Quotable API

## Project Structure

```text
telegram-discovery-bot/
├── src
    |├── bot.py
    |└── app_api.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/ph4848/telegram-discovery-bot.git
cd telegram-discovery-bot
```

### 2. Create a virtual environment

On Windows:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure API credentials

```text
TELEGRAM_BOT_TOKEN=your_telegram_bot_token
```

### 5. Run the bot

```bash
python bot.py
```

Open your bot in Telegram and send `/start`.

## Usage

1. Send `/start` to open the main menu.
2. Select **Search** and enter a city name, movie title, or quote topic.
3. Choose the type of result you want using the inline buttons.
4. Select **Random** to receive a random location, movie, and quote.
5. Select **Help** for usage instructions.

## APIs

- Movies API: https://moviesapi.ir/
- OpenWeather Geocoding API: https://openweathermap.org/api/geocoding-api
- Quotable: https://api.quotable.io/

External APIs may have availability, authentication, rate-limit, or response-format restrictions.
