# This function tells us what kind of animal each pet is and the pert's name

def describe_pet(animal_type, pet_name):
    print(f"\nI own a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

describe_pet('dog', 'mia')