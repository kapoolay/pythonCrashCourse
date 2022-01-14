# List 3 favorite fruits using 'favorite_fruits'
# Write 5 if statements
# Each statement checks whether a certain kind of fruit is in your list
# If the fruit is in your list print 'I really like {favorite_fruits}!'

favorite_fruits = ['Mangos', 'Oranges', 'Blueberries']

# Lowercase the fruits list using list comprehension
# LIST = [EXPRESSION ForLoop]
favorite_fruits_lower = [i.lower() for i in favorite_fruits]
# # test to see if lower case conversion worked
# print(favorite_fruits_lower)

if 'mangos' in favorite_fruits_lower:
    print('I really like mangos!')

if 'strawberries' in favorite_fruits_lower:
    print('I really like strawberries!')

if 'oranges' in favorite_fruits_lower:
    print('I really like oranges!')

if 'apples' in favorite_fruits_lower:
    print('I really like apples!')

if 'blueberries' in favorite_fruits_lower:
    print('I really like blueberries!')
