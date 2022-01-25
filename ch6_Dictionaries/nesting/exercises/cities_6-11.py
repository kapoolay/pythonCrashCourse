# Make a {dictionary} called cities
# 3 cities as keys
# each key includes country/population/fact ---> Dictionary within a dictionary
cities = {
    'houston': {
        'country': 'united states',
        'population': '3 million',
        'fact': 'it is very hot'
    },
    'paris': {
        'country': 'France',
        'population': '4 million',
        'fact': 'Eiffel Tower resides there'
    },
    'toronto': {
        'country': 'canada',
        'population': '3.5 million',
        'fact': 'the Raptors are based out of this city'
    },
}
# for every city in cities
# for every key/value in city
# print

# Print each city and all of the info
for city, cityInfo in cities.items():
    print(f"\n{city.title()}:")
    country = cityInfo['country']
    # print(country)
    population = cityInfo['population']
    # print(population)
    fact = cityInfo['fact']
    # print(fact)
    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population.title()}")
    print(f"\tFact: {fact.title()}")
