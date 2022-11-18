from random import randint

import prompt

RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def question_and_answer():

    random_int = randint(1, 100)
    answer = prompt.string(f'Question: {random_int}\nYour answer: ')
    if random_int % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return answer, right_answer
