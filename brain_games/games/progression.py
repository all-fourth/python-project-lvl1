import random

import prompt

RULES = 'What number is missing in the progression?'


def question_and_answer():
    length = random.randint(5, 10)
    step = random.randint(2, 10)
    start = random.randint(1, 100)
    progression = []

    counter = 1
    for num in range(length):
        progression.append(start + step * counter)
        counter += 1
    hide_random_num = random.randint(0, len(progression) - 1)
    right_answer = str(progression[hide_random_num])
    progression[hide_random_num] = '..'
    answer = prompt.string(
        f'Question: {" ".join(map(str, progression))}\n'
        f'Your answer: ',
    )

    return answer, right_answer
