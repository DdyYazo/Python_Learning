import random
import os
os.system("clear")

""" Los conjuntos permiten hacer operaciones de conjuntos como:
- Union
- Interseccion
- Diferencia
- Diferencia simetrica
- Subconjunto
- Superconjunto
"""

""" Ejemplo de union de conjuntos """
setCountriesA = {"Mexico", "Colombia",  "Argentina",}
setCountriesB = {"Argentina", "Peru", "Italia"}

setCountriesUnion = setCountriesA.union(setCountriesB) 
print(setCountriesUnion) # Al imprimirlo se puede ver que se unieron los conjuntos y se eliminaron los elementos repetidos

# Ejemplo con el operador de union |
print(setCountriesA | setCountriesB) # Ocurre lo mismo que con el metodo union

## En este caso tanto el metodo union como el operador | hacen lo mismo



""" Ejemplo de interseccion de conjuntos """
setCountriesIntersec = setCountriesA.intersection(setCountriesB)
print(setCountriesIntersec) # Al imprimirlo solo se puede ver que se imprimio el elemento Argentina porque es el unico que se repite en los conjuntos

# Ejemplo con el operador de interseccion &
print(setCountriesA & setCountriesB) # OCurre lo mismo que con el metodo intersection

## En este caso tanto el metodo intersection como el operador & hacen lo mismo



""" Ejemplo de diferencia(resta) de conjuntos """
setCountriesDiff = setCountriesA.difference(setCountriesB)
print(setCountriesDiff) # Al imprimirlo solo se puede ver que se imprimio el elemento Mexico y Colombia porque son los unicos que no se repiten en los conjuntos y estos son los que se encuentran en el conjunto A

# Ejemplo con el operador de diferencia -
print(setCountriesA - setCountriesB) # Ocurre lo mismo que con el metodo difference

## En este caso tanto el metodo difference como el operador - hacen lo mismo



""" Ejemplo de diferencia simetrica de conjuntos """
setCountriesSymDiff = setCountriesA.symmetric_difference(setCountriesB)
print(setCountriesSymDiff) # Al imprimirlo solo se puede ver que imprime los elementos que no se repiten en los conjuntos

# Ejemplo con el operador de diferencia simetrica ^
print(setCountriesA ^ setCountriesB) # Ocurre lo mismo que con el metodo symmetric_difference

## En este caso tanto el metodo symmetric_difference como el operador ^ hacen lo mismo



""" Ejemplo de subconjunto de conjuntos 
Un subconjunto es aquel que esta contenido en otro conjunto pero en este caso el conjunto A no esta contenido en el conjunto B"""
setCountriesSub = setCountriesA.issubset(setCountriesB)
print(setCountriesSub) # Al imprimirlo solo se puede ver que imprime un booleano porque el conjunto A no es subconjunto del conjunto B

# Ejemplo con el operador de subconjunto <=
print(setCountriesA <= setCountriesB) # Ocurre lo mismo que con el metodo issubset



""" Ejemplo de superconjunto de conjuntos 
Un superconjunto es aquel que contiene a otro conjunto pero en este caso el conjunto A no contiene al conjunto B"""
setCountriesSuper = setCountriesA.issuperset(setCountriesB)
print(setCountriesSuper) # Al imprimirlo solo se puede ver que imprime un booleano porque el conjunto A no es superconjunto del conjunto B