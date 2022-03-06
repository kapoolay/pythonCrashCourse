# Write a function called 'make_shirt()' that accepts a size and the text of a message that should be printed on the shirt
# The function should print a sentence summarizing the size of the shirt and the message printed on it
# Call the function

def make_shirt(shirtSize, printedMessage):
    print(f"\nI want a {shirtSize} sized shirt with the message \"{printedMessage}\" printed on it.")

# Once using positional arguments to make a shirt
make_shirt('medium', 'Hello World!')

# Another using keyword arguments
make_shirt(shirtSize='medium', printedMessage='Hello World 2!')