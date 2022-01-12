# store a requested topping in a variable
# print message if person did not order anchovies

requested_topping = 'Mushroom'

if requested_topping != 'anchovies':
    print('Hold the anchovies!')
# If these 2 values do not match, execute the code following the IF statement
# If the values do match, do not run the code

# For fun
if requested_topping.lower() == 'mushrooms':
    print(f'Gimme my {requested_topping} pizza!')
