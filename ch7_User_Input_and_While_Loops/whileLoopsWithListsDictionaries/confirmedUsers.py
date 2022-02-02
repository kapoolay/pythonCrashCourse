# Start with users that need to be verified
# Along with an empty list for confirmed users

unconfirmedUsers = ['kevin', 'ale', 'eddy']
confirmedUsers = []

# Verify each user until there are no more users
# Move each verified user to the confirmed users

# While there are users in unconfirmedUsers --> runs until empty
# For every user
# Take the last user on the list, assign it to the variable 'currentUser'
# Print that you have verified the user
# Add this user to the end of the list called 'confirmedUsers
while unconfirmedUsers:
    currentUser = unconfirmedUsers.pop()

    print(f"Verifying user: {currentUser.title()}")
    confirmedUsers.append(currentUser)
else:
    print("\n\tEveryone is verified!")

# Display all confirmed users --> 'confirmedUsers' List
print("\nThe following users have been confirmed:")

# For every user in the confirmedUsers list, print the user
for user in confirmedUsers:
    print(user.title())