
from telebot.util import quick_markup

strt_test = quick_markup({
    'Начать тест': {'callback_data': 'gotest'}
    })

question_1 = quick_markup({
    '1': {'callback_data': 'button_1'},
    '2': {'callback_data': 'button_2'},
    '3': {'callback_data': 'button_3'}
}, row_width=3)

question_2 = quick_markup({
    '1': {'callback_data': '2button_1'},
    '2': {'callback_data': '2button_2'},
    '3': {'callback_data': '2button_3'}
}, row_width=3)

question_3 = quick_markup({
    '1': {'callback_data': '3button_1'},
    '2': {'callback_data': '3button_2'},
    '3': {'callback_data': '3button_3'}
}, row_width=3)

question_4 = quick_markup({
    '1': {'callback_data': '4button_1'},
    '2': {'callback_data': '4button_2'},
    '3': {'callback_data': '4button_3'}
}, row_width=3)

question_5 = quick_markup({
    '1': {'callback_data': '5button_1'},
    '2': {'callback_data': '5button_2'},
    '3': {'callback_data': '5button_3'}
}, row_width=3)

question_6 = quick_markup({
    '1': {'callback_data': '6button_1'},
    '2': {'callback_data': '6button_2'},
    '3': {'callback_data': '6button_3'}
}, row_width=3)

question_7 = quick_markup({
    '1': {'callback_data': '7button_1'},
    '2': {'callback_data': '7button_2'},
    '3': {'callback_data': '7button_3'}
}, row_width=3)

question_8 = quick_markup({
    '1': {'callback_data': '8button_1'},
    '2': {'callback_data': '8button_2'},
    '3': {'callback_data': '8button_3'}
}, row_width=3)