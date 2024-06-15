import random
import os

os.system("clear")

# el ciclo for se usa para iterar sobre una secuencia de elementos
""" for i in range(1, 21): # se imprime del 1 al 20
    print(i) """

""" ejemplo con una lista """
my_list = [45, 56, 78, 90, 12, 34, 56, 78, 90]
for element in my_list: # se imprime cada elemento de la lista elemento se puede llamar como sea siempre y cuando se refiera al iterador
    print(element)

""" ejemplo con una tupla """
my_tuple = ('juan', 'pedro', 'maria', 'jose')
for element in my_tuple: # recorre cada elemento de la tupla
    print(element) # se imprime cada elemento de la tupla

""" ejemplo con un diccionario """
product = dict(
    name = 'David',
    price = 1000.00,
    stock = 150
)
for key in product.keys():
    print(key) # se imprime solo las llaves del diccionario
    print(key, '=>', product[key]) # se imprime la llave y el valor del diccionario

# formas mas eficientes de recorrer un diccionario mostrando las llaves y los valores en un solo ciclo
for key, value in product.items(): # recorre el diccionario y muestra las llaves y los valores
    print(key, '=>', value) # se imprime la llave y el valor del diccionario en un solo ciclo

""" recorrer un diccionario con varios diccionarios dentro usando la funcion dict() """
people = dict(
    person1 = dict(
        name = 'David',
        age = 30,
    ),
    person2 = dict(
        name = 'Juan',
        age = 25,
    ),
    person3 = dict(
        name = 'Pedro',
        age = 35,
    )
)
for person in people.values(): # se recorre el diccionario people y se muestra el valor de cada persona
    print(person['name'], person['age']) # se imprime el nombre y la edad de cada persona

for person, value in people.items(): # se recorre el diccionario people y se muestra el valor de cada persona
    print(person, '=>', value['name'], value['age']) # a diferencia del anterior, se imprime el nombre y la edad de cada persona indicando a que persona pertenece