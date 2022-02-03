# Make a list called 'sandwichOrders'
# Fill it with names of various sandwiches
# Make an empty list 'finishedSandwiches'
# Loop through the list of sandwich orders and print a message for each order -- "I made your {type} sandwich"
# As each sandwich is made, move it to 'finishedSandwiches'
# Once all sandwiches are done, print a message listing each sandwich that was made

sandwichOrders = ['ham', 'turkey', 'tuna']
finishedSandwiches = []

# Loop 1
# For every order in sandwichOrders
    # print "I made your {order} sandwich"
    # append {order} to 'finishedSandwiches[]
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