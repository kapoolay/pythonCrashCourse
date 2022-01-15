# store a requested topping in a variable
# print message if person did not order anchovies

# requested_topping = 'Mushroom'

# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')
# # If these 2 values do not match, execute the code following the IF statement
# # If the values do match, do not run the code
#
# # For fun
# if requested_topping.lower() == 'mushrooms':
#     print(f'Gimme my {requested_topping} pizza!')


# Testing multiple conditions

# requested_topping = ['mushrooms', 'extra cheese']
#
# if 'mushrooms' in requested_topping:
#     print('Adding mushrooms!')
# if 'pepperoni' in requested_topping:
#     print('Adding pepperoni')
# if 'extra cheese' in requested_topping:
#     print('Adding extra cheese')
#
# print('\nYour order is ready!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# # Checking for special items
#
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'bacon']
#
# # Simple for loop
# # for i in requested_toppings:
# #     print(f'Adding {i}')
#
# # What if you run out of green peppers
# for i in requested_toppings:
#     if i == 'green peppers':
#         print('Sorry we ran out of green peppers')
#     else:
#         print(f'Adding {i}')
#
# print('\nYour pizza is ready!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Checking if a List is not empty

requested_toppings = []
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', 'bacon']

if requested_toppings:
    for i in requested_toppings:
        print(f'Adding {i}')
    print('\nYour pizza is ready!')
else:
    print('Are you just wanting a cheese pizza?')

# When the name of a list is used in an if statement, Python returns 'True' if the list contains at least one item; an empty list evaluates to 'False'
