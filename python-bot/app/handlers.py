import json
from os import path, makedirs

basepath = path.dirname(__file__)
filename = 'questions.json'
filepath = path.abspath(path.join(basepath, '..', '..', filename))

with open(filepath, 'r') as file:
  questions = json.load(file)

def user_message_handler(user_id, text):
    keyboard_type = 'answers'
    reply = ''
    
    base = path.dirname(__file__)
    user_answer_name = str(user_id) + '.json'
    user_answer_path = path.abspath(path.join(base, '..', 'answers', user_answer_name))
    
    user_answer = []

    if text == 'Начать тест':
        makedirs(path.dirname(user_answer_path), exist_ok=True)

        with open(user_answer_path, 'w') as file:
            json.dump(user_answer, file, indent=4)
        
        question_number = questions[0]['question_number']
        question = questions[0]['question']
        answers = questions[0]['answers']
        reply = f'Вопрос №{question_number}\n\n{question}\n\n{answers['1']}\n{answers['2']}\n{answers['3']}'
        keyboard_type = 'answers'
    elif text == '1' or text == '2' or text == '3':
        pass
    else:
        reply = 'Прости, я тебя не понял :(\nПожалуйста, нажимай на кнопочки'
        
    return reply, keyboard_type
    
    
    

    
        
