'''Token of bot, TMDB API key'''

from moviebot import TOKEN, API_KEY
import os

TKN = str(TOKEN) if TOKEN else "129493984anhsbdvjsfabjs"
API = str(API_KEY) if API_KEY else ""

# Token of Telegram bot
TOKEN= TKN

# API key of TMDB (v3 auth)
API_KEY=os.environ.get(API)
