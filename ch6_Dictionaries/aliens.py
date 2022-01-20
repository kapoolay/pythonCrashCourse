# # A dictionary in Python is a collection of key-value pairs
# # Simple dictionary that stores information about a particular alien
#
# alien_o = {
    # 'color': 'green',
    # 'points': 5,
    # 'keyEx3': 'value',
    # }
#
# print(alien_o['color'])
# print(alien_o['points'])
# print(alien_o['keyEx3'])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# # Accessing Values in a dictionary
# # Give the name of the dictionary
# # Place the key inside a set of square brackets
# myDictionary = {'key1': 'exampleValue'}
# print(myDictionary['key1'])

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # If a player shoots down this alien you can look up how many points they should earn using this code:
# alien_o = {
    # 'color': 'green',
    # 'points': 5,
    # }
#
# newPoints = alien_o['points']
# print(f'You just earned {newPoints} points! Congrats!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Adding new key-value pairs
#
# alien_o = {
    # 'color': 'green',
    # 'points': 5,
    # }
#
# print(alien_o)
# alien_o['xAxis'] = 0
# alien_o['yAxis'] = 25
# print(alien_o)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Starting with an empty dictionary
#
# # define the dictionary name with empty braces
# alien_o = {}
#
# # Add key/value pairs on its own line
# alien_o['color'] = 'green'
# alien_o['points'] = 5
# print(alien_o)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Empty Dictionary
#
# person1 = {}
#
# person1['firstName'] = 'kevin'
# person1['lastName'] = 'capule'
# person1['age'] = '30'
# print(person1)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Modifying Values in Dictionary
#
# alien_o = {
    # 'color': 'green',
    # 'points': 5,
    # }
# # Double quotes are needed for the f"" since the variable includes 'color'
# print(f"The alien is {alien_o['color']}.")
#
# # Modify the alien from green to yellow
# alien_o['color'] = 'yellow'
# print(f"The alien is now {alien_o['color']}.")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Track the position of an alien that can move at different speeds
#
# alien_o = {
#     'x': 0,
#     'y': 25,
#     'speed': 'medium'
#     }
# # print(alien_o)
#
# # Move the alien to the right
# # Determine how far to move the alien based on its current speed
# # 'slow' = +1
# # 'medium' = +2
# # 'fast' = +3
#
# # make the alien faster
# alien_o['speed'] = 'fast'
#
# if alien_o['speed'] == 'slow':
#     x_increment = 1
# elif alien_o['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment = 3
#
# print(f"Original Position: {alien_o['x']}")
#
# # The new position is the old position plus the x_increment
# alien_o['x'] = alien_o['x'] + x_increment
# print(f"New Position: {alien_o['x']}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Removing Key-Value Pairs (permanently)
#
# alien_o = {
#     'color': 'green',
#     'points': 5,
#     'keyEx3': 'value'
#     }
#
# # Remove the key "keyEx3" from the dictionary
# del alien_o['keyEx3']
# print(alien_o)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Dictionary of Similar Objects

favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
    }

# What's Kevin's favorite language?
print(favoriteLanguages['kevin'])
language = favoriteLanguages['kevin'].title()
print(f"Kevin\'s favorite language is {language}")
