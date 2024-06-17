import random
import os
os.system("clear")

""" 
FORMA INICIAL DEL PLAYGROUND

def multiply_numbers(numbers):
    newMultiply = list(map(lambda number: number*2, numbers))
    return newMultiply

numbers = [1, 2, 3, 4]
response = multiply_numbers(numbers)
print(response)
 """
 
""" SOLUCION DEL RETO EMPLEANDO RESTRICCIONES E INTERACCION CON EL USUARIO"""
def multiply_numbers(numbers):
    newMultiply = list(map(lambda number: number*2, numbers))
    return newMultiply

def get_numbers_from_user():
    numbers = []
    while True:
        number = input("Ingrese una lista de numeros y oprima 'q' para salir: ")
        if number.lower() == 'q': 
            break
        else:
            try:
                numbers.append(int(number))
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return numbers

numbers = get_numbers_from_user()
result = multiply_numbers(numbers)
print(f"Los números multiplicados por 2 son: " + str(result))
print(f"Los números multiplicados por 2 son: {result}")

