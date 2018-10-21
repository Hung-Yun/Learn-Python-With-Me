
"""

Write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

"""

# Suppose we have two lists: a and b
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# We can use list comprehension to finish this very quickly
A = [i for i in a if i in b]
print(A)
