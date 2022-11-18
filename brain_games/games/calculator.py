import operator
import random

import prompt

RULES = 'What is the result of the expression?'


def question_and_answer():

    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    int_one = random.randint(1, 100)
    int_two = random.randint(1, 100)
    rand_operator = random.choice(list(operators.keys()))
    right_answer = str(operators.get(rand_operator)(int_one, int_two))
    answer = prompt.string(f'Question: {int_one}{rand_operator}{int_two}\nYour answer: ')

    return answer, right_answer
