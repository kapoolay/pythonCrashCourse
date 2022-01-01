# If you could invite anyone, living or deceased, to dinner, who would you invite?

guest_list = ['Kobe', 'JCole', 'Van Gogh']

greet = 'Hi'
invite = ', would you like to have dinner with me?'

print(f'{greet} {guest_list[0]}{invite}')
print(f'{greet} {guest_list[1]}{invite}')
print(f'{greet} {guest_list[2]}{invite}')

# • Modify your list, replacing the name of the guest who can't make it with the name of the new person you are inviting
removed_guest = guest_list.pop()
guest_list.append('Ross')

# • Starting with 3-4, add a print() call at the end of your program stating the name of the guest who can't make it
print(f'\nUnfortunately, {removed_guest} is unable to make it. Luckily {guest_list[2]} can make it!')

# • Print a second set of invitation messages, one for each person who is still in your List
print(f'\n{greet} {guest_list[0]}{invite}')
print(f'{greet} {guest_list[1]}{invite}')
print(f'{greet} {guest_list[2]}{invite}')
