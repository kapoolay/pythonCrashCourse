# A number raised to the third power is called a cube
# Example: the cube of 2 is written 2**3 in Python

# Make a list of the first 10 cubes (integers 1-10)
# Use a for loop to print out the value of each cube

# cubes = range(1,11)
#
# for value in cubes:
#     print(value**3)




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Exercise 4-9 Cube Comprehension
# Make a list of the first 10 cubes (integers 1-10)
# Use a for loop to print out the value of each cube

# LIST = [EXPRESSION ForLoop]

cubes = [value**3 for value in range(1,11)]
print(cubes)
