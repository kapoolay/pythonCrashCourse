magicians = ['alice', 'david', 'carolina']

# for magician in magicians:
#     print(magician)

# This can be read as 'For every magician in the list of magicians, print the magician's name'



# Tell each magician in the list they performed great
# Tell them we're looking forward to their next trip

for magician in magicians:
    print(f'{magician.title()}, that was great!')
    print(f'I am looking forward to your next trip, {magician.title()}!\n')
