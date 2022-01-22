users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
    },
}

# Loop through the usernames and pull each piece of userInfo from each user

for username, userInfo in users.items():
    print(f"\nUsername: {username}")
    fullName = f"{userInfo['first']} {userInfo['last']}"
    location = f"{userInfo['location']}"
    print(f"\tFull Name: {fullName.title()}")
    print(f"\tLocation: {location.title()}")
