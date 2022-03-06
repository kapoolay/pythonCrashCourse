# Modify 'make_shirt()' so that the shirts are large by default with a message that reads 'I love Python'

def make_shirt(shirtSize='large', printedMessage='I love Python'):
    print(f"\nI want a {shirtSize} sized shirt with the message \"{printedMessage}\" printed on it.")

# Large shirt call/default message
make_shirt()

# Medium shirt call with default message
make_shirt(shirtSize='medium')

# A shirt of any size with a different message
make_shirt(shirtSize='XXL', printedMessage='Hello World!')