""" Tu reto es implementar la función read_csv que lee el archivo CSV y calcula el total de gastos de la empresa. Para leer el archivo CSV, puedes utilizar la función open y el módulo csv de Python. Una vez que hayas leído los datos, puedes calcular el total de gastos implementando la lógica que consideres necesaria. """
from os import system

system("clear")
import csv

def read_csv(path):
    with open (path, "r") as csvfile:
        reader = csv.reader(csvfile)
        total = 0
        for row in reader:
            total += int(row[1])
        return total
    
response = read_csv('./8. Practice CSV read/data.csv')
print(response) # 767.0

