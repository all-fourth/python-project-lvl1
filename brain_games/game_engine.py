import prompt


def start_game(game):

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for repeat in range(3):
        question, right_answer = game.get_game()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == right_answer:
            print('Correct!')
        else:
            return print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{right_answer}'. "
                f"Let's try again, {name}!",
            )
    print(f'Congratulations, {name}!')
