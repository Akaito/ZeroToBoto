# Guessing game (step 0)

# Store off the computer's target number.
# We're using a string here, instead of an integer, so we can
# directly compare it to the return of raw_input() (the user's typed-in guess).
my_number = '4'

# Take user input with a prompt.
user_guess = raw_input("Guess my number (1-5): ")

# Write "True" or "False", depending on if they got it right or wrong, respectively.
print my_number == user_guess

