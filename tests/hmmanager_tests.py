from nose.tools import *

from hangman.hmmanager import Word


def test_word():
    word_class = Word('test', 5)

    assert_equals(word_class.word, 'test')
    assert_equals(word_class.max_guesses, 5)


def test_guess_checker():
    word_class = Word('test', 1)

    # try:
    #    assert_raises(SystemExit, word_class.guess('c'))
    # except SystemExit:
    #     pass

def test_guess():
    word_class = Word('test', 5)

    assert_equals(word_class.guess('t'), "You guessed the correct letter!")
    assert_equals(word_class.player_guesses, 1)
    assert_in('t', word_class.hits)

    assert_equals(word_class.guess('z'), "That letter is not in the word.")
    assert_equals(word_class.player_guesses, 2)
    assert_in('z', word_class.misses)
    assert_not_in('z', word_class.hits)

    assert_equals(word_class.guess('z'), "You already guessed that letter!")
    assert_equals(word_class.player_guesses, 2)
    assert_in('z', word_class.misses)
    assert_not_in('z', word_class.hits)

def test_word_prog():
    word_class = Word('test', 5)

    word_class.guess('t')
    assert_equals(word_class.player_guesses, 1)
    assert_equals(word_class.word_prog(), 't__t')
