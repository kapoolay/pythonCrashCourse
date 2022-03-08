def get_formatted_name(firstName, lastName):
    """Return a full name, neatly formatted"""
    fullName = f"{firstName} {lastName}"
    return fullName.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Making an Argument Optional

def get_formatted_name(firstName, middleName, lastName):
    """Return a full name, neatly formatted"""
    fullName = f"{firstName} {middleName} {lastName}"
    return fullName.title()

musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)

# To make the middle name optional, we can give the 'middleName' an empty default value and ignore the argument unless the user provides a value
# To make 'get_formatted_name()' work without a middle name, we set the default of 'middle_name' to an empty string and move it to the end of the list of parameters
# This modified version of the function works for ppl with first/last name, and it works for ppl who have a middle name as well

def get_formatted_name(firstName, lastName, middleName=''):
    """Return a full name, neatly formatted"""
    if middleName:
        fullName = f"{firstName} {middleName} {lastName}"
    else:
        fullName = f"{firstName} {lastName}"
    return fullName.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)