import random
import os
os.system("clear")

""" La función map tambien se puede usar en diccionarios """

## Ejemplo de la funcion map en diccionarios usando una lista de diccionarios
items = [
    {
     'product': 'laptop',
     'price': 800,
     },
    {
        'product': 'mouse',
        'price': 40,
    },
    {
        'product': 'monitor',
        'price': 400,
    }
]

## Imprimir la lista de los precios de los productos
prices = list(map(lambda item: item['price'], items)) # Se crea un objeto map que incorpora la funcion lambda que retorna los precios de los productos del diccionario items
print(items) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]
print(prices) # Output: [800, 40, 400]

# 1. Importar la biblioteca copy
import copy
# 2. Crear una copia del array original
## Primer modo de crear una copia del array original
items_cp = copy.copy(items)
print(items_cp) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]

## Segundo modo de crear una copia del array original
items_copy = copy.deepcopy(items)
print(items_copy) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]

###  La diferencia entre el primer y el segundo modo de crear una copia del array original es que copy solo crea una copia superficial del array original mientras que deepcopy crea una copia profunda del array original, es decir, si el array original tiene un array dentro de otro array entonces deepcopy crea una copia de cada array

## Ahora si se busca designar un impuesto a cada producto se puede hacer de la siguiente manera
# 1. Crear una funcion que calcule el impuesto
def add_taxes(item):
    item['taxes'] = item['price'] * 0.8
    return item

# 2. Definir la funcion en la funcion map
new_item = list(map(add_taxes, items)) # Se crea un objeto map que incorpora la funcion add_taxes que retorba todos los items del diccionario items con el impuesto
print(new_item) # Output: [{'product': 'laptop', 'price': 800, 'impuesto': 640.0}, {'product': 'mouse', 'price': 40, 'impuesto': 32.0}, {'product': 'monitor', 'price': 400, 'impuesto': 320.0}]
print(items) # En la salida se puede evidenciar que hubo un cambio en el array original lo que puede generar problemas en el codigo o errores de logica, entonces para solucionar ello se puede utilizar la biblioteca copy para crear una copia del array original y no modificarlo
print(items_copy) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]
