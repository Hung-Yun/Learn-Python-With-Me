
"""

Ask the user for a number and determine whether the number is prime or not.

"""

def prime():
    
    a = int(input("[Give me a number] "))

    # One is special, so it is discussed here.
    if a == 1:
        print("Not prime")

    # For other numbers, we use list comprehension to see if the length of b is larger than 0
    # If it is larger than 0, that means there is at least an "i" that makes a%i == 0
    else:
        b = [i for i in range(2,a) if a%i==0]
        if len(b)>0:
            print("Not prime")
        else:
            print("Prime")

if __name__=="__main__":
    prime()
