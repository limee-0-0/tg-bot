
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

start_test = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text="Начать тест")
start_test.add(button_1)

answers = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text="1")
button2 = KeyboardButton(text="2")
button3 = KeyboardButton(text="3")
answers.add(button1, button2, button3)

reset_test = ReplyKeyboardMarkup(resize_keyboard=True)
button_reset = KeyboardButton(text="Начать заново")
reset_test.add(button_reset)

keyboards = {
    'start_test': start_test,
    'answers': answers,
    'reset_test': reset_test
}
