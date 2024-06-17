import random
import os 
os.system("clear")

# Ejemplo de una función filter con una función lambda que retorna los números pares de una lista que tiene un diccionario
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
print(len(matches)) # Output: 3
print('\n')
## Ahora se desea filtrar una lista con solo los partidos que ganó el equipo local
new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches)) # En este caso la función filter retorna los partidos que ganó el equipo local mediante una función lambda y el iterable item
print(f'Lista nueva: {new_list}') 
print(len(new_list)) # Output: 2