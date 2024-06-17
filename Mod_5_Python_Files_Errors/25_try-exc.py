from os import system

system("clear")

""" En python existe una forma de manejar los errores, y es con el bloque try-except con el fin de hacer control de las propias excepciones  y las que se generan en el código, lo que se le conoce como pruebas unitarias. """

### 1. Ejemplo con la excepción ZeroDivisionError
try:
    print(5/0) # output: ZeroDivisionError: division by zero
except ZeroDivisionError as error: # as es una palabra reservada que nos permite asignar un alias a la excepción
    print("No se puede dividir entre 0")

print("Vitar")

#### Esto sirve para tener un registro de los errores que se generan en el código redirigiendolos a un archivo de texto o a una base de datos, esto se le conoce como logging, y es una buena práctica para el desarrollo de software.

### 2. Ejemplo con la excepción AssertionError
try:
    assert 1 != 1 # output: AssertionError
except AssertionError as aser:
    print("Esta operación no es posible")

### 3. Ejemplo con las excepciones personalizadas mediante raise
try:
    age = 11
    if age > 10:
        raise Exception(f'La edad {age} no puede ser mayor a 10') # raise es una palabra reservada que nos permite lanzar una excepción jubto a la palabra reservada Exception
except Exception as error:
    print(error)


#### Pero a veces resulta tedioso estar escribiendo el bloque try-except, por lo que python nos ofrece una forma de manejar los errores con el bloque try-except-finally, que nos permite ejecutar un bloque de código sin importar si se generó una excepción o no.

### 4. Ejemplo con el bloque try-except-finally
try:
### Secciones de código que pueden generar errores
    print(5/0) # output: ZeroDivisionError: division by zero
    if age > 10:
        raise Exception(f'La edad {age} no puede ser mayor a 10')
    assert 1 != 1 # output: AssertionError
### Sección de código que se ejecuta si no se generó una excepción
except ZeroDivisionError as error: 
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
        print(error)
finally:
### Sección de código que se ejecuta sin importar si se generó una excepción o no
    print("Este bloque de código se ejecuta sin importar si se generó una excepción o no")