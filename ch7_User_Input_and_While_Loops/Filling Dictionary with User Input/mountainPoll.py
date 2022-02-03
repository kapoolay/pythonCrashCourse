# Polling program

# Create empty dictionary
# Set a flag to indicate that the polling is active
# Create a 'while' loop
# Each pass thru the loop prompts for a name and a mountain they would like to climb
# For each name (key) and response (value), store in empty dictionary
#Find out if anyone else is going to take the poll
#If no, set the flag to false
#Polling is complete. Show the results
responses = {}
#flag
pollingActive = True

# while pollingActive is True
# Input: What is your name?
# Input: What mountain?
# Add {name: response} to the dictionary {responses}
# Input: Anyone else want to take the poll?
# If answer is 'no', pollingActive = False
# Print poll results --> loop
# for every name and their response in responses.items(), print...

while pollingActive:
    # Inputs - name:response
    name = input("\nWhat is your name? ")
    response = input("\nWhat mountain is your favorite? ")

    # dictionary[key] = value
    responses[name] = response
    # print(responses)

    # Input - y/n
    repeat = input("\nAnyone else? (y/n) ")
    if repeat == "n":
        pollingActive = False

print("\n--- Results ---")
for name, response in responses.items():
    print(f"{name.title()}: {response.title()}")

