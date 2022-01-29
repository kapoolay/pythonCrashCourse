# Stop the while loop in this program by calling 'break' as soon as the user enters 'quit'

prompt = "\nPlease enter the name of a city you have visited: "
prompt += "\n(Enter 'quit' when you are finished)  "

while True:
	city = input(prompt)

	if city == "quit":
		print("Thanks for playing!")
		break
	else:
		print(f"I'd love to go to {city.title()}.")

# A loop statement that starts with 'while True:' will run forever unless it reaches a break statement. The loop in this program continues asking the user to enter the names of cities they've been to until they enter 'quit'. When they enter 'quit', the 'break' statement runs, causing Python to exit the loop.

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished)  houston
# I'd love to go to Houston.
#
# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished)  austin
# I'd love to go to Austin.
#
# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished)  quit
# Thanks for playing!
