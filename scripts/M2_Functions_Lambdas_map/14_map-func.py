import random
import os
os.system("clear")

""" Map es una funcion que recibe como parametro una funcion y un iterable y retorna un objeto map que es un iterador que permite recorrer cada elemento del iterable y aplicarle la funcion que se ingreso como parametro a cada elemento del iterable """
""" Su sintaxis es: 
    map(funcion, iterable)
    donde:
    map: es la palabra reservada para indicar que es una funcion map
    funcion: es la funcion que se va a aplicar a cada elemento del iterable
    iterable: es el iterable que se va a recorrer """

## 1. Ejemplo base para implementar la funcion map
numbers = [2, 4, 6, 8, 10] # Se crea una lista con numeros
numbers_plus_one = [] # Se crea una lista vacia
for number in numbers: # Se recorre la lista numbers
    numbers_plus_one.append(number * 2) # Se agrega a la lista numbers_plus_one el numero de la lista numbers multiplicado por 2
print(numbers) # Output: [2, 4, 6, 8, 10]
print(numbers_plus_one) # Output: [4, 8, 12, 16, 20]

## 2. Ejemplo de la funcion map usando una función lambda en una sola linea
numbersv3 = map(lambda number: number * 2, numbers) # Se crea un objeto map que incorpora la funcion lambda que multiplica por 2 cada numero de la lista numbers
print(numbersv3) # Output: <map object at 0x7f1d9f7d7a90>
list_numbersv3 = list(numbersv3) # Se convierte el objeto map en una lista
print(list_numbersv3) # Output: [4, 8, 12, 16, 20]

## Reemplazar los valores de una lista por los valores de otra lista usando la funcion map y una funcion lambda
list1 = [1, 2, 3, 4, 5]# Se crea una lista con numeros
list2 = [6, 7, 8, 9] # Se crea una lista con numeros
list3 = map(lambda a, b: a + b, list1, list2) # Se crea un objeto map que incorpora la funcion lambda que suma los valores de las dos listas
print(list1) # Output: [1, 2, 3, 4, 5]
print(list2) # Output: [6, 7, 8, 9]
print(list3) # Output: <map object at 0x7f1d9f7d7a90>
list3 = list(list3) # Se convierte el objeto map en una lista
print(list3) # Output: [7, 9, 11, 13] debido a que la lista 2 tiene un elemento menos que la lista 1 el resultado es una lista con 4 elementos


### Utilidad: 
# La función map es una de las funciones más utilizadas en Python, ya que permite aplicar una función a cada elemento de un iterable (lista, tupla, etc.) y retornar un iterador para recorrer los resultados y permite reducir el código y hacerlo más legible utilizando ademas funciones lambda.