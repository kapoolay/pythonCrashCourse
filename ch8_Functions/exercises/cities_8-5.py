# Write a function called 'describe_city()' that:
# Accepts the name of a city
# Country of the city
# Function should print a simple sentence, such as 'Houston is in USA'.
# Give the parameter for the country a default value
def describe_city(cityName, countryName='usa'):
    if countryName == 'usa':
        countryName = 'the USA'
    else:
        countryName.title()
    print(f"{cityName.title()} is in {countryName.title()}.")

# Call your function for 3 different cities
describe_city(cityName='los angeles')
describe_city('new york')

# One of which is not in the default country
describe_city(cityName='paris', countryName='france')
