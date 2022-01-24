# Make a dictionary called "favorite_places"
# 3 names to use as keys in the dictionary
# 1-3 favorite places for each person --> List in a Dictionary?
favoritePlaces = {
    'kevin': ['los angeles', 'seattle', 'hawaii'],
    'alexia': ['paris', 'chicago', 'rome'],
    'eddy': ['new york'],
    'test':[],
}

# Loop thru each person and print each person's name and favorite places

for person, places in favoritePlaces.items():
    if len(places) > 1:
        print(f"{person.title()}\'s favorite places are:")
        for place in places:
            print(f"\t{place.title()}")
    elif len(places) == 1:
        print(f"{person.title()}\'s favorite place is:")
        for place in places:
            print(f"\t{place.title()}")
    else:
        print('--no values--')
    print('\n')
