# make_album() function
# Builds a dictionary describing a music album
# Takes parameters for artist name and album title
# Use function to make three dictionaries representing different albums
# Print each return value to show that the dictionaries are storing the album info correctly

def make_album(artistName, albumTitle):
    albumDict = {'name': artistName, 'album': albumTitle}
    return albumDict

artist1 = make_album('kanye west', 'college dropout')
print(artist1)

artist2 = make_album('jcole', '4 your eyez only')
print(artist2)

artist3 = make_album('chris stapleton', 'traveller')
print(artist3)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use 'None' to add an optional parameter to 'make_album()' that allows you to store the number of songs on the album
# If the calling line includes a value for the number of songs, add that value to the album's dictionary
# Make at least one new function call that includes the number of songs on an album

def make_album2(artistName, albumTitle, totalSongs=None):
    albumDict = {'name': artistName, 'album': albumTitle}
    if totalSongs:
        albumDict['songs'] = totalSongs
    return albumDict

artist4 = make_album2('jcole', 'born sinner', 16)
print(f"\n{artist4}")

artist3 = make_album2('chris stapleton', 'traveller')
print(artist3)