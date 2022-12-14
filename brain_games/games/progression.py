from random import randint

RULE = 'What number is missing in the progression?'


def generate_progression():
    length = randint(5, 10)
    step = randint(2, 10)
    start = randint(1, 100)
    progression = []
    counter = 1
    for num in range(length):
        progression.append(start + step * counter)
        counter += 1
    return progression


def get_game():

    progression = generate_progression()
    hide_random_num = randint(0, len(progression) - 1)
    right_answer = str(progression[hide_random_num])
    progression[hide_random_num] = '..'
    question = f'Question: {" ".join(map(str, progression))}'
    return question, right_answer
