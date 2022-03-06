def describe_pet(pet_name, animal_type='dog'):
    print(f"\nI own a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}!")

describe_pet(pet_name='sanchie')
describe_pet(pet_name='alvin', animal_type='chipmunk')
describe_pet(pet_name='harry', animal_type='hamster')