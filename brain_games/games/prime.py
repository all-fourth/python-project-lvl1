from random import randint

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime():
    random_num = randint(1, 100)
    prime = 0
    for getting_prime in range(2, random_num // 2 + 1):
        if random_num % getting_prime == 0:
            prime += 1
    return random_num, prime


def getting_result():
    random_num, prime = is_prime()
    if prime <= 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    question = f'Question: {random_num}'
    return question, right_answer
