# hangman-complete.py

import random


def get_random_word(dictionary_filepath):
    """Pulls one word (line) from the given dictionary."""
    words = []
    with open(dictionary_filepath) as f:
        words = f.readlines()
    # strip whitespace (newline) off the start/end of the string
    return words[random.randint(0, len(words)-1)].strip()


def get_letter_guess():
    """Prompts the user for input until they give us something valid.

    Returns the user's valid letter guess.
    """
    # just keep looping forever; only break or return will get us out
    while True:
        # even though the variable's called "letter", the user could
        # still type anything at all
        letter = raw_input('Guess a letter: ')
        if len(letter) == 1:
            return letter


def is_every_letter_guessed(word, guesses):
    """Returns if every letter in the target word is accounted for in
    the user's guesses.
    """
    # It's easier to check the converse; are we missing anything?  Check
    # if any one of the letters in the target word *isn't* guessed.
    for letter in word:
        if letter not in guesses:
            # Found a letter in the word that hasn't been guessed yet!
            return False
    # If we've reached this point, the whole word has been gone over.
    # Not one of its letters was missing from the list of guesses.
    return True


def partial_word(word, guesses):
    """Returns the target word, each character separated by spaces, with
    letters not yet guessed shown as underscores.
    """
    # gradually build the correctly-guessed/hidden parts of the word
    word_so_far = ''
    for letter in word:
        # write either the current letter of the target word, or a
        # period, depending on if the user has guessed the letter
        # yet or not
        if letter in guesses:
            word_so_far += letter
        else:
            word_so_far += '.'
    return word_so_far


#=====================================================================
# the word that must be guessed
target_word = get_random_word('hangman-dictionary.txt')
# a list of the letter guesses made
guesses = []

# Keep playing until the user guesses every letter in the word
while not is_every_letter_guessed(target_word, guesses):
    print 'Word so far: {}'.format(partial_word(target_word, guesses))
    print 'Guesses so far: {}'.format(guesses)
    guesses.append(get_letter_guess())
    print ''

print 'Found!  The word was "{}"'.format(target_word)
print '  Discovered in {} guesses.'.format(len(guesses))

