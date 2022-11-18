import prompt


def logic(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    correct_answers = 0
    for repetition in range(3):
        answer, right_answer = game.question_and_answer()
        if answer == right_answer:
            print('Correct!')
            repetition += 1
            correct_answers += 1
        else:
            return print(f"'{answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
    print(f'Congratulations, {name}!')
