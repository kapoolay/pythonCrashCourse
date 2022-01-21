favoriteLanguages = {
    'kevin': 'python',
    'john': 'java',
    'chris': 'c',
    'mike': 'js',
    'ale': 'python',
    'kim': 'html',
}

# Make a list of people who should take the poll
# Include names in the dictionary who have taken the poll
# Include names NOT in the dictionary

pollTakers = ['kevin', 'jon', 'pam', 'stanley', 'mike', 'sara', 'matt', 'chris']

# Loop through the list of people who should take the poll
# If they took the poll --> "Thank you for taking the poll"
# If they haven't taken the poll --> "Do you have a minute to take this poll?"

# for every name in "pollTakers"
# if name is in "favoriteLanguages", --> "Thank you for taking the poll"
# else --> "Do you have a minute to take this poll?"
for name in pollTakers:
    if name in favoriteLanguages.keys():
        print(f"\nThank you for taking the poll {name.title()}!\n")
    else:
        print(f"Hi {name.title()}! Do you have a minute to take this poll?!")
