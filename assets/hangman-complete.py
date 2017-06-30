# hangman-complete.py

# the word that must be guessed
word = 'otter'
# a list of the letter guesses made
guesses = []


# user_input: whatever the user typed in (such as from raw_input())
# returns: True if it's a single, lowercase letter; False otherwise
def is_valid_letter_guess(user_input):
    if len(user_input) != 1:
        return False
    # valid if it's a lowercase letter a-z
    if user_input >= 'a' and user_input <= 'z':
        return True
    return False


# keeps prompting the user for input until they give us something valid
# returns: the user's valid letter guess
def get_letter_guess():
    # just keep looping forever; only break or return will get us out
    while True:
        # even though the variable's called "letter", the user could still type anything at all
        letter = raw_input('Guess a letter: ')
        if is_valid_letter_guess(letter):
            return letter


# returns: True if every letter in the target word is accounted for in the user's guesses
def is_word_revealed():
    # for ... in -style enumerate the characters in the word
    for letter in word:
        # "in"-style check if a value is in a sequence (a list, in our case)
        if letter not in guesses:
            # found a letter in the word that hasn't been guessed yet!
            return False
    return True


def partial_word():
    word_so_far = ''
    for letter in word:
        if letter in guesses:
            word_so_far += letter
        else:
            word_so_far += '_'
        word_so_far += ' '
    return word_so_far


while not is_word_revealed():
    print 'Word so far: {}'.format(partial_word())
    print 'Guesses so far: {}'.format(guesses)
    guesses.append(get_letter_guess())
    print ''

print 'Found!  The word was "{}"'.format(word)
print '  Discovered in {} guesses.'.format(len(guesses))

