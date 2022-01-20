# Store ppl's favorite number
# 5 names
# Favorite number for each person

favoriteNumbers = {
    'kevin': 10,
    'ale': 6,
    'eddy': 6,
    'kobe': 8,
    'mj': 23,
}

# Print each person's name and their favorite number
for x, y in favoriteNumbers.items():
    print(f"{x.title()}\'s favorite number is {y}")
