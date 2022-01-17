# Ordinal numbers indicate their position in a list
# Such as 1st or 2nd
# Most ordinal numbers end in "th", except 1, 2, and 3

# Store numbers 1-9 in a list
# Loop through the list
# Use an if-elif-else to print the proper ordinal ending for each number
# Your output should read "1st 2nd 3rd 4th 5th 6th 7th 8th 9th"
# Each result should be on a separate line

# Review --> print range 1-9
for i in range(1, 10):
    print(i)

# Put range 1-9 in a list
numbers = list(range(1,10))
print(numbers)

# Review --> print range 1-9
for i in range(1, 10):
    print(i)

# For each i in numbers
# If i is 1, print 1 with "st"
# Elif i is 2, print 2 with "nd"
# Elif i is 3, print 3 with "rd"
# Else print with "th"

for i in numbers:
    if i == 1:
        print(f'{i}st')
    elif i == 2:
        print(f'{i}nd')
    elif i == 3:
        print(f'{i}rd')
    else:
        print(f'{i}th')


# Styling if statements
# The only recommendation is to use a single space around comparison operators
# Example
if age < 4:
# is better than:
if age<4:
