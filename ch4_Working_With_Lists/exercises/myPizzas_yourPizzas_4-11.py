# Start with exercise 4-1
# Make a copy of the list of pizzas and call it friend_pizzas
pizzas = ['pepperoni', 'pineapple', 'ham', 'cheese']
friend_pizzas = pizzas[:]

# Add a new pizza to the original list
pizzas.append('bbq')

# Add a different pizza to the list friend_pizzas
friend_pizzas.append('olives')

# Print the message 'My favorite pizzas are:'
# Use a for loop to print the first list pizzas
print('My favorite pizzas are:')
for pizza in pizzas:
    print(pizza)

# Print the message 'My friend\'s favorite pizzas are:'
# Use a for loop to print the list friend_pizzas
print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(pizza)
