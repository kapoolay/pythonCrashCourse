# Make the parrot.py program into a while loop
# Use the input "quit" as the quit value

prompt = ("\nTell me something, and I will repeat it back to you - enter with quotes")

prompt += ("\nEnter 'quit' to stop the game: ")

message = ""

while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

 # First time thru the loop, 'message' is just an emptry string, so Python enters the loop At 'message = input(prompt)', Python displays the prompt and waits for the user to enter their input. Whatever they enter is assigned to 'message' and printed; then, Python reevaluates the condition in the 'while' statement. As long as the user has not entered the word 'quit', the prompt is displayed again and Python waits for more input.

 # When the user finally enters 'quit', Python stops executing the 'while' loop and the program ends

# Program works well, except that it prints the word 'quit' as if it were an actual message. A simple 'if' test fixes this
