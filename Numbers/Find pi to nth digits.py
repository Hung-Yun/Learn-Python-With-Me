
"""

Find PI to the Nth Digit - Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.

"""

from math import factorial
from decimal import Decimal, getcontext

# The number of digits is determined by getcontext().prec
n = int(input("How many digits of pi would you like?"))
getcontext().prec = n+1

def main():
    
    # Chudnovsky algorithm, reference: https://en.wikipedia.org/wiki/Chudnovsky_algorithm

    k = 0
    InSigma = 0

    for k in range(10):
        InSigma += (-1)**k * factorial(6*k) * (545140134*k+13591409) / (factorial(3*k) * factorial(k)**3 * 640320**(3*k+1.5))
        
    pi = (12 * Decimal(InSigma))**(-1)

    print(pi)
    
if __name__=="__main__":
    main()
