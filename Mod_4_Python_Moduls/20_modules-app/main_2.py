
# En este caso se va a importar la función get_population() del módulo mod.py y se va a emplear en el programa main.py
""" 1. Para poder usar las funciones y variables definidas en un módulo se emplea la siguiente sintaxis 
from nombre_modulo import nombre_funcion, nombre_variable
donde: 
- nombre_modulo es el nombre del archivo sin la extensión .py
- nombre_funcion es el nombre de la función que se va a importar
- nombre_variable es el nombre de la variable que se va a importar
"""

""" 1.1 Ademas se puede renombrar un modulo o una función al importarla de la siguiente manera
- Para el modulo es:
import nombre_modulo as nuevo_nombre 
- Para las funciones o variables 
from nombre_modulo import nombre_funcion as nuevo_nombre"""

# Ejemplo


import utils_1 as u  # De este modo se importa el módulo utils.py y se le asigna el nombre u

keys, values = (
    u.get_population()
)  # De este modo se importa la función get_population() del módulo utils.py y se asigna a las variables keys y values
print(keys, values)


""" 2. Ahora en este caso Para mostrar la variable A del módulo mod.py se emplea la siguiente sintaxis
 """
print(u.A)  # De este modo se imprime la variable A del módulo mod.py

# En el segundo caso se va a hacer uso de la función population_by_country() del módulo utils.py definiendo una lista de diccionarios con la población de varios países y se va a emplear en el programa main.py

data = [
    {"Country": "Colombia", "Population": 502},
    {"Country": "Argentina", "Population": 400},
    {"Country": "Peru", "Population": 300},
    {"Country": "Mexico", "Population": 700},
]  # Se define una lista de diccionarios con la población de varios países
result = u.population_by_country(
    data, "Colombia"
)  # Se crea una variable llama result que almacena el resultado de la función population_by_country() del módulo utils.py y solo se le pasa el país "Colombia" junto con su población
print(
    result
)  # Output: [{'Country': 'Colombia', 'Population': 502}] # Se imprime el resultado de la función population_by_country() del módulo utils.py

""" 2.1 Otro modo de hacerlo es aplicando la sintaxis from nombre_modulo import * donde se importan todas las funciones y variables definidas en el módulo. """

from utils_1 import (population_by_country,)  # De este modo se importa la función population_by_country() del módulo utils.py y no es necesario emplear  utils.population_by_country() para usarla sino solo population_by_country()

result2 = population_by_country(
    data, "Argentina"
)  # Se crea una variable llama result que almacena el resultado de la función population_by_country() del módulo utils.py y solo se le pasa el país "Argentina" junto con su población
print(
    result2
)  # Output: [{'Country': 'Argentina', 'Population': 400}] # Se imprime el resultado de la función population_by_country() del módulo utils.py
