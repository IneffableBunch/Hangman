from sys import exit

class Word:

    def __init__(self, word, guesses):
        """Takes the word for the game, and guesses for the player."""
        self.word = word
        self.max_guesses = guesses

        self.player_guesses = 0

        self.hits = set()
        self.misses = set()

    def check_guess_amt(self):
        if self.player_guesses >= self.max_guesses:
            print("You used up all of your guesses!")
            exit(0)

    def guess(self, letter):
        """Checks if letter guessed is in main word.
        :rtype: string
        """
        # Makes sure to quit immediately if player_guesses are equal to max_guesses
        if self.player_guesses >= self.max_guesses:
            print("You used up all of your guesses!")
            exit(0)

        if not (len(letter) >= 2):

            if letter in self.misses:
                self.check_guess_amt()

                return "You already guessed that letter!"
            elif letter in self.word:
                self.hits.add(letter)
                self.player_guesses += 1
                self.check_guess_amt()

                return "You guessed the correct letter!"
            else:
                self.player_guesses += 1
                self.check_guess_amt()

                self.misses.add(letter)
                return "That letter is not in the word."

        else:
            self.check_guess_amt()

            return 'Only guess letters!'

    def word_prog(self):
        """Returns players word progress
        :rtype: string
        """
        guessed_word = ''

        for let in self.word:
            if let in self.hits:
                guessed_word += let
            else:
                guessed_word += '_'

        return guessed_word
