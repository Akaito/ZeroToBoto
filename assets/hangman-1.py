# hangman-1.py

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


#=====================================================================
# the word that must be guessed (hard-coded for now)
target_word = 'otter'
# a list of the letter guesses made
guesses = []

# keep playing until the user guesses every letter in the word
while not is_every_letter_guessed(target_word, guesses):
    print 'Guesses so far: {}'.format(guesses)
    guesses.append(get_letter_guess())
    print ''

print 'Found!  The word was "{}"'.format(target_word)

