# Think of five simple foods
# Store them in a tuple using ()
foods = ('chips', 'sandwiches', 'fries', 'burgers', 'water')
print('Old Menu:')
# Use a for loop to print each food
for food in foods:
    print(food)

# # Modify one of the items, and make sure that Python rejects the change
# foods[0] = 'chips'

# Replace two of the items with different foods
# Add a line that rewrites the tuple
foods = ('chips', 'sandwiches', 'sweet potatoes', 'burgers', 'soda')
print('\nNew Menu:')
# Use a for loop to print each of the items
for food in foods:
    print(food)
