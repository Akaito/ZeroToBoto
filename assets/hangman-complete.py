# hangman-complete.py


def is_valid_letter_guess(user_input):
    """Validate a user's input for guessing a single letter.
    
    user_input -- Whatever the user typed in (such as from raw_input()).
    Returns if it's a single, lowercase letter; False otherwise.
    """
    if len(user_input) != 1:
        return False
    # valid if it's a lowercase letter a-z
    if user_input >= 'a' and user_input <= 'z':
        return True
    return False


def get_letter_guess():
    """Prompts the user for input until they give us something valid.

    Returns the user's valid letter guess.
    """
    # just keep looping forever; only break or return will get us out
    while True:
        # even though the variable's called "letter", the user could
        # still type anything at all
        letter = raw_input('Guess a letter: ')
        if is_valid_letter_guess(letter):
            return letter


def is_word_revealed(word, guesses):
    """Returns if every letter in the target word is accounted for in
    the user's guesses.
    """
    # for ... in -style enumerate the characters in the word
    for letter in word:
        # "in"-style check if a value is in a sequence (a list, in our
        # case)
        if letter not in guesses:
            # found a letter in the word that hasn't been guessed yet!
            return False
    return True


def partial_word(word, revealed):
    """Returns the target word, each character separated by spaces, with
    letters not yet guessed shown as underscores.
    """
    # gradually build the revealed/hidden parts of the word
    word_so_far = ''
    for letter in word:
        # write either the current letter of the target word, or an
        # underscore, depending on if the user has guessed the letter
        # yet or not
        if letter in revealed:
            word_so_far += letter
        else:
            word_so_far += '.'
    return word_so_far


#=====================================================================
# the word that must be guessed
target_word = 'otter'
# a list of the letter guesses made
guesses = []

# Keep playing until the user guesses every letter in the word
while not is_word_revealed(target_word, revealed):
    print 'Word so far: {}'.format(partial_word(target_word, revealed))
    print 'Guesses so far: {}'.format(revealed)
    guesses.append(get_letter_guess())
    print ''

print 'Found!  The word was "{}"'.format(target_word)
print '  Discovered in {} guesses.'.format(len(guesses))

