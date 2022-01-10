# Copying a list --> PG 98
# To copy a list, you can make a slice that includes the entire original list by omitting the first and second index

# Make a list of the foods we like
my_foods = ['pizza','falafel', 'carrot cake']
# Make a new list copy my_foods by using [:]
# If you copy without the slice,[:], this syntax tells Python to associate the new variable friend_foods with the list that is already associated with my_foods, resulting in the same exact list
# Likewise 'onios' will appear in both lists, even though it appears to be added only to friend_foods
friend_foods = my_foods[:]
my_foods.append('ice cream')
friend_foods.append('onions')


print('My favorite foods are:')
print(my_foods)

print('\nMy friend\'s favorite foods are:')
print(friend_foods)
