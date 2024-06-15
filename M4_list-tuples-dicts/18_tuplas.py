import random
import os

os.system("clear")
# Las tuplas permite imprimir varios tipos de datos (int, float, string, bool, list, tuple)

# Las tuplas a diferencia de las listas no se pueden modificar
numers = (1, 2, 3, 4, 5)  # Tuplas de numeros
print(numers)
print(type(numers))

""" Especificando una posicion en la tupla """
print('0 =>',numers[0]) # Imprime el primer elemento de la tupla
print('-1 =>',numers[-1]) # Imprime el ultimo elemento de la tupla

strings = ("Hola", "Mundo", "Python", "Hola")  # Tuplas de strings
print(strings)
print(type(strings))

""" En una tupla solo es posible la declaración pero no se podran insertar nuevos elementos """
""" numers.apeend(6) # Esto no se puede hacer en tuplas
print(numers)
numers[0] = 'cambio' # Esto de igual manera no se puede hacer en tuplas """


""" Se puede acceder a un elemento de la tupla mediante su index """
print(strings.index('Python')) # Imprime el index del elemento que se encuentra en la tupla

""" Saber la camtidad de elementos que se repiten en la tupla """
print(strings.count('Hola'))

""" Transformación de tuplas a listas """
my_list = list(strings) # Transforma la tupla a una lista
print(my_list)
print(type(my_list))

my_list[1] = 'Mundo 2.0' # Se puede modificar la lista
print(my_list)

""" Transformación de listas a tuplas """
my_tuple = tuple(my_list) # Transforma la lista a una tupla
print(my_tuple)
print(type(my_tuple))

