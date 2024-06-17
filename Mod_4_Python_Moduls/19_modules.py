""" Los modulos son archivos que contienen un conjunto de funciones que pueden ser importadas y utilizadas en otros programas. Por otro lado, los modulos son una forma de organizar y reutilizar código."""

# Algunos modulos que vienen por defecto en python son:
# - random: permite generar números aleatorios
from random import randint
print(randint(1, 10)) # Retorna un número aleatorio entre 1 y 10

# - os: permite interactuar con el sistema operativo
import os
os.system("clear") # Limpia la consola

# - sys: permite interactuar con el sistema operativo
from sys import path
print(path) # Muestra la ruta donde se encuentran los modulos de python

# - re: permite trabajar con expresiones regulares
import re
from re import match
print(match(r"hello", "hello world")) # Muestra el objeto match si la cadena "hello" se encuentra en "hello world", r es para indicar que es una cadena cruda

text = 'Mi numero de telefono es 123-456-789, el codigo postal es 12345, mi numero de la suerte es 7'
result = re.findall('[0-9]+', text) # Retorna una lista con los números que se encuentran en el texto
print(result) # output: ['123', '456', '789', '12345', '7']

# - time: permite trabajar con fechas y horas
import time
timestamp = time.time() # Retorna el tiempo actual en segundos
print(timestamp) # output: 1622377398.0

local_time = time.localtime() # Retorna la fecha y hora actual
result = time.asctime(local_time) # Convierte la fecha y hora actual a una cadena
print(local_time) # output: time.struct_time(tm_year=2021, tm_mon=5, tm_mday=30, tm_hour=20, tm_min=43, tm_sec=18, tm_wday=6, tm_yday=150, tm_isdst=0)
print(result) # output: Sun May 30 20:43:18 2021

# - collections: permite trabajar con colecciones
from collections import Counter
numbers = [1, 1, 2, 1, 2, 1, 4, 5, 3, 3, 21]
counter = Counter(numbers) # Retorna un diccionario con el conteo de cada elemento de la lista
print(counter) # output: Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1, 10: 1})

# - datetime: permite trabajar con fechas y horas
# - math: permite realizar operaciones matemáticas
# - json: permite trabajar con archivos json
# - csv: permite trabajar con archivos csv
# - requests: permite realizar peticiones http
# - tkinter: permite crear interfaces gráficas
# - turtle: permite crear gráficos
# - socket: permite trabajar con sockets
# - threading: permite trabajar con hilos
# - copy: permite realizar copias de objetos
# - itertools: permite trabajar con iteradores
# - functools: permite trabajar con funciones
# - operator: permite trabajar con operadores
# - logging: permite realizar logs
# - unittest: permite realizar pruebas unitarias




