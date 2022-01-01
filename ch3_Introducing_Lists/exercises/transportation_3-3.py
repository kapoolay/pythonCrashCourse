#Think of your favorite mode of transportaion, such as a motorcycle or a car, and make a list that stores several examples. Use your list to print a series of statements about these items, such as "I would like to own a Honda motorcycle"

vehicles = ['tesla', 'harley', 'jeep', 'plane']

message_dream = 'My dream car is a'
message_dangerous = 'The most dangerous vehicle is probably'
message_fly = 'I would love to be able to fly a'

print(f'{message_dream} {vehicles[0].title()}!\n')
print(f'{message_dangerous} {vehicles[1].title()}!\n')
print(f'{message_fly} {vehicles[3]}!\n')
