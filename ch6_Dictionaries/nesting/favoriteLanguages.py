favoriteLanguages = {
    'kevin': ['python', 'js'],
    'john': ['java'],
    'chris': ['c', 'java'],
    'mike': ['js'],
    'ale': ['python', 'css'],
    'kim': ['html'],
}

# Loop thru each person's favorite languages
# Capitalize what is needed
# If they have more than 1 language, make sure the statement is plural, vice versa
for name, languages in favoriteLanguages.items():
    if len(languages) > 1:
        print(f"{name.title()}\'s favorite languages are:")
    else:
        print(f"{name.title()}\'s favorite language is:")
    # for statement for the languages
    for language in languages:
        if language == 'js' or language == 'html' or language == 'css':
            print(f"\t{language.upper()}")
        else:
            print(f"\t{language.title()}")








#
