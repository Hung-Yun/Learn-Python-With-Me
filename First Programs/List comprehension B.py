
"""

Write a program that prints out all the elements of the list that are less than 5.

"""

# Again, let's say we have a list called "a"
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# We can use list comprehension to finish this.
A = [i for i in a if i<5]
print(A)
