# hangman-1.py

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
            word_so_far = word_so_far + letter
        else:
            word_so_far = word_so_far + '.'
    return word_so_far


#=====================================================================
# the word that must be guessed
target_word = 'otter'
# a list of the letter guesses made
guesses = ['a', 'e', 'i', 'o', 'u']

print 'Word so far: ' + partial_word(target_word, [])
print 'Word so far: ' + partial_word(target_word, guesses)
print 'Word so far: ' + partial_word(target_word, ['o', 't', 'e', 'r'])

