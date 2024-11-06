import csv, os

__location__ = os.getcwd()

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))

class info:
    def __init__(self, temperature, latitude, longitude):
        self.temperature = temperature
        self.latitude = latitude
        self.longitude = longitude

    def get_temperature(self):
        return self.temperature
    def get_latitude(self):
        return self.latitude
    def get_longitude(self):
        return self.longitude
    def __repr__(self):
        return f'{self.temperature} {self.latitude} {self.longitude}'


class City:
    def __init__(self, city_name, temperature, latitude, longitude):
        self.city_name = city_name
        self.info = info(temperature, latitude, longitude)
    def get_city_name(self):
        return self.city_name

    def get_info(self):
        return self.info

    def __repr__(self):
        return f"City: {self.city_name}, Info: {self.info}"
class AllCity:
    def __init__(self, cities_data):
        self.all_cities = [City(item['city'], item['temperature'], item['latitude'], item['longitude']) for item in cities_data]

    def __repr__(self):
        return f"Allcity: {self.all_cities}"

    def find_city_index(self, name):
       for index, city in enumerate(self.all_cities):
           if city.city_name.lower() == name.lower():
               return index

    def average_temperature(self, country=None):
       temp = [] # list collect temp which city specified
       for city in self.all_cities:
           if country is None or city.city_name.lower() == country.lower():
               temp.append(float(city.info.temperature))
       if temp:
           avg_temperature = sum(temp) / len(temp)
       else:
           return None
       return avg_temperature

    def max_temperature(self, country=None):
       temp = [float(city.info.temperature) for city in self.all_cities if city.city_name == country or country is None]
       return max(temp) if temp else None


    def min_temperature(self, country=None):
       temp = [float(city.info.temperature) for city in self.all_cities if city.city_name == country or country is None]
       min_temperature = min(temp)
       return min_temperature

    def filter_cities(self, condition):
       # Use city as the loop variable and pass it to the condition function
       filter_list = [ city for city in self.all_cities if condition(city)]
       return filter_list

    def  aggregate(self,aggregation_key, aggregation_function):
        list_info = []
        for city in self.all_cities:
             element = getattr(city.info, aggregation_key, None)
             if element is not None:
                 list_info.append(element)
        return aggregation_function(list_info) if list_info else None


#Print the min and max latitude for cities in every country
all_cities = AllCity(cities)
min_latitude = all_cities.aggregate(aggregation_key='latitude', aggregation_function=min)
max_latitude = all_cities.aggregate(aggregation_key='latitude', aggregation_function=max)
print(min_latitude)
print(max_latitude)
countries_min_latitude = all_cities.filter_cities(condition=lambda city: city.info.latitude == min_latitude )
print(countries_min_latitude)
countries_max_latitude = all_cities.filter_cities(condition=lambda city: city.info.latitude == max_latitude )
print(countries_max_latitude)







