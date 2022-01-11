cars = ['audi', 'bmw', 'subaru', 'toyota']

# Loops through the list of car names and looks for value 'bmw'. Print 'bmw' in uppercase instead of title case

for car in cars:
    # if the value is 'bmw' print in upper()
    if car == 'bmw':
        print(car.upper())
    # else if the value is anything else, print in title()
    else:
        print(car.title())

# repush
