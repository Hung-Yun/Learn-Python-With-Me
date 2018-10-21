
"""

Make a two-player Rock-Paper-Scissors game.
Ask for player plays (using input), compare them, 
print out a message of congratulations to the winner, 
and ask if the players want to start a new game.

"""

def main():
    
    while True:
        
        game_dict = {"paper":1, "rock":2, "scissors":3}
        player1 = str(input("[Player1 choose one: paper, rock, scissors] "))
        player2 = str(input("[Player2 choose one: paper, rock, scissors] "))

        if player1 in game_dict and player2 in game_dict:
            if game_dict[player1]-game_dict[player2] == 0:
                print("Even")
            elif game_dict[player2]-game_dict[player1] in [-1,2]:
                print("Player2 wins")
            else:
                print("Player1 wins")
        else:
            print("Please choose paper, rock, or scissors.")
            
        a = input("Do you want to play again? (y/n) ")
        
        if str(a)=="n":
            break
        else:
            True

if __name__=="__main__":
    main()
