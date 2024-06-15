import random
import os

os.system("clear")

# El ciclo while sirve para ejecutar un bloque de codigo mientras se cumpla una condicion
# el ciclo while se ejecuta mientras la condicion sea verdadera
while True:
    print("se ejecuto el ciclo while")  # se ejecuta infinitamente

""" Ejemplo cpn un contador """
counter = 0  # contador inicia en 1
while counter < 10:
    counter += 1  # el contador se incrementa en 1
    print(counter)  # se imprime el contador del 1 al 10

""" para detener el ciclo while se usa el break """
counter = 0
while counter < 20:
    counter += 1
    if counter == 15:  # se detiene el ciclo cuando el contador llega a 15
        break  # se detiene el ciclo cuando el contador llega a 15
    print(counter) # se imprime el contador del 1 al 14

""" para saltar un ciclo se usa el continue """
counter = 0
while counter < 20:
    counter += 1
    if (
        counter < 15
    ):  # si el contador es menor a 15 se salta el ciclo y continua con el siguiente
        continue  # en este caso  ignora el ciclo inicial que imprime los valores del  1 al 14 y continua con el 15 hasta completar el ciclo while
    print(counter) # se imprime el contador del 15 al 20
