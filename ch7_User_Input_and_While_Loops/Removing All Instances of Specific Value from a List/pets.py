# Remove all instances of 'cat' from the list

pets = ['dog','cat', 'dog', 'goldfish', 'cat', 'rabbit', 'zebra', 'alligator']

while 'cat' in pets:
    pets.remove('cat')

print(sorted(pets))

