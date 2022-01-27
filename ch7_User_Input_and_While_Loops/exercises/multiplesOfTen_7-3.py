# Ask the user for a number
# Report whether the number is a multiple of 10 or not

prompt = "I can tell you if your number is a multiple of ten"
prompt += "\nGive me a number: "

# Input call
number = input(prompt)

# Make sure the inputted value is an integer
number = int(number)

# Conditional
if number % 10 == 0:
	print(f"\t{number} is a multiple of 10!")
else:
	print(f"\t{number} is not a multiple of 10!")
