
"""

A happy number is defined by the following process.
Starting with any positive integer, replace the number by the sum of the squares of its digits
repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers,
while those that do not end in 1 are unhappy numbers.
Display all the Happy Numbers in from 1 to 1000.

"""
Happylist = []

for n in range(1,1000):

    # Add up all the square value of each digit in n
    a = sum([ int(i)**2 for i in list(str(n)) ])

    while True:

        # a == 1 means Happy number!
        if a == 1:
            Happylist.append(n)
            break

        # a == 4 means it will enter an evil loop and never ends!
        elif a == 4:
            break

        # Just do the same thing, adding up the square value of each digit, but use m because I don't want to erase n.
        else:
            m = list(str(a))
            a = sum([ int(i)**2 for i in m ])
                
print(Happylist)
