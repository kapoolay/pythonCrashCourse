# Pass info to a function using 2 inputs
def greetUser(username, greeter):
    """Display a simple greeting."""
    print("\nThe purpose of this function is to print 'Hello!'")
    print(f"\tHello {username.title()}!")
    print(f"It's very nice to meet you {username.title()}! My name is {greeter.title()}!")

# Call the function
greetUser('alexia', 'kevin')