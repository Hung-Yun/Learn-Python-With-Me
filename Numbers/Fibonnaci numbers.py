
"""

Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

"""

def fibo():

    number = int(input("How many Fibonnaci numbers do you want to generate"))

    # If input 1 or 2, the result would be trivial.
    if number==1:
        print([1])
    elif number==2:
        print([1,1])

    # If input larger than 2, we apply the formula of Fibonnaci numbers.
    else:
        a=[1,1]
        for i in range(2,number):
            a.append(a[i-1]+a[i-2])
        print(a)

if __name__=="__main__":
    fibo()
