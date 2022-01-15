# Add an if test to helloAdmin.py
usernames = ['james', 'kevin', 'ale', 'eddy', 'admin', 'kate', 'leslie']
# If the list is empty print "We need to find some users!"
usernames =[]

if usernames:
    for i in usernames:
        if i == 'admin':
            print(f'Hello {i.title()}, would you like to see a status report?')
        else:
            print(f'Hello {i.title()}, welcome back!')
else:
    print('We need more users!')
