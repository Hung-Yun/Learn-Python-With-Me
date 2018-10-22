
"""

Next Prime Number
Generate prime numbers until the user chooses to stop

"""

def prime(n):
    
        factor = [i for i in range(2,n) if n%i==0]
        if len(factor)>0:
            return False
        else:
            return True

def main():

    # Display the first prime number
    current_prime = 2
    print("The first prime number is {}. ".format(current_prime))

    # Start the loop of asking next prime number
    while True:
        nextprime = input("Do you want to know the next prime? y/n ")
        if nextprime == "y":

            # Start the loop of testing whether the current number is a prime
            while True:
                current_prime += 1

                # If the current number is not a prime, it would +1 as it is still in the loop.
                if prime(current_prime) == True:
                    print("The next prime number is {}. ".format(current_prime))
                    break
        else:
            break

if __name__=="__main__":
    main()
