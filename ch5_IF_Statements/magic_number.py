# Print a message if the fiven answer is not correct

answer = 17

if answer != 42:
    print('That is not the correct answer!')
# The conditional test passes, because the value of answer(17) is not equal to 42
# Bc the test passes, the indented code block is executed

age_0 = 22
age_1 = 20

# Adding parenthesis around each individual test improves readability, but not required

# keyword 'and' needs both conditions to pass to be considered true
if (age_0 >= 21) and (age_1 >= 21):
    print('Yes both are over 21')
else:
    print('No, only one is over 21')

# keyword 'or' only needs one of the two conditions to pass to be considered true
if (age_0 >= 21) or (age_1 >= 21):
    print('At least one person is over 21')
else:
    print('False, no one is over 21')
