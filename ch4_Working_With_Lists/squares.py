# Make a list of the first 10 square numbers (the square of each integer from 1-10)
# In Python, 2 asterisks (**) represent exponents

# Create an empty List
squares = []
# # Tell Python to look through each value from 1-10 using the range()
# for value in range(1,11):
#     # Current value is raised to the second power and assigned to the variable square
#     square = value ** 2
#     # Each new value of square is appended (added to the end) to the list squares
#     squares.append(square)
# # The list of squares is printed
# print(squares)



# Write this program more concisely, and omit the variable square and append each new value directly to the List
# print('\nMore Concise Code:')
# squares =[]
# for value in range(1,11):
#     squares.append(value ** 2)
# print(squares)




# ~~~~~~~~~~~~~~~~~~~~~~~~~LIST COMPREHENSIONS PAGE 95~~~~~~~~~~~~~~~~~~~~~~~~~~~
# List comprehension allows you to generate the code above in just one line of Code
# Combines the for loop and the creation of new elements into one line, and automatically appends each new element

# ListName = [EXPRESSION FOR LOOP]
# print(ListName)

squares = [value**2 for value in range(1,11)]
print(squares)

addtwo = [value+2 for value in range(1,5)]
print(addtwo)
