
"""

Write a password generator in Python.
The passwords should be random, generating a new password every time the user asks for a new password.

"""

def password():

    import random
    s = "1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    length = int(input("[How many digits do you want for your password?] "))
    password = ""
    for i in random.sample(s,length):
        password += str(i)
    print("Your password is {}".format(password))
    
def main():
    new_one = str(input("[Do you want a new password] (y/n) "))
    if new_one == "y":
        password()
    elif new_one == "n":
        print("Your password is given.")
    else:
        print("Please type y or n.")
        main()

if __name__ == "__main__":
    main()
