# A theatre charges different ticket prices depending on person's age
# Write a loop in which you ask a user their age
# Then tell them how much their ticket costs

## Conditionals
# age < 3 --> free
# age <= 12 --> $10
# age > 12 --> $15

prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' to end): "
# print(prompt)

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

