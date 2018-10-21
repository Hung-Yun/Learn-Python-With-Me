
"""

This is also a way of finding whether the given number is a prime number.
But it is quite lengthy.
Just to practice how to use functions!

"""

def get_number(n):
    """return the integer of an input, while n is the message."""
    return int(input(n))

def is_prime(number):
    """return True if the number of input is a prime number"""
    if number == 1:
        prime = False
    elif number == 2:
        prime = True
    else:
        prime = True
        for check in range(2, int(number/2)+1):
            if number%check ==0:
                prime = False
                break
    return prime

def print_prime(number):
    prime = is_prime(number)
    if prime:
        descriptor = ""
    else:
        descriptor = "NOT"
    print(number," is",descriptor," a prime number.",sep="",end="\n")

if __name__=="__main__":
    print_prime(get_number("[Give me a number] "))
