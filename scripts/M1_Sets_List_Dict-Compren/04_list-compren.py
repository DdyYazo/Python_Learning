import random
import os
os.system("clear")

""" Las listas de comprensión son una forma de crear listas de forma rápida y sencilla. 
La sintaxis es muy similar a la de los conjuntos, pero en lugar de usar llaves, se usan corchetes.

1. La sintaxis es la siguiente:
[element for element in iterable]
En donde:
- element es la variable que se va a agregar a la lista
- iterable es una colección de elementos como una lista, un conjunto, una tupla, etc.
"""


## Ejejmplo de una lista sin comprension
numbers = []
for element in range(1, 11):
    # numbers.append(element) # Al imprimirlo se puede ver que se crea una lista con los numeros del 1 al 10
    numbers.append(element*2) # Ahora en este caso se crea una lista con los numeros del 1 al 10 multiplicados por 2
print(numbers)


## Ejemplos de una lista con comprension
# numbers_V2 = [element for element in range(1, 11)] # En este caso se crea una lista con los numeros del 1 al 10
numbers_Com = [element*2 for element in range(1, 11)] # Tambien se puede hacer operaciones con los elementos de la lista siguiendo esta sintaxis
print(numbers_Com) # Al imprimirlo se puede ver que se crea una lista con los numeros del 1 al 10



""" 2. Por otro lado, tambien es posible agregar condicionales a la lista de comprensión:
[element for element in iterable if condition]
En donde:
- element es la variable que se va a agregar a la lista
- iterable es una colección de elementos como una lista, un conjunto, una tupla, etc.
- condition es una condición que se debe cumplir para agregar el elemento a la lista """


## Ejemplo sin list comprenhention con condicionales
numbersCon = []
for i in range(1, 11):
    if i % 2 == 0: # En este caso se crea una condicion para que solo se agreguen los numeros pares
        numbersCon.append(i*2) # Luego cada numero se multiplica por 2
print(numbersCon) # Al imprimirlo se puede ver que se crea una lista con los numeros del 1 al 20 pero solo los pares pero de dos en dos


## Ejemplo de una list comprenhention con condicionales
numbers_V3 = [i*2 for i in range(1, 11) if i % 2 == 0] # En este caso se crea una lista con los numeros del 1 al 10 pero solo los pares
print(numbers_V3) # Al imprimirlo se puede ver que se crea una lista con los numeros del 1 al 10 pero solo los pares



""" Ejemplo con los dias de la semana en español """
days = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
newlist = []
for i in days:
    if "a" in  i:
        newlist.append(i)
print(newlist)


## Ejemplo con list comprenhention
newlist2 = [i for i in days if "a" in i]
print(newlist2)