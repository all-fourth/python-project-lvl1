from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(random_num):
    return random_num % 2 == 0


def get_game():
    random_num = randint(1, 100)

    if is_even(random_num):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'Question: {random_num}'
    return question, right_answer
