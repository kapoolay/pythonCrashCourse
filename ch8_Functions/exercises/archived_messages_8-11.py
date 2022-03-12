# Start with exercise 8-10

# Function that prints each text message and moves each message to a new list called 'sent_messages[]' as it's printed.
def send_messages(messages):
    while messages:
        current_Message = messages.pop()
        print(f"Message Sent: \'{current_Message}\'")
        sent_messages.append(current_Message)

# Function to print unsent messages
def print_unsent_messages_list(messagesList):
    print("\nUnsent Messages:")
    for message in messagesList:
        print(f"\t{message}")

# Function to print sent messages
def print_sent_messages(messagesList):
    print("\nSent Messages:")
    for message in messagesList:
        print(f"\t{message}")

messages = ['hi', 'bye', 'ily']
sent_messages = []

# Call the function 'send_messages()' with a copy of the list of messages
send_messages(messages[:])

# After calling the function, print both of your lists to show that the original list has retained its messages
print_unsent_messages_list(messages)
print_sent_messages(sent_messages)
# print(f"Unsent Messages:\n\t{messages}")
# print(f"Sent Messages:\n\t{sent_messages}")