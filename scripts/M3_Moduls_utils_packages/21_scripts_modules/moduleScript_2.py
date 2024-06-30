import os

os.system("clear")


""" 1. Los scripts en python son archivos que contienen código que se puede ejecutar directamente que a diferencia de los modulos no necesitan ser importados para ser utilizados. """

""" Ejemplo: Con base en el comportamiento del modulo script_2 en example.py, para solucionar este problema se debe modificar este modulo para embeberlo en una función que se pueda importar en otro modulo. """

from utils_v1 import (
    population_by_country,
    get_population,
)  # Se importan las funciones population_by_country() y get_population() del módulo utils.py

data = [
        {"Country": "Colombia", "Population": 502},
        {"Country": "Argentina", "Population": 400},
        {"Country": "Peru", "Population": 300},
        {"Country": "Mexico", "Population": 700},
    ]


# Crear la funcion para el modulo script_2.py
def run():
    keys, values = get_population()
    print(keys, values)

    country = input("Ingrese el país: ")  # Se le pide al usuario que ingrese un país
    result = population_by_country(data, country)
    print(result)

if __name__ == "__main__": # En este caso se declara el punto de entrada para que se pueda ejecutar el archivo script_2.py
    run() # Y tambien se llame la función run() para que se pueda ejecutar en otros archivos

""" 3. Sin embargo luego de haber definido la función run() y declarado la variable data fuera del scope de la función run() no se  podra ejecutar el archivo script_2.py por que no hay un control de este archivo o mayormente conocido como un punto de entrada (entry point)
Para ello se implementa un if basado en la variable __name__ que es una variable que se encuentra en todos los archivos de python y que retorna el nombre del archivo que se esta ejecutando, que se basa en una dualidad y pueda ejecutarse tanto en esta terminal como en otros archivos.
"""
# En este caso para que se puede ejecutar el archivo script_2.py se debe declarar ese punto de entrada




### EJEMPLO BASE PARA EL USO DE SCRIPTS EN PYTHON
def hello():
    print("Hola desde module.py!")

if __name__ == "__main__":
    print("module.py se está ejecutando directamente")
else:
    print("module.py se ha importado como un módulo")

# Cuando se ejecute desde la terminal el output será: module.py se está ejecutando directamente