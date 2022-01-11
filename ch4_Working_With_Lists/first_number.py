for value in range(1, 5):
    print(value)

# The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you provide, never containing the end value, which is 5 in this case.

# To pring the numbers from 1-5, your range values need to be 1 and 6
print('\nValues 1-5:')
for value in range(1, 6):
    print(value)


# You can also pass range() only one argument, and it will start the sequence at 0
print('\nPassing Only 1 Arguement:')
for value in range(5):
    print(value)


# Converting the results of a range into a List
numbers = list(range(5))
print(f'\nRange results to List:')
print(numbers)
