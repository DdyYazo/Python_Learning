""" Debes utilizar la función my_divide, que recibe dos parámetros de entrada que representan los números a dividir. Dentro de esta función, debes implementar la lógica necesaria para capturar la excepción ZeroDivisionError. """

def my_divide(a, b):
   try:
      result = a / b
   except ZeroDivisionError as error:
      result = 'No se puede dividir entre 0'
   return result
    
response = my_divide(10, 2)
print(response) # 5

response = my_divide(10, 0)
print(response) # No se puede dividir por 0
