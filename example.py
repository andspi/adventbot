import keys

telegram_api_key = keys.telegram_api_key
giphy_api_key = keys.giphy_api_key   

# print(telegram_api_key)
# print(giphy_api_key)

from telegram.ext import Updater
updater = Updater(token=telegram_api_key, use_context=True)

dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please take my gifts!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start',start)
dispatcher.add_handler(start_handler)

updater.start_polling()
