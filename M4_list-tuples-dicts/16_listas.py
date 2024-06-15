import random
import os

os.system("clear")

# Las listas permiten guardar varios valores en una sola variable
numbers = [1, 2, 3, 4, 5]
print(numbers)
print(type(numbers))

tasks = ["Sacar la basura", "Barrer la entrada", "Lavar los trastes"]
print(tasks)


# Listas que imprimen varios tipos de datos
types = [1, 2.5, "Hola", True, 1, 2, 3]
print(types)

# Indexing en listas es lo mismo que en strings
print(numbers[0])  # Imprime el primer elemento de la lista
print(tasks[0])  # Imprime el primer elemento de la lista


# typesindexing = [1, 2.5, 'Hola', True, [1, 2, 3]] # Listas dentro de listas

# Mutación de listas

# Se pueden hacer ajustes o cambios que se conoce como mutación pero solo en listas en cambio en strings no se puede

text = "Hola mundo"
text[0] = 'h'
print(text)
# Esto no se puede hacer en strings dado que no se pueden mutar de dicha manera pero si se pueden mediante replace por otro lado en listas si se puede

# Ejemplo de mutación en listas
tasks[0] = "Sacar al perro"

print(tasks)

# Esto puede ser util para hacer cambios en listas
tasks[0] = "Sacar al ganado"
print(tasks)

# Tambien permite seleccionar un rango de elementos y cambiarlos
tasks[0:4] = ["Sacar al perro", "Barrer la entrada"]
print(numbers[:3])  # Imprime los primeros 3 elementos de la lista

# El operador de in tambien funciona en listas
print(True in types)
print("Hola" in types)
print("Adios" in types)
