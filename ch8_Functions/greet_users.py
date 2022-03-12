# Passing a List thru a Function

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        message = f"\n\tHello, {name.title()}!"
        print(message)

usernames = ['kevin', 'alexia', 'eddy']

greet_users(usernames)

