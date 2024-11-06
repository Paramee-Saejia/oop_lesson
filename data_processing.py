import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

# Load cities data
cities = []
with open(os.path.join(__location__, 'cities.csv')) as file:
    rows = csv.DictReader(file)
    for row in rows:
        cities.append(row)

countries = []
with open(os.path.join(__location__, 'countries.csv')) as file:
    rows = csv.reader(file)
    for row in rows:
        countries.append(row)


# Function to calculate average temperature
def average_temperature(cities, country=None):
    temps = []
    for city in cities:
        if country is None or city['country'].lower() == country.lower():
            temps.append(float(city['temperature']))

    if temps:
        return sum(temps) / len(temps)
    else:
        return None


# Function to calculate max temperature
def max_temperature(cities, country=None):
    temps = []
    for city in cities:
        if country is None or city['country'].lower() == country.lower():
            temps.append(float(city['temperature']))

    if temps:
        return max(temps)
    else:
        return None


# Function to calculate min temperature
def min_temperature(cities, country=None):
    temps = [float(city['temperature']) for city in cities if country is None or city['country'].lower() == country.lower()]
    return min(temps) if temps else None


# Print the average temperature of all the cities
print("The average temperature of all the cities:")
print(average_temperature(cities))
print()

# Print all cities in Italy
my_country = 'Italy'
cities_temp = [city['city'] for city in cities if city['country'].lower() == my_country.lower()]
print(f"All the cities in {my_country}:")
print(cities_temp)
print()

# Print the average temperature for all the cities in Italy
print(f"The average temperature of all the cities in {my_country}:")
print(average_temperature(cities, my_country))
print()

# Print the max temperature for all the cities in Italy
print(f"The max temperature of all the cities in {my_country}:")
print(max_temperature(cities, my_country))
print()

# Print the min temperature for all the cities in Italy
print(f"The min temperature of all the cities in {my_country}:")
print(min_temperature(cities, my_country))
print()

# Function to filter out cities based on a condition
def filter_cities(condition, dict_list):
    filtered_list = [item for item in dict_list if condition(item)]
    return filtered_list


# Filter cities with latitude >= 60
cities_above_latitude_60 = filter_cities(lambda x: float(x['latitude']) >= 60.0, cities)
for item in cities_above_latitude_60:
    print(item)

# Aggregate function to group by country and calculate a value (average temperature)
def aggregate(aggregation_key, aggregation_function, dict_list):
    data_dict = {}
    for dict in dict_list:
        value = dict.get(aggregation_key)
        if value not in data_dict:
            data_dict[value] = []
        data_dict[value].append(dict)   #create dic in list

    aggregation_result = {}
    for key, value in data_dict.items():
        aggregation_result[key] = aggregation_function(value)

    return aggregation_result

# - print the average temperature for all the cities in Italy
# - print the average temperature for all the cities in Sweden
for country in ['Italy', 'Sweden']:
    aggregated_data = aggregate(aggregation_key='country', aggregation_function=average_temperature, dict_list=cities)
    average_temp = aggregated_data.get(country, "Not found")
    print(f"The average temperature for all cities in {country}: {average_temp}")

# - print the min temperature for all the cities in Italy
aggregated_data_min = aggregate(aggregation_key='country', aggregation_function=min_temperature, dict_list=cities)
min_temp_Italy = aggregated_data_min.get('Italy', "Not found")
print(f"the min temperature for all the cities in Italy is {min_temp_Italy} ")
aggregated_data_max = aggregated_data_min = aggregate(aggregation_key='country', aggregation_function= lambda x:min_temperature(x), dict_list=cities)
max_temp_Sweden = aggregated_data_max.get('Sweden', 'Not Found')
print(f"the max temperature for all the cities in is {max_temp_Sweden} ")