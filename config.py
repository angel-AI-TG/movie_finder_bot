'''Token of bot, TMDB API key'''

import os

# Token of Telegram bot
TOKEN = os.environ.get("BOT_TOKEN","123456:abcdefghijklmnop")

# API key of TMDB (v3 auth)
API_KEY= os.environ.get("API_KEY","Read The Readme.md")
