user_o = {
    'username': 'efermi',
    'fist': 'enrico',
    'last': 'fermi',
}

# # Username
# print(user_o['username'])

# # Loop thru the dictionary for all key-value pairs
# for k, v in user_o.items():
#     print(f"\nKey: {k.title()}")
#     print(f"Value: {v.title()}")

# Loop through
favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
    }

# # Print key-values
# for name, language in favoriteLanguages.items():
#     print(f"\n{name.title()}\'s language is {language.title()}")

# # Print keys only
# for name in favoriteLanguages.keys():
#     print(f"\n{name.title()}")

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





#
