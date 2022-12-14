from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number: int):
    if number <= 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_game():
    random_num = randint(2, 100)

    if is_prime(random_num) <= 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'Question: {random_num}'
    return question, right_answer
