import os

from dotenv import load_dotenv
from github import Github

from general_functions import dic_countries_cities, day_time_greeting

load_dotenv()

min_population = 100_000
github_token = os.getenv('TOKEN')

repo_name = "EduardoProfe666/world-greetings"
file_path = "README.md"

g = Github(github_token)

repo = g.get_repo(repo_name)
contents = repo.get_contents(file_path)

file_content = \
    f"""
# World Greetings

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

> [!NOTE]  
> En Windows no se verán correctamente los emojis de las banderas.

Esto es un `python bot` que genera cada 5 minutos aprox un mensaje de saludo para 
cada parte del mundo en dependencia de la hora local.

Está organizado en países y ciudades, incluyendo información general de cada uno.

Por cuestiones de eficiencia solamente se incluyen las ciudades con una población mayor 
que `{min_population}` habitantes

Si te gustó deja tu estrellita en el repo 👆😏

# 🌎 Países


"""

cities_list = dic_countries_cities(min_population)

for country_code, info in cities_list.items():
    file_content += \
        f"""
## {info['flag']} {info["info"].name}

`⚜ Nombre Oficial`: {info["info"].name}

`🆔 Código Alfa-2`: {info["info"].alpha_2}

`🆔 Código Alfa-3`: {info["info"].alpha_3}

`🆔 Código numérico`: {info["info"].numeric}

    """
    for city in info['cities']:
        day, time, greeting = day_time_greeting(city)
        file_content += \
            f"""
### {city.name}
`👋 Saludo`: {greeting} 

`📅 Día`: {day}

`⌚ Hora Local`: {time} 

`ʕ•́ᴥ•̀ʔ Nombre en ASCII`: {city.asciiname}

`🗺️ Latitud`: {city.latitude}

`🗺️ Longitud`: {city.longitude}

`🗺️ Id Geográfico`: {city.geonameid}

`⏰ Zona Horaria`: {city.timezone}

`⛰️ Elevación`: {city.elevation}

`🚶‍ Población`: {city.population}

`👨‍👨‍👧‍👧 Demografía`: {city.dem}

        """

repo.update_file(contents.path, "Update greetings for all countries", file_content, contents.sha)
