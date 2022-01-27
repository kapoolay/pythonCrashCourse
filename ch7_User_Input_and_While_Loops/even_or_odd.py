# Ask the user to input a number, determine if it's even/odd
number = input("Enter a number, and I'll tell you if it's even or odd: ")

# make sure the input variable is an integer
number = int(number)

if number % 2 == 0:
    print(f"\nThis number is even - {number}")
else:
    print(f"This is definitely odd! -- {number}")

# Even numbers are always divisible by two, so if the modulo of a number and 2 is zero (if number % 0 == 0), the number is even. Otherwise, it's odd

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Put the prompt on 2 lines
prompt = "I can tell you if your number is even or odd."
prompt += "\nGive me a number: "
# Have a user input a number
number = input(prompt)
# Change that string input to an integer
number = int(number)
# Write a conditional statement
if number % 2 == 0:
    print(f"\n{number} is even!")
else:
    print(f"\n{number} is odd!")
