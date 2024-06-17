from os import system

system("clear")


""" Tu reto es utilizar el concepto de módulos de Python para retornar la suma total de todas las órdenes de compra. Para resolver el ejercicio, debes trabajar en el archivo main.py, donde se encuentra la función get_total. Esta función recibe como parámetro la lista de órdenes de compra.

Debes retornar la suma total de todas las órdenes haciendo uso de las funciones definidas en el archivo my_functions.py.my_functions.py.
"""
import my_functions as ut

def get_total(orders):
  totals = ut.calc_total(ut.get_totals(orders)) # Se llama a la función calc_total del módulo my_functions.py y se le pasa como argumento el resultado de la función get_totals del módulo my_functions.py
  return totals

orders = [
  {
    "customer_name": "Nicolas",
    "total": 100,
    "delivered": True,
  },
  {
    "customer_name": "Zulema",
    "total": 120,
    "delivered": False,
  },
  {
    "customer_name": "Santiago",
    "total": 20,
    "delivered": False,
  }
]

total = get_total(orders)
print(total)