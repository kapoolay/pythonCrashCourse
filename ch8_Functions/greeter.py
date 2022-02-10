# # Define a function
# def greetUser():
#     """Display a simple greeting."""
#     print("The purpose of this function is to print 'Hello!'")
#     print("\n\tHello!")
#
# # Call the function
# greetUser()
#
# # "def" is the keyword to inform Python that you're defining a function
# # Docstrings are enclosed in triple quotes, which describes what the function does

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Pass info to a function
def greetUser(username, greeter):
    """Display a simple greeting."""
    print("\nThe purpose of this function is to print 'Hello!'")
    print(f"\tHello {username.title()}!")
    print(f"My name is {greeter.title()}! Nice to meet you!")


# Call the function
# greetUser("kevin")
# greetUser("alexia")
greetUser("kevin", "eddy")