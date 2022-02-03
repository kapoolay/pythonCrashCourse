# Using the list from 7-8
# Make sure the sandwich 'pastrami' appears in the list at least 3x
# Add a code near the beginning to print a message saying the deli has run out of pastrami
# Use a 'while' loop to remove all occurrences of 'pastrami' from 'sandwichOrders'
# Make sure no pastrami sandwiches end up in 'finishedSandwiches'

sandwichOrders = ['pastrami', 'ham', 'pastrami', 'turkey', 'pastrami', 'tuna', 'pastrami']
finishedSandwiches = []

# Loop 1
# For every order in sandwichOrders
    # print "I made your {order} sandwich"
    # append {order} to 'finishedSandwiches[]
print("I'm sorry folks, but we are sold out of pastrami!")
while 'pastrami' in sandwichOrders:
    sandwichOrders.remove('pastrami')
# print(sandwichOrders)

for order in sandwichOrders:
    print(f"I made your {order} sandwich.")
    finishedSandwiches.append(order)
# # Testing append function
# print(finishedSandwiches)

# Loop 2
# For every sandwich in finishedSandwiches
    # print sandwich
print("\nThese are the finished sandwiches: ")
for sandwich in finishedSandwiches:
    print(f"\t{sandwich.title()}")