# If you could invite anyone, living or deceased, to dinner, who would you invite?

guest_list = ['Kobe', 'JCole', 'Van Gogh']

greet = 'Hi'
invite = ', would you like to have dinner with me?'

print(f'{greet} {guest_list[0]}{invite}')
print(f'{greet} {guest_list[1]}{invite}')
print(f'{greet} {guest_list[2]}{invite}\n')

# • Starting with 3-4, add a print() call at the end of your program informing people that you found a bigger dinner table.
print(f'Hi everyone! I was able to find a bigger table!')
# • Use insert() to add one new guest to the beginning of your List
guest_list.insert(0,'Stanley')
# • Use insert() to add one new guest to the middle of your List
guest_list.insert(3,'Ross')
# • Use append() to add one new guest to the end of your List
guest_list.append('Phoebe')

print(guest_list)

# • Print a new set of invitation messages, one for each person in your List
print(f'\n{greet} {guest_list[0]}{invite}')
print(f'{greet} {guest_list[1]}{invite}')
print(f'{greet} {guest_list[2]}{invite}')
print(f'{greet} {guest_list[3]}{invite}')
print(f'{greet} {guest_list[4]}{invite}')
