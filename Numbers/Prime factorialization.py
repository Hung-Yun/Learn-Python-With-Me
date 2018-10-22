
"""

Prime Factorization
Have the user enter a number
and return its prime factors
Extra: show the exponent of the prime factors as well

"""

def prime_factors(n):

    # Find out all the factors11
    factors = [ i for i in range(2,n+1) if n%i == 0 ]

    # Create a list to store the factor if the factor is a prime number.
    prime_factors = []
    for i in factors:

        # check_factors is to check whether the item is a prime
        check_factors = [ j for j in range(1,i+1) if i%j == 0 ]

        # The length of check_factors == 2 means it only contains the factor 1 and itself
        if len(check_factors) == 2:
            prime_factors.append(i)
            
    return prime_factors

def main():

    # Input a number
    n = int(input("Give a number. We will finish the prime factorialization. "))

    # Create a dictionary where index is the prime factor, and the value is the exponent.
    fact_expo = {}

    # Create a loop that goes through each factor in prime factors.
    for i in prime_factors(n):
        count = 0
        number = n

        # If number%i == 0, that means it could be divided again.
        while number % i == 0:
            count += 1
            number /= i
        fact_expo[i] = count

    for key, value in fact_expo.items():
        print(key, "^", value, sep = "")
    
if __name__=="__main__":
    main()
