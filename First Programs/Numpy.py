
"""

Learn how to use the package numpy.
I would use several simple practice to illustrate some simple methods and functions in numpy.

"""

# Import the numpy package under the name np
import numpy as np

# Use np.__version__ to see the version of numpy
print("The version of numpy is ", np.__version__, end="\n")

# Create a null vector of size 10
null_vector = np.zeros(10)
print("The null vector of size 10 is ", null_vector, end="\n")

# Create a null vector of size 10 but the fifth value which is 1
null_vector[4] = 1
print("Beware the fifth element of this null vector: ", null_vector, end="\n")

# Create a vector with values ranging from 10 to 25
vector_range = np.arange(10,26)
print(vector_range)

# Reverse a vector (first element becomes last)
# Suppose we build a vector "a" from 0 to 9
# We can use [x:y:z] to illustrate the way of index.
a = np.arange(10)
print("This is the original a:", a)
a[0:6:2] = 10 # from the 0th to 6th position, set every 2nd element to the value 10.
print("We change some value accordingly:", a)
a = a[::-1] # this way we could reverse the vector.
print("We reverse the sequence of a:", a)

# To make a matrix, we can use reshape
print("Make it a 5x2 matrix!\n", a.reshape(5,2))

# Or we can start from using np.arange
a = np.arange(9).reshape(3,3)
print("Make it a 3x3 matrix!\n", a)

# Find indices of non-zero elements from [1,2,0,0,4,0]
z = [1,2,0,0,4,0]
nz = np.nonzero(z)
print("The indices of nonzero elements in the vector are ", nz)

# Create a 3x3 identity matrix
z = np.eye(3)
print(z)

# Create a 3x3x3 array with random values
z = np.random.random((3,3,3))
print("The random array is quite long!\n", z, "\nFinally ends!")

# Create a 10x10 array with random values and find the minimum and maximum values
z = np.random.random((10,10))
zmin, zmax = z.min(), z.max()
print("The minimum is", zmin,"\nThe maximum is", zmax)
print("We can find out the data type (dtype) is", z.dtype)

# Create a random vector of size 30 and find the mean value
z = np.random.random(30)
print("The mean value of a random array: ", z.mean())
