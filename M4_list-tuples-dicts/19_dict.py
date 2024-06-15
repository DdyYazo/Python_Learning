import random
import os

os.system('clear')

# Los diccionarios son estructuras de datos que permiten almacenar valores de diferente tipo, como enteros, cadenas, listas e incluso otros diccionarios.
my_dict = {}
print(my_dict)
print(type(my_dict))

#   
# 1. Con llaves
my_dict = {
    'name': 'David',
    'lastname': 'Yazo',
    'nickname': 'Tdow',
    'age': 30
}
print(my_dict)
# 2. Con la función dict()
my_dict = dict(
    name = 'David',
    lastname = 'Yazo',
    nickname = 'Tdow',
    age = 30
)
print(my_dict)

print(len(my_dict)) # la dimension del diccionario es 4
print(my_dict['name']) # acceder a un elemento del diccionario
print(my_dict['lastname'], my_dict['nickname']) # acceder a varios elementos del diccionario
print(my_dict.get('xvalor')) # si no existe la llave, con get devuelve None

# print(my_dict['xvalor']) # sin get en este caso, devuelve un error
print('name' in my_dict, 'papa' in my_dict) # in busca en las llaves del diccionario

""" Agregar elementos al diccionario """
my_dict['phone'] = '123456789'
print(my_dict)

""" Eliminar elementos del diccionario """
del my_dict['phone']
print(my_dict)

""" Recorrer el diccionario """
""" for key in my_dict.keys():
    print(key) """