from math import gcd
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def getting_result():

    random_num1 = randint(1, 100)
    random_num2 = randint(1, 100)
    right_answer = gcd(random_num1, random_num2)
    question = f'Question: {random_num1} {random_num2}'
    return question, str(right_answer)
