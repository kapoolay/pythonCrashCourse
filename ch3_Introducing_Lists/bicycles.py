bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print('List:')
print(bicycles)

print('\nExtract the first item on the list:')
print(bicycles[0].title())

print('\nExtract the 2nd and 4th item on the list:')
print(bicycles[1].title())
print(bicycles[3].title())

print('\nExtract the last element in the list')
print(bicycles[-1].title())

print('\nExtract the 2nd and 3rd to last element from the list')
print(bicycles[-2].title())
print(bicycles[-3].title())

print('\nMessage using f-strings')
message = f'My dream bicycle is a {bicycles[3].title()}!'
print(message)
