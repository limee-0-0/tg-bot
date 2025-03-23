
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

strt_test = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text="Начать тест")
strt_test.add(button_1)

answers = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="1")
button2 = KeyboardButton(text="2")
button3 = KeyboardButton(text="3")
answers.add(button1, button2, button3)

reset_test = ReplyKeyboardMarkup(resize_keyboard=True)
