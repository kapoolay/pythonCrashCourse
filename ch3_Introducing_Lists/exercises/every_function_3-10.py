# Think of something you can store in a list.
# Write a program that creates a list containing these items
# Use each function introduced in this chapter at least once

groceries = ['potatoes', 'tortilla', 'ground beef', 'tomatoes', 'cilantro', 'onions', 'powdered sugar', 'grapes', 'blueberries']


# Print a sentence accessing two of the elements
# print(f'I always buy {groceries[7]} and {groceries[-1]} when I shop for groceries!')

# Print sentence using .title()
# print(f'{groceries[5].title()} make me cry!')

# Print sentence accessing the last item on the List
# print(f'Mia loves to eat {groceries[-1]}!')

# Pull the first thing on the list and compose a message using that value
# print(f'{groceries[0].title()} make really great fries!')

# Modify Elements in the list - Change the first value of the item to 'sweet potatoes'
# groceries[0] = 'sweet potatoes'
# print(groceries)


groceries = ['potatoes', 'tortilla', 'ground beef', 'tomatoes', 'cilantro', 'onions', 'powdered sugar', 'grapes', 'blueberries']


# Add 'apples' end of the List
# groceries.append('apples')
# print(groceries)

# Remove 'apples' from the List, but save it in a variable
# popped_groceries = groceries.pop()
# print(f'The last thing on the list was {popped_groceries}.')
# print(groceries)

# Insert 'oranges' to the beginning of the List
# groceries.insert(0,'oranges')
# print(groceries)
#
# # Remove 'oranges' from the List
# groceries.pop(0)
# print(groceries)

# Add 'oranges' to the end of the List, print, then remove it by the value 'orange'
# groceries.append('oranges')
### OR
# print(len(groceries))
# groceries.insert(10,'oranges')
#
# print(groceries)
# groceries.remove('oranges')
# print(groceries)


groceries = ['potatoes', 'tortilla', 'ground beef', 'tomatoes', 'cilantro', 'onions', 'powdered sugar', 'grapes', 'blueberries']

# Sort method temporarily by Alpha
# print(sorted(groceries))
# print(groceries)

# # Sort method temporarily by reverse Alpha
# ## Temporarily Reversed Alpha
# print(sorted(groceries,reverse=True))
# ## OG Order
# print(groceries)

# Permanently sort by alpha
groceries.sort()
print(groceries)

# Print List in Reverse Order
groceries.reverse()
print(groceries)

# Find the length of the List
length = len(groceries)
print(f'I need to buy {length} things from HEB!')
