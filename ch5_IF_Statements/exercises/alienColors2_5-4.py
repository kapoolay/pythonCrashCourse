# Create a variable called 'alien_color'
alien_color = 'green'

# Write an if-else statement to test whether the alien's color is green
# If it is, print a message that the player just earned 5 points
# If the alien's color isn't green, print a message that the player earned 10 points
# Write one version of this program that passes the if test and another that runs the else block

if alien_color == 'green':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')

print('\n')

# The version that fails will have no output
if alien_color == 'red':
    print('You just earned 5 points!')
else:
    print('You just earned 10 points!')
