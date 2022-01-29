prompt = ("\nTell me something, and I will repeat it back to you - enter with quotes")

prompt += ("\nEnter 'quit' to stop the game: ")

# Flag
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print("The game is over, thanks for playing!")
    else:
        print(message)
