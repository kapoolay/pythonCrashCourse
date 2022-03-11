# Write a function called 'city_country()' that takes in the name of a city and its country. The function should return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least 3 city-country pairs, and print the values that are returned.

def city_country(cityName, countryName):
    location = f"\n{cityName}, {countryName}"
    return location.title()

kevin = city_country('houston', 'united states')
print(kevin)

alexia = city_country('paris', 'france')
print(alexia)

eddy = city_country('anaheim', 'united states')
print(eddy)