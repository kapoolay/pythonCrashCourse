# This function tells us what kind of animal each pet is and the pert's name

def describe_pet(animal_type, pet_name):
    print(f"\nI own a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Positional Arguments
describe_pet('dog', 'mia')
describe_pet('rat', 'sanchie')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Keyword Arguments
# The order of keyword arguments doesn't matter because Python knows where each value should go.
describe_pet(animal_type='dog', pet_name='mia')
describe_pet(animal_type='parrot', pet_name='spiderman')

# The function doesn't change. But when we call the function, we explicitly tell Python which parameter each argument should be matched with.
# When Python reads the function call, it knows to assign the argument 'parrot' to the parameter 'animal_type' and the argument 'spiderman' to the parameter 'pet_name'.


