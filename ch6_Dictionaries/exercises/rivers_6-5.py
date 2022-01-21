# Dictionary containing 3 major rivers (key) and their countries (value)

rivers = {
    'mississippi': 'usa',
    'nile': 'egypt',
    'amazon': 'brazil'
}

# Loop to print a sentence about each river
## The {river} runs through {country}
for river, country in rivers.items():
    if country == 'usa':
        print(f"The {river.title()} runs thru {country.upper()}.")
    else:
        print(f"\nThe {river.title()} runs thru {country.title()}.")

# Loop to print the name of each river (key) in the dictionary
print("\nAll Rivers:")
for river in rivers.keys():
    print(river.title())

# Loop to print each country in the dictionary (value)
print("\nAll Countries:")
for country in rivers.values():
    if country == 'usa':
        print(country.upper())
    else:
        print(country.title())
