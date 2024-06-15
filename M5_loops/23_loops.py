import random
import os

os.system("clear")

# Los ciclos anidados son ciclos dentro de ciclos. Por ejemplo, si tenemos un ciclo for y dentro de este ciclo for tenemos otro ciclo for, entonces tenemos un ciclo anidado. Los ciclos anidados son útiles cuando queremos realizar una tarea repetitiva dentro de otra tarea repetitiva. Por ejemplo, si queremos imprimir una tabla de multiplicar, podemos usar un ciclo for para recorrer los números del 1 al 10 y dentro de este ciclo for podemos usar otro ciclo for para recorrer los números del 1 al 10. De esta forma, podemos imprimir la tabla de multiplicar del 1 al 10.

""" Ejemplo de un ciclo anidado de una matriz """
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# print(matrix[0][0], matrix[0][1], matrix[0][2]) # imprime la primera fila de la matriz

for row in matrix: # row se refiere a  una lista que se recorre en la matriz
    print(row) # imprime cada fila de la matriz
    for column in row: # item se refiere a cada elemento de la fila
        print(column, end=" ") # imprime cada elemento de la fila dejando un espacio
    print() # imprime la matriz completa



""" Ejemplo de un ciclo anidado de una matriz mostrando solo dos filas """
matrix = [
    [23, 12, 11],
    [45, 52, 54],
    [71, 83, 92]
]

""" Ciclo for anidado donde solo se muestre la primera y segunda fila """
for row in range(2):  # imprime solo la primera y segunda fila de la matriz
    print(matrix[row]) # imprime cada fila de la matriz
    for column in range(3): # imprime cada elemento de la fila dejando un espacio
        print(matrix[row][column], end=" ") # imprime cada elemento de la fila dejando un espacio
    print()