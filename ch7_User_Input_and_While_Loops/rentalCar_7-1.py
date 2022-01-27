# Write a program that asks the user what kind of rental car they would like
# Print a message about that car --> "Let's see if I can find you a {car}"

carPrompt = input("What kind of car would you like to rent? ")

# Lowecase the input value
carPrompt = carPrompt.lower()

# Conditional statement
if carPrompt == 'subaru':
	print(f"\nWe found you a Subaru!")
else:
	print(f"\nI\'m sorry, we don\'t have anymore in stock.")
