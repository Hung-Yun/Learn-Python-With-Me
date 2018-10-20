
"""

This project is to show how to input information.

"""

def main(): # wrapper function

    name = input("[Please enter your name.] ")
    print("Hi, {}. Nice to see you. ".format(name))
    age = input("[How old are you.] ")
    print("Glad to know that you are", age, "years old.", sep=" ", end="\n")

if __name__=="__main__":
    main()