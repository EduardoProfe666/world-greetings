from datetime import datetime
from itertools import groupby
import flag
import pycountry
import pytz


def dic_countries_cities(min_population):
    from allcities import cities
    cities_list = list(cities)
    cities_list = list(filter(lambda c: c.population > min_population and c.country_code != 'XK', cities_list))
    cities_list.sort(key=lambda c: c.country_code)

    grouped_cities = {}
    for country_code, group in groupby(cities_list, key=lambda c: c.country_code):
        cities = list(group)
        cities.sort(key=lambda c: c.name)
        grouped_cities[country_code] = {'cities': list(cities),
                                        'code': country_code,
                                        'flag': flag.flag(country_code),
                                        'info': pycountry.countries.get(alpha_2=country_code)}

    return grouped_cities


def greeting(hour):
    gr = "Buenas noches"
    if 1 <= hour < 12:
        gr = "Buenos días"
    elif 12 <= hour < 18:
        gr = "Buenas tardes"
    return gr


def day_time_greeting(city):
    t = datetime.now(pytz.timezone(city.timezone))
    day = t.strftime('%A %d/%B/%Y')
    time = t.strftime('%I:%M %p')

    return day, time, greeting(t.hour)
