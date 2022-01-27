# Write a program that ask the user how many people are in their dinner group
headCount = input("How many people are in your group? ")

# Conditionals
# If the answer is > 8, print a message saying they'll have to wait for a table
# Otherwise, their table is ready
# Make sure the inputted value is an integer
headCount = int(headCount)

if headCount > 8:
	print("\tYou will have to wait for a table")
else:
	print("\tYour table is ready!")
