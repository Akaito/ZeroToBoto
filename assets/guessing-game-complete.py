# Guessing game (completed)

import random

# Prepare the random number generator so we don't just get the
# same random number each time.
random.seed()
# Store off the computer's randomized target number.
my_number = random.randint(1, 100)

# We need to declare the user's guess variable to use it in the while loop
# below, but don't want it to already be correct.  So just store some
# value that the computer won't come up with for its number.
user_guess = -1

while user_guess != my_number:
    # Take user input with a prompt, and convert it to an int.
    user_guess = int(raw_input("Guess my number (1-100): "))

    # Help guide the human to the right answer.
    if user_guess < my_number:
        print "Too low."
    if user_guess > my_number:
        print "Too high."

# This won't be hit until the while loop ends, when the guess matches my_number.
print "Correct!  My number was", my_number

