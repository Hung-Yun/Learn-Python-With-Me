
"""

You, the user, will have in your head a number between 0 and 100. 
The program will guess a number, and you will say whether it is too high, too low, or your number.
At the end of this exchange, your program should print out how many guesses it took to get your number.

"""

# The user has to come up with a number ranging from 0 to 100 in mind
import random
mini = 0
maxi = 101
guess = random.randint(mini,maxi)
Try = 1

while True:
    a = input("[Is {} your number] ".format(guess))
    if a == "too high":
        guess -= random.randint(1,10)
    elif a == "too low":
        guess += random.randint(1,10)
    elif a == "correct":
        print("Yes, this is the correct answer.")
        break
    else:
        True
    Try += 1

print("You have tried {} times!" .format(Try))
