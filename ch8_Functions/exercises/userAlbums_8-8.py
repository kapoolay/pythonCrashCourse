# Start with 8-7 program
# Write a 'while loop' that allows users to enter an album's artist and title
# Once you have that info, call 'make_album()' with the user's input and print the dictionary that's created
# Be sure to include a quit value in the while loop

def make_album(artistName, albumTitle):
    artistDict = {'name': artistName, 'album': albumTitle}
    return artistDict

# artist1 = make_album('jcole', 'forest hills')
# print(artist1)

while True:
    print(f"\n==== Please enter an artist and their album. ====")
    print(f"(Enter 'q' at anytime to quit)")

    namePrompt = input(f"\nArtist's name: ")
    if namePrompt == 'q':
        print("Thanks for playing!")
        break

    albumPrompt = input(f"Album name: ")
    if albumPrompt == 'q':
        print("Thanks for playing!")
        break

    artistInfo = make_album(namePrompt, albumPrompt)
    print(artistInfo)