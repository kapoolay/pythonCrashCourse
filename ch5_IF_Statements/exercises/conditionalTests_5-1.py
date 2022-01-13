# Write a series of conditional Tests
# Print a statement describing each test and your prediction for the results of each test

# car = 'subaru'
#
# print('Is car == "subaru"? I predict true')
# print(car == 'subaru')
#
# print('\nIs car == "audi"? I predict false')
# print(car == 'audi')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

kev = 30
ale = 27

print('\nIs Kev older than Ale? True')
print(kev >= ale)

print('\nIs Ale older than Kev? False')
print(ale >= kev)

print('\nKev and Ale the same age? False')
print(kev == ale)

print('\n')
if kev >= 30 and ale >= 30:
    print('We\'re both old!')
else:
    print('You\'re old Kev!')

print('\n')
if kev >= 30 or ale >= 30:
    print('We\'re both old!')
else:
    print('You\'re old Kev!')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# banned_users = ['Andrew', 'carolina', 'david']
# user = 'Kev'
#
# print('\nIs the "user" called "kev"? True')
# print(user.lower() == 'kev')
#
# print(f'\nIs the "user" called "{banned_users[0]}"? False')
# print(user == banned_users[0].lower())
# print(banned_users[0].lower())
#
# print('\nKev is a banned user? False')
# print(user in banned_users)
#
# banned_users.append('kev')
#
# print('\nKev is a banned user? True')
# print(user in banned_users)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# toppings = ['pepperoni', 'ham', 'pineapple']
#
# print('\nOnions a topping? False')
# print('onions' in toppings)
#
# # Add bacon
# toppings.insert(0, 'Bacon')
# print('\nAdded bacon to toppings:')
# print(toppings)
#
# # false condition, lower case bacon causes false result
# print('\nIs bacon a topping? false')
# print('bacon' in toppings)
#
# # True bacon condition
# bacon = toppings[0]
# print(bacon)
# print('\nIs "Bacon" a topping? True')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
