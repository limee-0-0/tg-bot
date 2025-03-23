import json

from dotenv import load_dotenv

import os


from telebot import TeleBot
import app.keyboards as kb
from app.handlers import user_message_handler

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = TeleBot(API_TOKEN)



# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text='Привет! Давай узнаем, какой ты язык программирования\nОтветь мне на несколько вопросов', 
                     reply_markup=kb.strt_test)

@bot.message_handler(commands=['help'])
def helpme(message):
    bot.reply_to(message, 'Это команда /help')

@bot.message_handler(content_types=['text'])
def message_handler(message):
    user_id = message.chat.id
    text = message.text

    reply = user_message_handler(user_id, text)
    keyboard_type = user_message_handler(user_id, text)
    bot.send_message(user_id, text=reply, reply_markup=keyboard_type)





bot.infinity_polling()