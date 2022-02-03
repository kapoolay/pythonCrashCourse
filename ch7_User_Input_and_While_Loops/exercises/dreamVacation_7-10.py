# Write a program that polls users about their dream vacation
# "If you could visit one place in the world, where would that be?"
# empty dictionary
# vacationPoll = {name: place}
vacationPoll = {}
# Set a flag for the loop to continue if it's still 'True'
# Loop thru name/place prompts (2 inputs)
# Add each key(name): value(place) to the empty dictionary(vacationPoll)
# Input 3: See if anyone else wants to take the poll (y/n)
# If 'n', set the flag to 'False'
pollActive = True

while pollActive:
    name = input("\nWhat is your name? ")
    place = input("\nIf you could visit one place in the world, where would that be? ")
    # print(name)
    # print(place)
    vacationPoll[name] = place
    # print(vacationPoll)
    repeat = input(f"Is there anyone else that needs to take this poll? (y/n) ")
    if repeat == 'n':
        pollActive = False

# Print the results
print(f"\n=== Results ===")
for name, place in vacationPoll.items():
    print(f"{name.title()}: {place.title()}")