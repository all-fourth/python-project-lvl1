import operator
import random

RULES = 'What is the result of the expression?'
OPERATORS = ({
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
})


def getting_result():

    random_num1 = random.randint(1, 100)
    random_num2 = random.randint(1, 100)
    rand_operator = random.choice(list(OPERATORS.keys()))
    right_answer = str(OPERATORS.get(rand_operator)(random_num1, random_num2))
    question = f'Question: {random_num1} {rand_operator} {random_num2}'
    return question, right_answer
