
"""

Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
(If you don’t know what a divisor is, it is a number that divides evenly into another number.
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

"""

# First we ask the user to input an integer
a = input("give me an integer: ")

# Then we use list comprehension to deal with it
# Remember to change the data type of a into int.
# int(a)%int(i) == 0 means it is the divisor of that integer
A = [ i for i in range(1,int(a)+1) if int(a) % int(i) == 0 ]
print(A)
