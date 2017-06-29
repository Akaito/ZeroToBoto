# hangman-complete.py

word = 'otter'
guesses = []


def is_valid_letter_guess(user_input):
    if len(user_input) != 1:
        return False
    if user_input >= 'a' and user_input <= 'z':
        return True
    if user_input >= 'A' and user_input <= 'Z':
        return True
    return False


def get_letter_guess():
    letter_guess = ''
    while True:
        letter = raw_input('Guess a letter: ')
        if is_valid_letter_guess(letter):
            return letter


def is_word_revealed():
    for letter in word:
        if letter not in guesses:
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

print 'Found!  The word was "{}"'.format(word)
print '  Discovered in {} guesses.'.format(len(guesses))

