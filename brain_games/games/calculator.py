import operator
import random
import types

import prompt

RULES = 'What is the result of the expression?'
OPERATORS = types.MappingProxyType({
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
})


def question_and_answer():

    int_one = random.randint(1, 100)
    int_two = random.randint(1, 100)
    rand_operator = random.choice(list(OPERATORS.keys()))
    right_answer = str(OPERATORS.get(rand_operator)(int_one, int_two))
    answer = prompt.string(
        f'Question: {int_one} {rand_operator} {int_two}\nYour answer: ',
    )

    return answer, right_answer
