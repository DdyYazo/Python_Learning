import random
import os
os.system("clear")

""" En este reto se debe crear la misma lista utilizando la característica de "List Comprehension" de Python para crear la lista de números pares de manera más concisa y eficiente"""

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = [] # Se crea una lista vacia
for number in numbers:
  if number % 2 == 0: # Se agrega la condicion de que solo se agreguen los numeros pares a la lista
    even_numbers.append(number) # Se agregan los numeros pares a la lista even_numbers hacineod uso de la funcion append la cual permite agregar elementos a una lista
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = []
even_numbers_v2 = [number for number in numbers if number % 2 == 0] # Se crea la lista even_numbers_v2 con los numeros pares de la lista numbers

print('v2 =>', even_numbers_v2)