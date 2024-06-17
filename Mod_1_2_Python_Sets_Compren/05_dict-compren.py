import random
import os
os.system("clear")

""" Al igual que las listas los diccionarios tambien permite implementear comprensiones
Sintaxis de un dictionary comprehension sin condicional
1. La sintaxis en el caso de los diccionarios es la siguiente:
    {key: value for value in iterable} 
    donde:
        key: es el nombre de la llave
        value: es el valor de la llave
        iterable: es el iterable que se va a recorrer"""

## Ejemmplo de un diccionario sin comprension
dict1 = {}
for i in range(1, 5):
    dict1[i] = i+3 # En este caso se suma cada numero el numero 3
print(dict1) # Al imprimirlo se puede ver que se crea un diccionario con los numeros del 1 al 4 y a cada numero se le suma 3

## Ejemplo de un diccionario con comprension
dict2 = {i: i+3 for i in range(1, 5)} # En este se emplea la sintaxis de un diccionario con comprension
print(dict2) # Al imprimirlo hace lo mismo que el ejemplo anterior

""" 2. Generar el diccionario a partir de una lista  """

## Ejemplo sin utilizar comprension
countries = ["MX", "COL", "ARG", "USA"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100) # Se genera un numero aleatorio entre 1 y 100 para cada pais
print(population) # Al imprimirlo se puede ver que se crea un diccionario con los paises y sus respectivas poblaciones

## Ejemplo utilizando comprension
population_v2 = {country: random.randint(1, 100) for country in countries} # En este se emplea la sintaxis de un diccionario con comprension
print(population_v2) # Al imprimirlo hace lo mismo que el ejemplo anterior pero en una sola linea

""" 3. Generar el diccionario a partir de dos listas """

names = ["Juan", "Maria", "Pedro", "Luisa"] # Se crea una lista con nombres
ages = [18, 25, 30, 40, 50] # Se crea una lista con edades

print(list(zip(names, ages))) # Al imprimirlo se puede ver que se crea una lista de tuplas con los nombres y sus respectivas edades

### Primera forma de crear un diccionario a partir de dos listas en este caso se emplea la funcion zip la cual permite unir dos listas
new_dict = {names: ages for (names, ages) in zip(names, ages)} # En este se emplea la sintaxis de un diccionario con comprension pero utilizando la funcion zip la cual permite unir dos listas

print(new_dict) # Al imprimirlo se puede evidenciar que se crea un diccionario con los nombres y sus respectivas edades

### Segunda forma de crear un diccionario a partir de dos listas
dict3 = {names[i]: ages[i] for i in range(len(names))} # Para este caso es importante el iterador i ya que permite recorrer las listas y crear el diccionario a diferencia del ejemplo anterior que emplea la funcion zip para unir las listas ademas len es una funcion que permite saber la longitud de una lista

print(dict3) # Al imprimirlo cumple la misma funcion que el ejemplo anterior

#### La diferencia entre la primera y la segunda forma de crear un diccionario a partir de dos listas es que en la primera se emplea la funcion zip para unir las listas y en la segunda se emplea un iterador para recorrer las listas y crear el diccionario	por lo tanto la primera forma es mas eficiente que la segunda para evitar errores de indexacion``