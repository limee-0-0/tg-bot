
import os
from dotenv import load_dotenv

from telebot import TeleBot, types
import app.keyboards as kb

load_dotenv()

API_TOKEN = os.getenv('API_TOKEN')

bot = TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text='Привет! Давай узнаем, какой ты язык программирования')
    bot.send_message(message.chat.id, text='Ответь мне на несколько вопросов', reply_markup=kb.strt_test)

@bot.message_handler(commands=['help'])
def helpme(message):
    bot.reply_to(message, 'Это команда /help')


@bot.callback_query_handler(func=lambda call: call.data == "gotest")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №1\n\nКогда вы просыпаетесь?\n\n1. Зависит от того, во сколько лёг\n2. Ближе к обеду, чтобы хоть как-то выспаться\n3. Утром, чем раньше, тем лучше",
                     reply_markup=kb.question_1)


@bot.callback_query_handler(func=lambda call: call.data == "button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №2\n\nУ вас есть список задач на день?\n\n1. Да, само собой, как же без него\n2. Мне он не нужен, прекрасно справляюсь без него\n3. Если день сложный - пишу, если нет, то и без списка хорошо",
                     reply_markup=kb.question_2)
    

@bot.callback_query_handler(func=lambda call: call.data == "2button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №3\n\nМожете ли вы делать несколько дел одновременно?\n\n1. Не люблю работать в таком режиме, но если приходится, то вообще без проблем\n2. Да, в наше время без этого никак\n3. Нет, я занимаюсь задачами поочереди",
                     reply_markup=kb.question_3)
    

@bot.callback_query_handler(func=lambda call: call.data == "3button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №4\n\nКак вы проводите свободное время?\n\n1. В смысле - свободное время? Вы про что?\n2. Если нужно сделать что-то на работе - доделываю, а если нет - отдыхаю\n3. Отдыхаю и ничего не делаю. Кайф!",
                     reply_markup=kb.question_4)


@bot.callback_query_handler(func=lambda call: call.data == "4button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №5\n\nНа рабочем столе у вас хаос или порядок?\n\n1. Хаос\n2. Порядок\n3. По настроению",
                     reply_markup=kb.question_5)


@bot.callback_query_handler(func=lambda call: call.data == "5button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №6\n\nЕсли к вам внезапно нагрянут друзья, что вы сделаете?\n\n1. Скажу, что сейчас занят, и договорюсь о новом визите. А потом закрою дверь и пойду работать дальше\n2. Будет сложно, но я постараюсь что-нибудь придумать\n3. Приму в любое время - это же друзья!",
                     reply_markup=kb.question_6)


@bot.callback_query_handler(func=lambda call: call.data == "6button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №7\n\nВы легко делегируете задачи?\n\n1. Только в крайних случаях, когда без этого уже совсем никак\n2. Конечно, и чем больше, тем лучше\n3. Всё делаю сам, потому что кроме меня никто ничего нормального не сделает",
                     reply_markup=kb.question_7)
    

@bot.callback_query_handler(func=lambda call: call.data == "7button_1")
def start_test(call: types.CallbackQuery):
    bot.answer_callback_query(call.id, " ")
    bot.delete_message(call.message.chat.id, call.message.message_id)
    bot.send_message(chat_id=call.message.chat.id, text="Вопрос №8\n\nЧитаете ли вы инструкции от бытовой техники?\n\n1. От корки до корки, включая гарантийный талон и руководство по безопасному обращению\n2. Что читаю?\n3. К сложным приборам - да, а к обычному пылесосу зачем читать?",
                     reply_markup=kb.question_8)

# # обработка сообщений (эхо)
# @bot.message_handler(func=lambda message: True)
# def echo_message(message):
#     bot.reply_to(message, message.text)

bot.infinity_polling()