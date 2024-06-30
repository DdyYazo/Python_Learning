from os import system

system('clear')

from Producto import Producto
from Orden import Orden

producto1 = Producto('Camisa', 100.00)
producto2 = Producto('Pantalon', 300.00)
producto3 = Producto('Zapatos', 90.00)
producto4 = Producto('Tennis', 70.00)

productos1 = [producto1, producto2]
productos2 = [producto3, producto4]
orden1 = Orden(productos1)
print(orden1)
print()

""" Agregar producto a la orden 1"""
orden1.agregar_producto(producto3)
orden1.agregar_producto(producto4)
print(orden1)
print()
    
""" Nueva orden """
orden2 = Orden(productos2)
print(orden2)
print()