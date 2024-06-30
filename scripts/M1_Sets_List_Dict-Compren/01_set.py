import random
import os 
os.system("clear")

""" Los conjuntos son una colección de elementos que no están ordenados ni indexados.
Estos se pueden:
- Modificar
Sin embargo:
- No tienen orden
- No permiten duplicados"""

# Crear un conjunto de textos
set1 = {"Hola", "Mundo", "Mundo"} # Estos se declaran entre brequets {} y separados por comas
print(set1) # Al imprimirlo se puede ver que el elemento duplicado no se imprime
print(type(set1)) # Al imprimir el tipo de dato se puede ver que es un conjunto

# Crear un conjunto de numeros
setNumber = {1, 2, 3, 4, 5, 6, 7, 8, 9, 9}
print(setNumber) # Al imprimirlo se puede ver que el elemento duplicado no se imprime


# Crear un conjunto de numeros y textos al igual que las listas
setTypes = {1, 2, 3, "Hola", "Mundo", 4, 5, 6, 7, 8, 9, False}
print(setTypes) # Output: {False, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Hola', 'Mundo'}


""" Conjuntos a partir de estructuras de datos """

# Crear un conjunto a partir de un string implementado la forma explisita
setString = set("HolaaaMundo") # Esta es la manera en que deseo un conjunto a partir de un string
print(setString) # Output: {'a', 'H', 'M', 'o', 'l', 'n', 'd', 'u'} 
print(type(setString)) # Output: <class 'set'>

# Crear un conjunto a partir de una tupla
setTuple = set(('abc', 'cbv', 'as','abc')) # Esta es la manera en que deseo un conjunto a partir de una tupla
print(setTuple) # Al imprimirlo se puede ver que los elementos repetidos no se imprimen

# Crear un conjunto a partir de una lista de numeros
numbers = ([1, 2, 3, 1, 2, 3, 4]) # Esta es la manera en que deseo un conjunto a partir de una lista
setNumbers = set(numbers) # En este caso se crea una variable para almacenar el conjunto
print(setNumbers) # output: {1, 2, 3, 4}

# Ahora se pueden pasar los elementos de un conjunto a una lista
listNumbers = list(setNumbers) # Uso de la funcion list() para convertir el conjunto a una lista
print(listNumbers) # Output: [1, 2, 3, 4]
