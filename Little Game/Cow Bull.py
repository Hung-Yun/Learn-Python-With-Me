
"""

Create a program that will play the “cows and bulls” game with the user.
The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
The player wins until they get four cows, since the correct numbers are in the correct places.

"""

import random

def CowBull():
    
    given_number = ""
    for i in random.sample([0,1,2,3,4,5,6,7,8,9],4):
        given_number += str(i)
    # print(given_number) You can print this number to check in advance.
    
    Try = 1
    
    while True:
        cow_bull = [0,0]
        guess_number = str(input("[Give a 4 digit number] "))
        for i in range(4):
            if given_number[i] == guess_number[i]:
                cow_bull[0] += 1
        for j in range(4):
            if guess_number[j] in given_number and given_number[j] != guess_number[j]:
                cow_bull[1] += 1
        print("You got {} cow(s) and {} bull(s).".format(cow_bull[0],cow_bull[1]))
        
        if cow_bull[0] == 4:
            break
        else:
            True
            
        Try += 1
    
    print("You have tried {} times".format(Try))

if __name__=="__main__":
    CowBull()
    
