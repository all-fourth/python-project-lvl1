from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    random_int = randint(1, 100)
    prime = 0
    for getting_prime in range(2, random_int // 2 + 1):
        if random_int % getting_prime == 0:
            prime += 1
    return random_int, prime


def getting_result():
    random_int, prime = is_prime()
    if prime <= 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'Question: {random_int}'
    return question, right_answer
