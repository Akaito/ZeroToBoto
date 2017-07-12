# hangman-0.py

def partial_word(word, revealed):
    """Returns the target word, each character separated by spaces, with
    letters not yet guessed shown as underscores.
    """
    # gradually build the correctly-guessed/hidden parts of the word
    word_so_far = ''
    for letter in word:
        # write either the current letter of the target word, or a
        # period, depending on if the user has guessed the letter
        # yet or not
        if revealed:
            word_so_far = word_so_far + letter
        else:
            word_so_far = word_so_far + '.'
    return word_so_far


#=====================================================================
# the word that must be guessed
target_word = 'otter'

print 'Word so far: ' + partial_word(target_word, True)
print 'Word so far: ' + partial_word(target_word, False)

