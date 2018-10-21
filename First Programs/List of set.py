
"""

Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

"""

import numpy

# The first function used for and if to iterate the elements in that list
def dupe1(a):
    y=[]
    for i in a:
        if i not in y:
            y.append(i)
    y.sort()
    return y

# The second one used list(set(a)) to remove duplicates directly.
def dupe2(a):
    return list(set(a))

a=[1,2,3,5,6,7,5,4,2,1]
print(dupe1(a))
print(dupe2(a))
