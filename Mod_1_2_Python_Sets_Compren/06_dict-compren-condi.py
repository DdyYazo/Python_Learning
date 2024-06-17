import random
import os
os.system("clear")

""" Sintaxis de un dictionary comprehension con condicional
La sintaxis en el caso de los diccionarios es la siguiente:
    {key: value for value in iterable if condition} 
    donde:
        key: es el nombre de la llave
        value: es el valor de la llave
        iterable: es el iterable que se va a recorrer
        condition: es la condicion que se debe cumplir para que se agregue el elemento o no al diccionario"""

# Ejemplo del diccionario con comprension sin condicional

countries = ["MX", "COL", "ARG", "USA"]
population_V2 = {country: random.randint(1, 100) for country in countries} # En este se emplea la sintaxis de un diccionario con comprension para asignar un numero aleatorio entre 1 y 100 a cada pais
print(population_V2) # Al imprimirlo se puede ver que se crea un diccionario con los paises y sus respectivas poblaciones

# Ejemplo del diccionario anterior con condicional donde se agregan los paises con poblacion mayor a 20
result ={country: population for (country, population) in population_V2.items() if population > 20} # En este ejemplo country es la llave y population es el valor de la llave y se emplea la funcion items() para recorrer el diccionario de population_V2 y se agrega la condicion de que solo se agreguen los paises con poblacion mayor a 20 al diccionario result
print(result) # Al imprimirlo se puede ver que se crea un diccionario con los paises y sus respectivas poblaciones mayores a 20

# Ahora a partir de un texto se va a crear un diccionario comprenhension con condicional donde imprima las vocales y la cantidad de veces que aparecen en el texto
text = "Hi, my name is Juan and I am a software developer"
unique = { character: character.upper() for character in text if character in "aeiou"} # En este ejemplo se emplea la funcion upper para que las vocales aparezcan en mayuscula y se agrega la condicion de que solo se agreguen las vocales al diccionario unique
print(unique) # Al imprimirlo se puede ver que se crea un diccionario con las vocales y la cantidad de veces que aparecen en el texto

text = "Hi, my namE is Juan and I am a software developer"

# Crea un diccionario de comprensión que cuenta las ocurrencias de cada vocal en el texto, solo si la vocal aparece en el texto
character_count = {character: text.lower().count(character) for character in 'aeiou' if text.lower().count(character) > 0} # Se incluye una condición para solo agregar las vocales al diccionario si aparecen en el texto (es decir, su conteo es mayor a 0).
print(character_count)
