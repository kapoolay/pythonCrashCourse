# Loop through
favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
    }

# Print key-values
for name, language in favoriteLanguages.items():
    print(f"\n{name.title()}\'s language is {language.title()}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Print keys only
for name in favoriteLanguages.keys():
    print(f"\n{name.title()}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Only print messages for kevin and ale
friends = ['kevin', 'ale']

for name in favoriteLanguages.keys():
    print(f"\nHi {name.title()}!")
    if name in friends:
        # language = favoriteLanguages[name].title()
        print(f"{name.title()}, I see you love {favoriteLanguages[name].title()}")
# # for every name in favoriteLanguages
#     # Say Hi
#     # If that name is in the list 'friends',
#     # Say 'I see you love <language>'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Did kobe take the poll?

if "kobe" not in favoriteLanguages.keys():
    print("Kobe, take the poll!")

# keys() method isn't just for looping: it actually returns a list of all the keys, and this line simply checks if "kobe" is in this list.
# Bc he's not, a message is printed inviting him to take the poll

# Returns all keys in the dictionary
print(favoriteLanguages.keys())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Loop thru the keys in a particular order
# Use sorted() to get a copy of the keys in order
favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
}

for name in sorted(favoriteLanguages.keys()):
    print(f"{name.title()}")
    # print(f"\n{name.title()}, thank you sharing your favorite language!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
}

# Print value for each pair using value()

for language in favoriteLanguages.values():
    if language == "html":
        print(language.upper())
    else:
        print(language.title())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
}

# Pull values without repeats
# Sorted in alpha without repition
print("Languages Mentioned:")
for language in sorted(set(favoriteLanguages.values())):
    if language == 'html' or language == 'js':
        print(f"\t{language.upper()}")
    else:
        print(f"\t{language.title()}")

languages = {'python', 'ruby', 'python', 'c'}
print(languages)



#
