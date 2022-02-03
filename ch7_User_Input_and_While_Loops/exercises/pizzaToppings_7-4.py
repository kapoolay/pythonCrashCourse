# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value
# As they enter each topping, print a message saying you'll add that topping to their pizza

prompt = "\nWhat toppings do you want on your pizza?"
prompt += "\nEnter one at a time."
prompt += "\n(Once done, enter 'finished'): "

# TEST
# print(prompt)
# toppings = input(prompt)
# print(toppings)


while True:
    toppings = input(prompt)

    if toppings == "finished":
        print("Your pizza is ready")
        break
    else:
        print(f"{toppings.title()} has been added!")


# # Solution
# prompt = "\nWhat topping would you like on your pizza?"
# prompt += "\nEnter 'quit' when you are finished: "
#
# while True:
#     topping = input(prompt)
#     if topping != 'quit':
#         print(f"  I'll add {topping} to your pizza.")
#     else:
#         break

