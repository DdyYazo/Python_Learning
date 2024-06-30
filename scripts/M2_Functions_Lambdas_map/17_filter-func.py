import random
import os 
os.system("clear")

""" Filter en python es una función que permite filtrar elementos de una lista o diccionario con base en una condición """
""" Su sintexis es la siguiente: 
filter(función, iterable)
donde:
función: es una función que retorna un valor booleano
iterable: es una lista o diccionario
"""

# Ejemplo de una función filter con una función lambda que retorna los números pares de una lista
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Lista de números
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # En este caso se retorna los números pares de la lista meidante una función lambda filtrada por la función filter
print(even_numbers) # output: [2, 4, 6, 8, 10]
print(numbers) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
