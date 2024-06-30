import random
import os 
import copy
os.system("clear")

# Con base en el diccionario de la lección anterior en esta practica se va a aplicar la Inmutable map para crear un map inmutable

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

prices = list(map(lambda item: item['price'], items)) 
print(prices)
print(items)

def add_taxes(item):
    new_item = copy.deepcopy(item) # Con esta linea se crea una copia del diccionario original sin modificar su valor por referencia
    new_item['taxes'] = new_item['price'] * 0.8
    return new_item

new_items = list(map(add_taxes, items))
print(f"Los nuevos items con impuestos son: {new_items}" )
print(f"Los items originales son: {items}" )
