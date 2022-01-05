# Seeing the World: Think of at least five places in the world you'd like to visit

# Store the locations in a List
places = ['tokyo', 'rome', 'italy', 'paris', 'greece']
print('Original:')
print(places)


# Use sorted() to print your list in alpha order without modifying the actual List
print('\nTemporary Alpha Order:')
print(sorted(places))

print('\nOriginal Order:')
print(places)


# Print your list in reverse alpha order without changing the original Order
print('\nTemporary Reverse Alph Order:')
print(sorted(places,reverse=True))

print('\nOriginal Order:')
print(places)


# Use reverse() to change the order of your List
print('\nReverse of Original:')
places.reverse()
print(places)


# Use reverse() to change the order back to the OG
print('\nReverse back to Original:')
places.reverse()
print(places)


# Use sort() to change your list so it's stored in alpha Order
print('\nSort list by Alpha Order Permanently:')
places.sort()
print(places)

# Use sort() to change your list so it's stored in reverse alpha Order
print('\nSort list in Reverse Alpha Order Permanently:')
places.sort(reverse=True)
print(places)
