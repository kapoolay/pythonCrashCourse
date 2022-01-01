# If you could invite anyone, living or deceased, to dinner, who would you invite?


guest_list = ['Kobe', 'JCole', 'Van Gogh']

greet = 'Hi'
invite = ', would you like to have dinner with me?'

# print(f'{greet} {guest_list[0]}{invite}')
# print(f'{greet} {guest_list[1]}{invite}')
# print(f'{greet} {guest_list[2]}{invite}\n')

guest_list.insert(0,'Stanley')
guest_list.insert(3,'Ross')
guest_list.append('Phoebe')

print(guest_list)

# • Starting with 3-6, add a new line that prints a message saying that you can invite only two people for dinner
print('\nUnfortunately, I can only invite 2 people for dinner.\n')

# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you're sorry you can't invite them to dinner.
print(guest_list)
removed_guest = guest_list.pop()
print(f'I\'m sorry we can\'t have dinner, {removed_guest}\n')
print(guest_list)

removed_guest = guest_list.pop()
print(f'I\'m sorry we can\'t have dinner, {removed_guest}\n')
print(guest_list)

removed_guest = guest_list.pop()
print(f'I\'m sorry we can\'t have dinner, {removed_guest}\n')
print(guest_list)

removed_guest = guest_list.pop()
print(f'I\'m sorry we can\'t have dinner, {removed_guest}')
print(guest_list)


# • Print a message to each of the two people still on your list, letting them know they're still invited.
print(f'\nYou are still invited {guest_list[0]}!')
print(f'You are still invited {guest_list[1]}!\n')

# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.
print(guest_list)
del guest_list[0]
print(guest_list)
del guest_list[0]
print(guest_list)

#TESTING


# print(f'\n{greet} {guest_list[0]}{invite}')
# print(f'{greet} {guest_list[1]}{invite}')
# print(f'{greet} {guest_list[2]}{invite}')
# print(f'{greet} {guest_list[3]}{invite}')
# print(f'{greet} {guest_list[4]}{invite}')
