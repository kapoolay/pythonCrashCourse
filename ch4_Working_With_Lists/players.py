# Slicing a List --> PG 96

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# # Slice players 1-3
# print(players[0:4])
#
#
# # Slice players 2-4
# print(players[1:4])
#
# # Without a starting index, Python starts at the beginning of the list
# print(players[:4])
#
# # Omitting the second index includes the beginning index to the end of the list
# # This allows you to output all of the elements from any point in your list to the end, regardless the length of the list
# print(players[3:])
#
#
# # A negative index returns an element a certain distance from the end of a list
# # You can output any slice from the end of a list
# # For example, if we want to output the last 3 players on the roster, we can use the slice players[-3:]
# # You can include a third value in the brackets indicating a slice --> tells Python how many items to skip between items in the specified range
# print(players[-3:])
# print(players[::3])

# ~~~~~~~~~~~~~~~~~~~~~~~LOOPING THROUGH A SLICE~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('Here are the first three players on my team:')

# For every player in players(first 3):
    # Print each player's name as a title
for player in players[:3]:
    print(player.title())
