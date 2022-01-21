# 5 programming words as keys
# Values store their meanings
glossary = {
    'dictionary': 'Dictionaries are used to store data values in key:value pairs.',
    'list': 'Lists are used to store multiple items in a single variable',
    'tuples': 'Tuples are unchangeable lists',
    'variables': 'Variables are containers for storing data values',
    'comments': 'Comments starts with a #, and Python will ignore them',
}

# Print each word and it's meaning as neatly formatted output

# # Key: Value
# print(f"Dictionary: {glossary['dictionary']}")
# print(f"List: {glossary['list']}")
# print(f"Tuples: {glossary['tuples']}")
# print(f"Variables: {glossary['variables']}")
# print(f"Comments: {glossary['comments']}")

# # Key
#     # Value
# print(f"Dictionary:\n\t{glossary['dictionary']}")
# print(f"List:\n\t{glossary['list']}")
# print(f"Tuples:\n\t{glossary['tuples']}")
# print(f"Variables:\n\t{glossary['variables']}")
# print(f"Comments:\n\t{glossary['comments']}")

#Loop
# for x,y in thisDict.items():
# 	print(x, y)
for x,y in glossary.items():
    print(f"{x.title()}:\n\t{y}.")
