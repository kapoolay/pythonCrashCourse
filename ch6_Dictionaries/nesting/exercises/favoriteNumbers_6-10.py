# Modify 6-2 program so each person can have more than one favorite number
# Print eacher person's name along with their favorite numbers
favoriteNumbers = {
    'kevin': [10, 32],
    'ale': [6],
    'eddy': [6, 90, 9],
    'kobe': [8, 33, 24],
    'mj': [23, 45],
    'test': [],
}

# Print each person's name and their favorite number
for name, numbers in favoriteNumbers.items():
    if len(numbers) == 1:
        print(f"\n{name.title()}\'s favorite number is:")
        for number in numbers:
            print(f"\t{number}")
    elif len(numbers) > 1:
        print(f"\n{name.title()}\'s favorite numbers are:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f'\nTHIS IS A TEST')
