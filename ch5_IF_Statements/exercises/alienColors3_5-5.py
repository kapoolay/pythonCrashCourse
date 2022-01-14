# Create a variable called 'alien_color'
alien_color = 'green'

# Write an if-elif-else chain statement to test whether the alien's color is green
# If it is, print a message that the player just earned 5 points
# If the alien's color is yellow, print a message that the player earned 10 points
# If the alien's color is red, print a message that the player earned 15 points
# Write 3 versions of this program, making sure each message is printed for the appropriate color alien

if alien_color == 'green':
    print('You earned 5 points!')
elif alien_color == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('\nVersion 2')
alien_color2 = 'yellow'

if alien_color2 == 'green':
    print('You earned 5 points!')
elif alien_color2 == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('\nVersion 3')
alien_color2 = 'red'

if alien_color2 == 'green':
    print('You earned 5 points!')
elif alien_color2 == 'yellow':
    print('You earned 10 points!')
else:
    print('You earned 15 points!')
