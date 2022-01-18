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
# Adding new key-value pairs

alien_o = {
'color': 'green',
'points': 5,
}

print(alien_o)
alien_o['xAxis'] = 0
alien_o['yAxis'] = 25
print(alien_o)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Starting with an empty dictionary

# define the dictionary name with empty braces
alien_o = {}

# Add key/value pairs on its own line
alien_o['color'] = 'green'
alien_o['points'] = 5
print(alien_o)
