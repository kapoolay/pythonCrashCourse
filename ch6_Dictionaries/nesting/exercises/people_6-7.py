# Start with 6-1 program
# Make 2 new dictionaries representing different people
person1 = {
    'firstName': 'kevin',
    'lastName': 'capule',
    'age': 30,
    'city': 'houston'
}

person2 = {
    'firstName': 'alexia',
    'lastName': 'filipputti',
    'age': 27,
    'city': 'paris'
}

person3 = {
    'firstName': 'mia',
    'lastName': 'capule',
    'age': 8,
    'city': 'colorado'
}

# store all 3 dictionaries in a list called people
people =[]
people.append(person1)
people.append(person2)
people.append(person3)
# print(people)

# loop thru the list of people
# Print every info about each person
# first/last/age/city
for person in people:
    # print(f"{person['firstName'].title()} {person['lastName'].title()} is {person['age']} and is from the city of {person['city'].title()}!")
    fullName = f"{person['firstName'].title()} {person['lastName'].title()}"
    # print(fullName)
    age = person['age']
    # print(age)
    city = f"{person['city'].title()}"
    # print(city)
    print(f"\n{fullName}, from the city of {city}, is {age} years old.")


















#
