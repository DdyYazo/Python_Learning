import random
import os
os.system("clear")

""" Las funcines lambda son funciones anonimas que se pueden usar en una sola linea de codigo las cuales no poseen un identificador o no tienen un nombre"""
""" Su sintaxis es: 
    lambda argumentos: expresion
    donde:
    lambda: es la palabra reservada para indicar que es una funcion lambda
    argumentos: son los parametros que recibe la funcion, estos son opcionales
    expresion: es el cuerpo de la funcion, es decir, lo que hace la funcion """
   
## Ejemplo de una función declarativa
def increment(n):
    return n + 1

increment_V2 = lambda x : x + 1 # Esta lamba permite hacer lo mismo que la funcion increment sin necesidad de usar el return

result = increment(10)
print(result)

result = increment_V2(20)
print(result)

### En este caso una función declarativa requiere mas lineas de codigo que una función lambda

## Ejemplo de una función lambda
## Crear una lambda que devuelve el nombre completo
full_name = lambda first, last: f'The fullname is {first.title()} {last.title()}' # La sintaxis de la lambda es la misma que la de una funcion pero en este caso se compone por:
# 1. full_name: es el nombre de la funcion
# 2. lambda: es la palabra reservada para indicar que es una funcion lambda
# 3. first, last: son los parametros de la funcion
# 4. f'The fullname is {first.title()} {last.title()}': es el cuerpo de la funcion, es decir, lo que hace la funcion, utilizando la función title() para poner la primera letra en mayuscula
print(full_name('juan', 'perez'))

## Las funciones lambda son muy utiles cuando se quiere crear una funcion que se va a usar una sola vez
