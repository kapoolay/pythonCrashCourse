# Start with a copy of 8-9
# Write a function called 'send_messages()' that prints each text message and moves each message to a new list called 'sent_messages[]' as it's printed.
def send_messages(messages):
    while messages:
        current_Message = messages.pop()
        print(f"Message Sent: \'{current_Message}\'")
        sent_messages.append(current_Message)

# Function to print unsent messages
def print_unsent_messages_list(messagesList):
    print("\nUnsent Messages:")
    for message in messagesList:
        print(f"{message}")


# Function to print sent messages
def print_sent_messages(messagesList):
    print("\nSent Messages:")
    for message in messagesList:
        print(f"\t{message}")

# After calling the function, print both of your lists to make sure the messages were moved correctly.
messages = ['hi', 'bye', 'ily']
sent_messages = []

send_messages(messages)
print_unsent_messages_list(messages)
print_sent_messages(sent_messages)