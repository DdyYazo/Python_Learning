# En este caso es necesario importar la libreria functools para poder utilizar la función reduce
import functools
from functools import reduce # Otra forma de importar la función reduce pero solo la función reduce
import os 
os.system("clear")

""" La función reduce de Python es una función que permite reducir una lista a un solo valor aplicando una función a cada elemento de la lista. """
""" Su sintexis es la siguiente:
reduce(función, iterable)
donde:
función: es una función que retorna un valor booleano
iterable: es una lista o diccionario
"""
# Ejemplo de una función reduce con una función lambda que retorna la suma de los elementos de una lista
numbers = [1, 2, 3, 4, 5]
result_1 = functools.reduce(lambda counter, item: counter + item, numbers) # Retorna la suma de los elementos de la lista que a diferencia de filter y map no retorna una lista sino un solo valor
print(result_1) # Output: 15
print('\t')
## Explicación de la función reduce en el ejemplo anterior
def sum(counter, item):
    print(f'counter: {counter}, item: {item}')
    return counter + item 
result = functools.reduce(sum, numbers)
print('\t')
print(f'El resultado de la suma entonces seria: {result}')

# Ejemplo de una función reduce con una función lambda que retorna un valor especifico de una lista de diccionarios
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
] # Esta lista de diccionarios muestra los resultados de los partidos de futbol
print(f'Lista original: {matches} ')
print(len(matches))
print('\n')
## Ahora se desea obtener la suma de los goles de los partidos
total_goals = functools.reduce(lambda counter, item: counter + item['home_team_score'] + item['away_team_score'], matches, 0) # Retorna la suma de los goles de los partidos tanto de local como de visitante
print(f'La suma de los goles de los partidos es: {total_goals}')

## Explicación de la función reduce en el ejemplo anterior
def sum_goals(counter, item):
    print(f'counter: {counter}, item: {item}')
    return counter + item['home_team_score'] + item['away_team_score']
result = functools.reduce(sum_goals, matches, 0) # El 0 es el valor inicial de la variable counter
print('\t')
print(f'El resultado de la suma entonces seria: {result}')