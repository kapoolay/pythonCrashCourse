# alien_0 = {"color": "green", "points": 5}
# alien_1 = {"color": "yellow", "points": 10}
# alien_2 = {"color": "red", "points": 15}
#
# aliens = [alien_0, alien_1, alien_2]
#
# # Loop thru the list [aliens]
# for alien in aliens:
#     print(alien)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Make an empty list for storing aliens
# aliens = []
#
# # Make 30 aliens
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
# # Show the first 5 aliens using a slice
# for alien in aliens[:5]:
#     print(alien)
# print('...')
#
# # Show how many aliens have been created
# print(f"Total Aliens: {len(aliens)}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Make an empty list for storing aliens
aliens = []

# Make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Use a for loop and if statement to change the color of aliens
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# # Expand the loop by adding elif block that turns yellow aliens into red
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['points'] = 10
#         alien['speed'] = 'medium'
#     elif alien['color'] == 'yellow':
#         alien['color'] = 'red'
#         alien['points'] = 15
#         alien['speed'] = 'fast'

# Show the first 5 Aliens
for alien in aliens[:5]:
    print(alien)









#
