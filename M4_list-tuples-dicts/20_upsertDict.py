import random
import os

os.system("clear")

person = dict(
    name="David", 
    last_name="Yazo",
    langs=["Python", "JavaScript", "C++"],
    age=99
)
print(person)


""" Agregar elementos al diccionario """
person["name"] = "Pepe"  # reemplazar un elemento del diccionario
person["age"] -= 50  # reemplazar un elemento del diccionario restando 50 a la edad
person["langs"].append("Go")  # agregar un elemento a la lista mediante el metodo append
print(person)


""" Eliminar elementos del diccionario """

# metodo del para eliminar elementos del diccionario
del person["last_name"]
del person["langs"][1]  # eliminar un elemento de la lista
print(person)

# metodo pop
person.pop("age")  # devuelve el valor eliminado debe especificar la llave
print(person)

""" obtener los items, las llaves y los valores  del diccionario en forma de arreglo """
# El metodo items devuelve una tupla con los items del diccionario
print(f"los items  del diccionario son: {person.items()}")
# El metodo keys devuelve una tupla con las llaves del diccionario
print(f"las llaves  del diccionario son: {person.keys()}")
# El metodo values devuelve una tupla con los valores del diccionario
print(f"los valores del diccionario son: {person.values()}")

""" copiar un diccionario """
# copiar un diccionario con el metodo copy
person2 = person.copy()
print(person2)


""" Recorrer el diccionario """
""" for key in person.keys():
    print(key) """
