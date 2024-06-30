import random
import os
os.system("clear")

""" El scope o alcance en Python es la visibilidad de una variable dentro de un programa, es decir, en que partes del programa se puede acceder a una variable o no """

## 1. Ejemplo de una variable global
# En este caso la variable global es 'name' y se puede acceder a ella desde cualquier parte del programa
name = "Juan" # Variable global
print(f"El nombre es: {name}") # Se imprime el valor de la variable global

## 2. Ejemplo de una variable local
# En este caso la variable local es 'name' y solo se puede acceder a ella desde el bloque de codigo donde se declaro es decir dentro de la funcion
def print_name():
    name = "Luisa" # Variable local
    print(f"El nombre es: {name}") # Se imprime el valor de la variable local
print_name() # Se ejecuta la funcion

## 3. Ejemplo de una variable global y local
# En este caso se puede acceder a la variable global y local desde cualquier parte del programa
name = "Juan" # Variable global
def print_name():
    name = "Luisa" # Variable local
    print(f"El nombre es: {name}") # Se imprime el valor de la variable local
print_name() # Se ejecuta la funcion
print(f"El nombre es: {name}") # Se imprime el valor de la variable global

## 4. Ejemplo de convertir una variable local en global
# En este caso se puede acceder a la variable global y local desde cualquier parte del programa
def print_name():
    global name # Se declara la variable global
    name = "Luisa" # Variable local
print_name() # Se ejecuta la funcion
print(f"El nombre es: {name}") # Se imprime el valor de la variable global

### La diferencia entre una variable global y local es que la variable global se puede acceder desde cualquier parte del programa mientras que la variable local solo se puede acceder desde el bloque de codigo donde se declaro mayormente dentro de una funcion