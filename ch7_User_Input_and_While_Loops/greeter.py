# Writing clear prompts
# Does not work in Atom

# # Prompt the user for their name
# name = input("Please enter your name: ")
# # Greet the user
# print(f"\nHi, {name}!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Putting the prompt on multiple lines
prompt = "If you tell us who you are, we can personalize the message you see."
prompt += "\nWhat is your name: "

name = input(prompt)
print(f"Hello, {name}! Good to see you again!")
