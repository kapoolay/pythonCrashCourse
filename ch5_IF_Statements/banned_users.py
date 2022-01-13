# Checking whether a value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()} is not a banned user\n')
else:
    print('She is banned\n')

# Add 'marie' to the list banned_users
# Print out a message saying she is banned
banned_users.append('marie')
#testing to see if user was added
print('Marie has been banned')
print(banned_users)

if user not in banned_users:
    print(f'{user.title()} is not a banned user')
else:
    print(f'{user.title()} is banned')
