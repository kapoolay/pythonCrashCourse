# 5 programming words as keys
# Values store their meanings
glossary = {
    'dictionary': 'Dictionaries are used to store data values in key:value pairs.',
    'list': 'Lists are used to store multiple items in a single variable',
    'tuples': 'Tuples are unchangeable lists',
    'variables': 'Variables are containers for storing data values',
    'comments': 'Comments starts with a #, and Python will ignore them',
    'sets': 'A set is a collection which is unordered, unchangeable*, and unindexed',
    'booleans': 'Booleans represent one of two values: True or False',
    'for loop': 'A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string)',
    'arrays': 'Arrays are used to store multiple values in one single variable',
    'Python Operators': 'Operators are used to perform operations on variables and values'
}

# Loop thru dictionary
# Print out Key: Value pairs cleanly

for key, value in glossary.items():
    print(f"\n{key.title()}:\n\t{value}")
