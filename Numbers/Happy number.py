
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
    a = sum([ int(i)**2 for i in list(str(n)) ])
    while True:
            if a == 1:
                Happylist.append(n)
                break
            elif a == 4:
                break
            else:
                m = list(str(a))
                a = sum([ int(i)**2 for i in m ])
                
print(Happylist)
