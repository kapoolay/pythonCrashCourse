# Make a list containing a series of short text messages
# Pass the list to a function called 'show_messages()', which prints each text message

def show_messages(messagesList):
    for message in messagesList:
        print(f"\t{message}")

messages = ['hi', 'bye', 'ily']
show_messages(messages)