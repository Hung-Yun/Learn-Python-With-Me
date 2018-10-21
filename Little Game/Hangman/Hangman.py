
def game():

    """In this game, you are asked to guess all the letters in a word from sowpods.txt.
       If the word is, let's say, "SUPERMAN."
       You enter the letter "s". Then it would display "S-------".
       If the letter you entered is not in the word, you would have six chances to guess again."""
    
    # import a new word called "problem"
    import numpy
    with open('sowpods.txt') as f:
        words = list(f)
    random = numpy.random.randint(len(words))
    problem = words[random].split("\n")[0]
    
    # make the problem a list in order to slice and index
    listproblem = list(problem)
    display = "-"*len(problem)
    listdisplay = list(display)
    error = 6
    Try = 0
    
    while error > 0:

        letter = input("[Enter a letter] ")
        Try += 1

        if letter.upper() in listdisplay:
            print("Already guessed!")
        elif letter.upper() in listproblem:
            while letter.upper() in listproblem:
                index = listproblem.index(letter.upper())
                listdisplay[index] = letter.upper()
                listproblem[index] = " "
            string = ""
            for i in listdisplay:
                string += i
            print(string)
        else:
            error -= 1
            print("Not in the word")
            print("You still have {} chances to guess.".format(error))

        if len(set(listproblem)) == 1:
            print("You guess the word!")
            print("You have tried {} times.".format(Try))
            break
            
    if len(set(listproblem)) > 1:
        print("You lose.")

def main():
    while True:
        start = input("[Do you want to start a new game?] y/n ")
        if start != "n":
            game()
        else:
            break

if __name__=="__main__":
    main()
