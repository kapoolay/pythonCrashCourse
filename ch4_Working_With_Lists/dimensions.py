# Tuples is a list that cannot change
# Python refers to values that cannot change as 'immutable', and an immutable list is called a tuple
# A tuple looks just like a list except you use parenthesis instead of square brackets

dimensions = (200, 50)

# # try to change one of the items in the list
# # this creates an error
# dimensions[0] = 250

# print(dimensions[0])
# print(dimensions[1])

# Loop through tuple
print('\nOG Dimension:')
for dimension in dimensions:
    print(dimension)

# If you want to define a tuple with one element, you need to include a trailing comma
my_t = (3,)
# It doesn't often make sense to build a tuple with one element, but this can happen when tuples are generated automatically


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Writing over a tuple
# You can't modify a tuple, but you can assign a new value to a variable that represents a tuple
dimensions = (400, 100)
print('\nNew Dimension:')
for dimension in dimensions:
    print(dimension)
