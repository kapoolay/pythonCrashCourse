# Using one of the programs in this chapter, add several lines to the end of the program with the following:

pizzas = ['pepperoni', 'pineapple', 'ham', 'cheese', 'olives', 'vegan']

# Print the message 'The first three items in the list are:'.
# Then use a slice to print the first three items from that program's list
print('\nThe first three items in the list are:')
for pizza in pizzas[:3]:
    print(pizza)

# Print the message 'Three items from the middle of the list are:'.
# Use a slice to print three items from the middle of the list.
print('\nThree items from the middle of the list are:')
for pizza in pizzas[1:4]:
    print(pizza)

# Print the message 'The last three items in the list are:'.
# Use a slice to print the last three items in the list.
print('\nThe last three items in the list are:')
for pizza in pizzas[-3:]:
    print(pizza)
