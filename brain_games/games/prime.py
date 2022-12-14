from random import randint

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_num):
    prime = 0

    for getting_prime in range(2, random_num // 2 + 1):
        if random_num % getting_prime == 0:
            prime += 1
    return prime


def get_game():
    random_num = randint(2, 100)

    if is_prime(random_num) <= 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'Question: {random_num}'
    return question, right_answer
