# print('Modifying elements in a List')
#
# motorcycles = ['honda', 'yamaha', 'suzuki',]
# print(motorcycles)
#
# motorcycles[0] = 'ducati'
# print(motorcycles)
#
# #~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# print('\nAdding elements in a List')
#
# motorcycles = ['honda', 'yamaha', 'suzuki',]
#
# motorcycles.append('ducati')
# print(motorcycles)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~

# print('Build an Empty List:')
#
# motorcycles = []
#
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
#
# print(motorcycles)

# #~~~~~~~~~~~~~~~~~~~~~~~~~~

# print('Insert Elements Into a List:'.title())
#
# motorcycles = ['honda', 'yamaha', 'suzuki',]
# print(motorcycles)
#
# print('\nUsing the insert(place,value) Method')
# motorcycles.insert(0,'ducati')
#
# print(motorcycles)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# motorcycles = ['honda', 'yamaha', 'suzuki',]
# print(motorcycles)
#
# print('\nRemoving an Item Using the del Statement:')
# del motorcycles[1]
# print(motorcycles)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# motorcycles = ['honda', 'yamaha', 'suzuki',]
# print(motorcycles)
#
# print('\nRemoving an Item using the pop() Method:')
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# motorcycles = ['honda', 'yamaha', 'suzuki',]
#
# last_owned = motorcycles.pop()
# print(f'The last motorcycle I owned was a {last_owned.title()}.')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# print('Popping Items from any Position in a List:\n')
#
# motorcycles = ['honda', 'yamaha', 'suzuki',]
#
# first_owned = motorcycles.pop(0)
# print(f'The first motorcycle I owned was a {first_owned.title()}.')
# print(motorcycles)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

print('Removing an Item by Value:\n')

motorcycles = ['honda', 'yamaha', 'suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive} is too expensive for me!')
