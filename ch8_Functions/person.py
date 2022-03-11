def build_person(firstName, lastName):
    """Return a dictionary of information about a person"""
    person = {'first': firstName, 'last': lastName}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Store a person's age as well

def build_person2(firstName, lastName, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': firstName, 'last': lastName}
    if age:
        person['age'] = age
    return person

musician2 = build_person2('kevin', 'capule', 30)
print(musician2)

