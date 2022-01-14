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

requested_topping = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_topping:
    print('Adding mushrooms!')
if 'pepperoni' in requested_topping:
    print('Adding pepperoni')
if 'extra cheese' in requested_topping:
    print('Adding extra cheese')

print('\nYour order is ready!')
