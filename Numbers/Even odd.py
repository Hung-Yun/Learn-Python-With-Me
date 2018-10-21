
"""

Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.

"""

def main():
    
    number = int(input("Give me an integer."))

    if number % 2 == 0:
        print("Hey your number is even.")
        
    elif number % 2 == 1:
        print("Hey your number is odd.")
        
    else:
        print("This is not an integer.")
        main()

if __name__=="__main__":
    main()
