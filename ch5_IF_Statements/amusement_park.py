# Admission
# < 4 --> free
# < 18 --> $25
# >= 18 --> $40

# Use and if statement to determine a person's admission rate

age = 66

# if age < 4:
#     print('You are free to go in!')
# elif age < 18:
#     print('Please pay $25.')
# else:
#     print('Please pay $40.')

# More concise code
# Add another elif for senior discounts >= 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f'Your admission is ${price}.')

# Omitting the else block
# Python doesn't require an else block
# With no else statement, every block of code must pass a specific test in order to be executed
# else block is a catchall statement
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f'Your admission is ${price}.')
