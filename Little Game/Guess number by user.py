
"""

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, tell them whether they guessed too low, too high, or exactly right.

"""

import numpy

# Randomly create an integer from 1 to 9
a = numpy.random.randint(1,10)

# Keep track of the times the user guessed.
Try = 1

# Start guessing
while True:
    inp = int(input("[Guess a number from 1 to 9] "))
    if inp>a:
        print("[you guess too high]")
    elif inp<a:
        print("[you guess too low]")
    else:
        print("CORRECT!")
        break
    Try += 1

print("you have tried "+ str(Try)+" times")

