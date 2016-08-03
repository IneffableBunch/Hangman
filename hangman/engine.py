from random import randint

from hangman.hmmanager import Word


def game_engine():
    randwords = ['daughter', 'development', 'amusement', 'birthday', 'cakes', 'cloth']

    game_word = randwords[randint(0, 5)]
    game_max_guesses = round(len(game_word) * 1.3)

    hmgame = Word(game_word, game_max_guesses)

    while True:
        print("\nYou have {0} guesses left.".format(hmgame.max_guesses - hmgame.player_guesses))
        guess = input("Your guess: ")

        print(hmgame.guess(guess))
        print(hmgame.word_prog())


if __name__ == '__main__':
    game_engine()
