# Make several dictionaries representing a different pet
# Each dictionary includes animalType/ownerName
pet1 = {
    'name': 'mia',
    'type': 'dog',
    'ownerName' : 'kevin',
}
# print(pet1)

pet2 = {
    'name': 'sanchie',
    'type': 'dog',
    'ownerName': 'eddy',
}
# print(pet2)

# Store dictionaries in list called "pets"
pets = []
pets.extend((pet1, pet2))
# pets.append(pet1)
# pets.append(pet2)
print(pets)

# Loop through your list printing all of the information about the animal
for pet in pets:
    print(f"Name: {pet['name'].title()}")
    print(f"\tType: {pet['type']}")
    print(f"\tOwner: {pet['ownerName'].title()}")
