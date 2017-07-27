# hangman-0.py

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


#=====================================================================
# the word that must be guessed (hard-coded for now)
target_word = 'otter'

letter = get_letter_guess()

if letter in target_word:
    print '{} is in the word!'.format(letter)
else:
    print '{} is NOT in the word.'.format(letter)

