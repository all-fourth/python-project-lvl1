import prompt


def get_answer(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULES)
    for repeat in range(3):
        question, right_answer = game.getting_result()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
            repeat += 1
        else:
            return print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'. "
                f"Let's try again, {name}!",
            )
    print(f'Congratulations, {name}!')
