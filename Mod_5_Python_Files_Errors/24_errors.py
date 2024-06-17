from os import system

system("clear")

"""Los errores en python son excepciones que se generan cuando el programa no puede continuar su ejecución."""

## 1. Cuando tenemos un error de identación
print("Hola") # output: IndentationError: unexpected indent

## 2. Cuando tratamos de dividir entre 0
""" print(5/0) """ # output: ZeroDivisionError: division by zero 

## 3. Cuando tratamos de llamar a una variable que no existe
print('dd') # output: NameError: name 'a' is not defined

#### Python al reconocer un error, detiene la ejecución del programa y nos muestra un mensaje de error.

## 4. Cuando hay un error de verificación de tipos

""" suma = lambda a, b: a + (b*2)
assert suma(1, 2) == 3 # output: AssertionError """

### Por otro lado hay una manera de manejar los errores, y es con el bloque try-except con el fin de hacer control de las propias excepciones  y las que se generan en el código, lo que se le conoce como pruebas unitarias.


## Ejemplo de try-except
age = 11
if age > 10:
    raise Exception(f'La edad {age} no puede ser mayor a 10') # raise es una palabra reservada que nos permite lanzar una excepción jubto a la palabra reservada Exception
print(age) # output: Exception: La edad 11 no puede ser mayor a 10