# Using get() to Access values

alien_o = {
    'color': 'green',
    'speed': 'slow',
}

# # print a key that doesn't exist
# print(alien_o['points'])

# Results in an error
# You can use the get() method to set a default value that will be returned if the requested key doesn't exist
# get() requires a key as a first argument
# a second optional argument can be passed to be returned if the key doesn't exist

point_value = alien_o.get('points', 'No point value assigned')
print(point_value)
