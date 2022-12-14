from random import randint

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even():
    random_num = randint(1, 100)
    even = random_num % 2 == 0
    return even, random_num


def get_game():
    even, random_num = is_even()
    if even:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'Question: {random_num}'
    return question, right_answer
