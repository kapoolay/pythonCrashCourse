# # Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
#
# # Create an empty list for printed designs
# completed_models = []
#
# # Simulate printing each design, until none are left.
# # Move each design to 'completed_models' after printing
#
# # While there are items in unprinted designs,
# # For each design in unprinted designs, print it
# # For each printed design, add it to completed models
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     # print(current_design)
#     print(f"Completed Print: {current_design.title()}")
#     completed_models.append(current_design)
#
# # Display all completed models
# print("\n==== The following models have been printed ====")
# # print(f"\n{completed_models}")
# for completed_model in completed_models:
#     print(f"\t{completed_model.title()}")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Adding Functions

# First function will handle printing the designs.
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to 'completed_models' after printing
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

# Second will summarize the prints that have been made.
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\n==== The following models have been printed ====")
    for completed_model in completed_models:
        print(f"\t{completed_model.title()}")

# Cleaner and more organized main body using the 2 defined functions
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# This example demonstrates the idea that every function should have one specific job.
# This is more beneficial than using one function to do both jobs.
# If you're writing a function and notice the function is doing too many different tasks, try to split the code into two functions.

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Preventing a Function from Modifying a List

# You can send a copy of a list to a function like this:
# function_name(list_name[:])

# The slice notation [:] makes a copy of the list to send to the function.

# If we  didn't want to empty the list of unprinted designs in 'printing_models.py', we could call 'print_models' like this:
# print_models(unprinted_designs[:], completed_models)
















