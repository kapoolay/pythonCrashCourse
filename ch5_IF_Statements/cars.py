# cars = ['audi', 'bmw', 'subaru', 'toyota']
#
# # Loops through the list of car names and looks for value 'bmw'. Print 'bmw' in uppercase instead of title case
#
# for car in cars:
#     # if the value is 'bmw' print in upper()
#     if car == 'bmw':
#         print(car.upper())
#     # else if the value is anything else, print in title()
#     else:
#         print(car.title())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# CONDITIONAL TESTS

# A single equal sign (=) sets the value of the variable
# "Set the value of car equal to 'audi'"
# car = 'bmw'

# A double equal sign (==) checks the value of the variable
# "Is the value of car equal to 'bmw'?"
car == 'bmw'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Case Checking for equality
# Testing for equality is case sensitive in Python
# 2 values with different capitalization are not considered equal
>>> car = 'Audi'
>>> car == 'audi'
False

# If case matters, then you're good
# If case doesn't matter,  you can convert the variable's value to lowercase before doing the comparison:
>>> car = 'Audi'
>>> car.lower() == 'audi'
True
>>> car
'Audi'
