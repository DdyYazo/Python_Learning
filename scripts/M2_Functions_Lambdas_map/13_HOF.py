import random
import os
os.system("clear")

""" Higher Order Functions es una funcion que recibe como parametro otra funcion o que retorna una funcion """

## 1. Ejemplo de una funcion que recibe como parametro otra funcion
def increment(n): # Esta funcion recibe como parametro un numero
    return n + 1 # Esta funcion retorna el numero ingresado mas 1

def high_order_function(x, func): # Esta funcion recibe como parametro un numero y una funcion
    return x + func(x) # Esta funcion retorna el numero ingresado mas el resultado de la funcion que se ingreso como parametro

result = high_order_function(2, increment) # Esta funcion retorna el numero 10 mas el resultado de la funcion increment y no es neceario ejecutar la funcion increment sino definirla como parametro
print(result) # Output: operacion 2 + (2 + 1) = 5


## 2. Ejemplo practico de una funcion que retorna otra funcion utilizando funciones lambda

increment_V2 = lambda x : x + 1 # Esta lamba permite hacer lo mismo que la funcion increment sin necesidad de definir una función usando def o declarar su retorno con return

high_order_function_V2 = lambda x, func: x + func(x) # Esta funcion recibe como parametro un numero y una funcion y retorna el numero ingresado mas el resultado de la funcion que se ingreso como parametro

result = high_order_function_V2(2, increment_V2) # Esta funcion retorna el numero 10 mas el resultado de la funcion increment y no es neceario ejecutar la funcion increment sino definirla como parametro
print(result) # la salida seria la operacion 2 + (2 + 1) = 5 



## 3.  Ejemplo de uso de lambdas directamente al designar los argumentos de una funcion
## Definir la función inicial como lambda
high_order_function_V2 = lambda x, func: x + func(x) # Esta funcion recibe como parametro un numero y una funcion y retorna el numero ingresado mas el resultado de la funcion que se ingreso como parametro
result = high_order_function_V2(2, lambda x: x + 1) # Al declararse la variable permite establecer como parametro una función lambda
print(result)

result = high_order_function_V2(2, lambda x: x * 2) # Esta función lambda retorna el numero ingresado multiplicado por 2
print(result) # Output: la operacion 2 + (2 * 2) = 6


## Ejemplo de una funcion que retorna otra funcion
def create_multiplier(n):
    return lambda x: x * n

multiply_by_2 = create_multiplier(2)
result = multiply_by_2(5)
print(result)  # Output: 10
