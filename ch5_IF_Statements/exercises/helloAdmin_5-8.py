# List of 5 or more usernames including 'admin'
# Loop through the list
# print a greeting to each user
# If the user is 'admin', print a special greeting: "Hello {admin}, would you like to see a status report?"
# Else print a generic greeting: "Hello {user}, welcome back!"

usernames = ['james', 'kevin', 'ale', 'eddy', 'admin', 'kate', 'leslie']

for i in usernames:
    if i == 'admin':
        print(f'Hello {i.title()}, would you like to see a status report?')
    else:
        print(f'Hello {i.title()}, welcome back!')
