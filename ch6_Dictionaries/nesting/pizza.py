# List in a Dictionary
# Type of crust
# List of toppings

pizza = {
    'crust': 'thin',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Print the pizza order in a statement
print(f"You ordered a {pizza['crust']}-crust pizza\nwith the following toppings:")

# Print each topping in the list 'toppings' from the dictionary 'pizza'
for topping in pizza['toppings']:
    print(f"\t{topping}")
