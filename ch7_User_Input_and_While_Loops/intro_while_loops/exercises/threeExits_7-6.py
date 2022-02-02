# Write 3 different versions of either exercise 7-4 or 7-5 that do each of the following

# 7-4
# A theatre charges different ticket prices depending on person's age
# Write a loop in which you ask a user their age
# Then tell them how much their ticket costs
## Conditionals
# age < 3 --> free
# age <= 12 --> $10
# age > 12 --> $15

prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' to end): "

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Use a conditional test in the 'while' statement to stop the loop
# age = input(prompt)
# age = int(age)
#
# while age < 100:
#     if age == "quit":
#         break
#     elif age < 3:
#         print("Your ticket is free, enjoy!")
#     elif age <= 12:
#         print("Your ticket cost is $10.")
#     elif age > 12:
#         print("Your ticket cost is $15.")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Use a variable to control how long the loop runs
#
# active = True
# while active:
#     age = input(prompt)
#
#     if age == "quit":
#         active = False
#     else:
#         # Change input into number
#         age = int(age)
#         if age < 3:
#             print("Your ticket is free, enjoy!")
#         elif age <= 12:
#             print("Your ticket cost is $10.")
#         elif age > 12:
#             print("Your ticket cost is $15.")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Use a 'break' statement to exit the loop when the user enters a 'quit' value
while True:
    age = input(prompt)
    if age != "quit":
        # Change input into number
        age = int(age)
        if age < 3:
            print("Your ticket is free, enjoy!")
        elif age <= 12:
            print("Your ticket cost is $10.")
        elif age > 12:
            print("Your ticket cost is $15.")
    else:
        print("Enjoy the movie!")
        break