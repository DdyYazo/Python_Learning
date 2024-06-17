import random
import os
os.system("clear")

""" Las funciones son un conjunto de instrucciones que realizan una tarea especifica y que pueden ser reutilizadas en cualquier parte del programa. """
""" Sintaixs de una funcion """
""" def nombreFuncion(parametros):
donde:
    nombreFuncion: es el nombre de la funcion
    parametros: son los parametros que recibe la funcion, estos son opcionales
    : es un simbolo que indica que se va a definir una funcion"""
    
## Ejemplo de una funcion sin parametros
print("Ejemplo 1")
def saludo(): # Definicion de la funcion
    print("Hola, soy una funcion") # Cuerpo de la funcion
    print("Hola de nuevo, soy una funcion") # Cuerpo de la funcion
saludo()

## Ejemplo de una funcion con parametros
print("\nEjemplo 2")
def saludo2(nombre): # Definicion de la funcion
    print(f"Hola {nombre}, soy una funcion") # Cuerpo de la funcion
    print(f"Hola de nuevo {nombre}, soy una funcion") # Cuerpo de la funcion
saludo2("Juan")

## Ejemplo de una funcion que opera con parametros
print("\nEjemplo 3")
def suma(number): # Definicion de la funcion
    print(number * 2) # Cuerpo de la funcion
suma(5)

## Ejemplo de una funcion dentro de otra funcion
print("\nEjemplo 4")
def suma2(a,b): # Definicion de la funcion
    suma(a+b) # En este caso se llama a la funcion suma() dentro de la funcion suma2()
suma2(5,10) # Al imprimirse muestra la suma de los parametros de la funcion sum2() multiplicados por 2 teniendo en cuenta que la funcion suma() multiplica por 2
suma2(10,10)
