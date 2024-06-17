import random
import os
os.system("clear")

""" Para resolver este desafío, debes escribir un algoritmo que elimine los elementos repetidos para obtener un conjunto único llamado new_set. """

countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAm = {"COL", "BZ", "ARG"}

new_set = countries.union(northAm, centralAm, southAm) # Usando  el metodo union se unen los conjuntos
print(new_set) # Al imprimirlo se puede ver que se unieron los conjuntos y se eliminaron los elementos repetidos los cuales son BZ, MX, COL, ARG, USA, GT, CANADA

print(countries|northAm|centralAm|southAm) # Usando el operador | se unen los conjuntos