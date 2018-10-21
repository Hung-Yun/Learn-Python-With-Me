
# As a reminder, our tic tac toe game is really a list of lists.
# The game starts out with an empty game board like this:game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
# Ask the user to enter coordinates in the form “row,col”, a number, then a comma, then a number.
# Then you can use your Python skills to figure out which row and column they want their piece to be in.
# I want to move starting from (1, 1) instead of (0, 0).
# To people who don’t program, starting to count at 0 is a strange concept

game = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

def check_win():
    for i in range(3):
        row = set([game[i][0],game[i][1],game[i][2]])
        if len(row) == 1 and game[i][0] != 0:
            return game[i][0]
        
        column = set([game[0][i],game[1][i],game[2][i]])
        if len(column) == 1 and game[0][i] != 0:
            return game[0][i]
        
        diag1 = set([game[0][0],game[1][1],game[2][2]])
        if len(diag1) == 1 and game[0][0] != 0:
            return game[0][0]
        
        diag2 = set([game[0][2],game[1][1],game[2][0]])
        if len(diag2) == 1 and game[0][0] != 0:
            return game[2][0]
        
def check_space():
    a=1
    for i in range(3):
        for j in range(3):
            a *= game[i][j]
    return a

def player1_input():
    
    player1_input = input("[Player 1 put in x,x to indicate the number of row and column] ")
    row = int(player1_input.split(",")[0])
    column = int(player1_input.split(",")[1])

    if game[row-1][column-1] == 0:
        game[row-1][column-1] = 1
    else:
        print("[Please enter x,x where x from 1 to 3]")
        player1_input()

def player2_input():
    
    player1_input = input("[Player 2 put in x,x to indicate the number of row and column] ")
    row = int(player1_input.split(",")[0])
    column = int(player1_input.split(",")[1])
    
    if game[row-1][column-1] == 0:
        game[row-1][column-1] = 2
    else:
        print("[Please enter x,x where x from 1 to 3]")
        player2_input()
        
def main():

    while True:

        if check_space() == 0:
            player1_input()
        else:
            print("The spaces are full.")
            break
        if check_space() == 0:
            player2_input()
        else:
            print("The spaces are full.")
            break

        print(game,"------------------------",sep="\n")

        if check_win() == 1 or check_win() == 2:
            print("The winner is Player {}".format(check_win()))
            break
        else:
            True
            
if __name__=="__main__":
    main()
