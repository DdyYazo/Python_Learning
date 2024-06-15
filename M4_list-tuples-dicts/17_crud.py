import random
import os

os.system("clear")
# CRUD Create Read Update & Delete
numbers = [1, 2, 3, 4, 5]
print(numbers[1])
numbers[-1] = 10
print(numbers)


""" El metodo append agrega un elemento al final de la lista "El Create" """
numbers.append(
    700
)  # El append solo permite agregar un elemento a la vez al final de la lista
print(numbers)

"""El metodo insert permite agregar un elemento en una posición especifica """
numbers.insert(
    0, "SOPA"
)  # El insert permite agregar un elemento en una posición especifica
print(numbers)


"""El insert permite agregar un elemento en una posición especifica sin sobreescribir el elemento que se encuentra en dicha posición "El Create"""
numbers.insert(2, "Macaco")
print(numbers)  # Imprime la lista con el nuevo elemento en la posición 2


""" Uniendo listas con el operador + """

tasks = ["todo 1", "todo 2", "todo 3"]
new_list = numbers + tasks
print(new_list)

""" Metodo index para cambiar un elemento de la lista "El Update" """
index = new_list.index("todo 1")
# Autoamaticamente detecta la posición del elemento
new_list[index] = "todo 1.1"  
# Se puede cambiar el elemento definido en el index de la posición que se encuentra
print(new_list)


""" Metodo remove para eliminar un elemento de la lista "El Delete" """
new_list.remove("todo 1.1") 
# Elimina el elemento que se encuentra en el index de la posición que se encuentra
print(new_list)

""" Metodo pop para eliminar un elemento de la lista automaticamente "El Delete" """
new_list.pop()  
# Elimina automaticamente el elemento que se encuentra em la posición especifica en este caso el ultimo elemento
print(new_list)

new_list.pop(0) 
# Elimina automaticamente el elemento que se encuentra em la posición especifica
print(new_list)


""" Metodo reverse para invertir el orden de la lista "El Update" """
new_list.reverse()  # Invierte el orden de la lista
print(new_list)

""" Metodo sort para ordenar la lista "El Update" """
numbers_a = [1, 5, 3, 2, 4]
numbers_a.sort() # Ordena la lista de menor a mayor
print(numbers_a)

strings = ["ez", "ar", "bs", "ca", "di"]
strings.sort()  # Ordena la lista de menor a mayor
print(strings)


""" En el caso de listas mezcladas no se puede usar el metodo sort dado que no se puede ordenar numeros con strings """
new_list.sort()  # Ordena la lista de menor a mayor en este caso no se puede dado que hay strings y numeros lo que genera un error
print(new_list)
