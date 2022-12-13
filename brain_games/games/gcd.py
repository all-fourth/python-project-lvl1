from math import gcd
from random import randint

RULES = 'Find the greatest common divisor of given numbers.'


def getting_result():

    int_one = randint(1, 100)
    int_two = randint(1, 100)
    right_answer = gcd(int_one, int_two)
    question = f'Question: {int_one} {int_two}'
    return question, str(right_answer)
