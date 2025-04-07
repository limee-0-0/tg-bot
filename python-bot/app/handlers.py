import json
from os import path, makedirs

basepath = path.dirname(__file__)
filename = 'questions.json'
filepath = path.abspath(path.join(basepath, '..', '..', filename))

with open(filepath, 'r', encoding='utf-8') as file:
  questions = json.load(file)

def user_message_handler(user_id, text):
    keyboard_type = 'answers'
    reply = ''
    
    user_answer_name = str(user_id) + '.json'
    user_answer_path = path.abspath(path.join(basepath, '..', 'answers', user_answer_name))

    if text == 'Начать тест' or text == 'Начать заново':
        makedirs(path.dirname(user_answer_path), exist_ok=True)

        with open(user_answer_path, 'w', encoding='utf-8') as file:
            json.dump([], file, indent=4)

        question_number = questions[0]['question_number']
        question = questions[0]['question']
        answers = questions[0]['answers']
        reply = f"Вопрос №{question_number}\n\n{question}\n\n{answers['1']}\n{answers['2']}\n{answers['3']}"
    elif text == '1' or text == '2' or text == '3':
        with open(user_answer_path, 'r', encoding='utf-8') as file:
            current_user_answers = json.load(file)

        current_question_index = len(current_user_answers)
        current_question = questions[current_question_index]

        user_answer = {
            'question_number': current_question['question_number'],
            'question': current_question['question'],
            'answer': current_question['answers'][text],
            'points': int(text)
        }

        current_user_answers.append(user_answer)

        with open(user_answer_path, 'w', encoding='utf-8') as file:
            json.dump(current_user_answers, file, indent=4, ensure_ascii=False)

        is_last_question_answered = len(questions) == len(current_user_answers)

        if is_last_question_answered:
            points_list = [item['points'] for item in current_user_answers]
            result = sum(points_list)

            programming_language = ''
            language_description = ''

            if result < 14:
                programming_language = 'Python'
                language_description = 'Вы обладаете легкостью, простотой и невероятной продуктивностью. Вы быстро находите решения для любых проблем, используя минимальные ресурсы и оставляя всё лишнее за бортом. Ваше мышление прямолинейное и эффективное, Вы видите суть вещей и сразу переходите к делу, не тратя время на излишние сложности.'
            elif result < 20:
                programming_language = 'C++'
                language_description = 'Вы мощный, многогранный и невероятно эффективный человек. Вы обладаете высокой производительностью и способностью глубоко погружаться в детали любой задачи, разбирая её до мельчайших компонентов. Вы мастер в управлении ресурсами, будь то время, энергия или внимание, что позволяет Вам добиваться выдающихся результатов в кратчайшие сроки.'
            else:
                programming_language = 'Java'
                language_description = 'Вы надежны, стабильны и высокоорганизованны. Ваше мышление структурированно и последовательно. Вы предпочитаете ясность и предсказуемость во всех аспектах жизни, избегая неожиданностей и ошибок. Также Вы обладаете широким кругозором и глубокими знаниями в различных областях, что позволяет Вам легко адаптироваться к новым ситуациям и решать самые разные задачи.'

            reply = f'Поздравляю! Вы {programming_language}!\n{language_description}'
            keyboard_type = 'reset_test'
        else:
            question_number = questions[current_question_index + 1]['question_number']
            question = questions[current_question_index + 1]['question']
            answers = questions[current_question_index + 1]['answers']

            reply = f"Вопрос №{question_number}\n\n{question}\n\n{answers['1']}\n{answers['2']}\n{answers['3']}"
    else:
        reply = 'Прости, я тебя не понял :(\nПожалуйста, нажимай на кнопочки'

    return reply, keyboard_type
