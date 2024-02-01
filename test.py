#
#
from allcities import cities
from itertools import groupby
import flag
import pycountry


cities_list = list(cities)
cities_list = list(filter(lambda c: c.population>80_000 and c.country_code!='XK', cities_list))
cities_list.sort(key=lambda c: c.country_code)
grouped_cities = {}
for country_code, group in groupby(cities_list, key=lambda c: c.country_code):
    cities = list(group)
    cities.sort(key=lambda c: c.name)
    grouped_cities[country_code] = {'cities': list(cities),
                                    'code': country_code,
                                    'flag': flag.flag(country_code),
                                    'info': pycountry.countries.get(alpha_2=country_code)}


# Imprimir el resultado
for country_code, info in grouped_cities.items():
    print(f"Country Code: {country_code}")
    print(f'Flag: {info["flag"]}')

    print(f'Name: {info["info"].name}')
    print(f'Official Name: {info["info"].official_name}')
    for city in info['cities']:
        print(f"City: {city.name}, Population: {city.population}")

# from datetime import datetime
# import pytz
# from allcities import cities
#
# def get_current_time_in_city(city):
#     city_tz = pytz.timezone(city.timezone)
#     current_time = datetime.now(city_tz).strftime("%Y-%m-%d %H:%M:%S")
#     return f"La hora actual en {city.name} es {current_time}"
#
# # Lista de ciudades
# cities_list = list(cities)
#
# # Imprimir la hora actual en cada ciudad
# for city in cities_list:
#     print(get_current_time_in_city(city))
