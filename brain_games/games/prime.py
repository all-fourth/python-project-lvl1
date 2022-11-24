from random import randint

import prompt

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def question_and_answer():

    random_int = randint(2, 100)
    answer = prompt.string(f'Question: {random_int}\nYour answer: ')
    counter = 0
    for is_prime in range(2, random_int // 2 + 1):
        if (random_int % is_prime == 0):
            counter += 1
    if (counter <= 0):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return answer, right_answer
