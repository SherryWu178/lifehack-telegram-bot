# import logging
# import telegram
# from typing import Tuple, Optional

# from telegram import Update, Chat, ChatMember, ChatMemberUpdated

# from telegram.ext import (
#         Updater,
#         CommandHnadler,
#         CallbackContext,
#         ChateMemberHandler,
#         )
# bot = telegram.Bot(token='1892557011:AAFd_H0RKCLvZdIc9SHknIGH_ofi0q3W3Xc')
# # Enable logging
# logging.basicConfig(
#         format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
#         )

# logger = logging.getLogger(__name__)

# Set your bot_token here
# (the same one as you've created and used just now!)
import logging
import requests

from telegram.ext import MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram.ext import Updater
bot_token = "1892557011:AAFd_H0RKCLvZdIc9SHknIGH_ofi0q3W3Xc"

# Importing python-telegram-bot's library functions

# Setting up our logger
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def get_cat_fact():
    endpoint = "https://catfact.ninja/fact"
    response = requests.get(endpoint)
    fact = response.json()["fact"]
    return fact


def get_dog_fact():
    endpoint = "http://dog-api.kinduff.com/api/facts"
    response = requests.get(endpoint)
    fact = response.json()["facts"][0]
    return fact


# Setting up their polling stuff
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

# Functions to handle each command


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hi! To start a jio, type '/start_jio'")

def 


def cat_asdf(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=get_cat_fact())


def dog(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=get_dog_fact())


def carpark(update, context):
    carpark_code = context.args[0].upper()
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=get_carpark_availability(carpark_code))


def echo(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=update.message.text)


def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


# Create and add command handlers
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

cat_handler = CommandHandler('cat', cat_asdf)
dispatcher.add_handler(cat_handler)

dog_handler = CommandHandler('dog', dog)
dispatcher.add_handler(dog_handler)

carpark_handler = CommandHandler('carpark', carpark)
dispatcher.add_handler(carpark_handler)

echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

updater.start_polling()

# Start the Bot
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN)
updater.bot.setWebhook('https://floating-waters-24425.herokuapp.com/' + bot_token)

updater.idle()
