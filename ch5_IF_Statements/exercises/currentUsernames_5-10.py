# List of 5 or more users in "current_users"
# List 5 users in "new_users" --> 2 of these users being in "current_users"
# Loop through "new_users" to see if a new username has already been used
# If it has been used, print "You will need a new username"
# If it has NOT been used, print "Username is available"
# Comparison is case insensitive
# If "John" has been used, "JOHN" is not accepted

current_users = ['james', 'KEVIN', 'aLe', 'eddy', 'beth', 'kate', 'leslie']
new_users = ['Kevin', 'Delia', 'Chris', 'Mia', 'Ale']

# LIST = [EXPRESSION ForLoop]
current_users_lower = [i.lower() for i in current_users]
new_users_lower = [i.lower() for i in new_users]

# For every i in new_users
# If i is in current users
# Print "You will need a new username"
# Else print "Username is available"
# Case is insensitive
for i in new_users_lower:
    if i in current_users_lower:
        print('You will need a new username')
    else:
        print('Username is available')
