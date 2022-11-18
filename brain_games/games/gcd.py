import math
import random

import prompt

RULES = 'Find the greatest common divisor of given numbers.'


def question_and_answer():

    int_one = random.randint(1, 100)
    int_two = random.randint(1, 100)
    right_answer = str(math.gcd(int_one, int_two))
    answer = prompt.string(f'Question: {int_one} {int_two}\nYour answer: ')

    return answer, right_answer
