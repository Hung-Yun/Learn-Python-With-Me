
"""

Find e to the Nth Digit - Enter a number and have the program generate e up to that many decimal places.
Keep a limit to how far the program will go.

"""

from math import factorial
from decimal import Decimal, getcontext

def main():

    # The number of digits is determined by getcontext().prec
    n = int(input("How many digits of e would you like?"))
    getcontext().prec = 10
    
    e = 0
    
    for i in range(15):
        e += (factorial(i))**(-1)

    print(e)

if __name__=="__main__":
    main()
