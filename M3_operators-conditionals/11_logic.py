import os

os.system("clear")
# operador AND
print("AND")

print("True and True =>", True and True)
print("True and False =>", True and False)
print("False and True =>", False and True)
print("False and False =>", False and False)

# Ejercicio con AND y valores numericos
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

# Ejercicio de Stock a partir de las reglas del negocio

stock = int(input("Ingrese el numero de Stock: "))

print(stock >= 100 and stock <= 10000)
# En este caso si ingresamos 10 retorna False
# Por otro lado si ingresamos 102 retorna True

# Operador OR
print("OR")
print("True or True =>", True or True)
# True
print("True or False =>", True or False)
# True
print("False or True =>", False or True)
# True
print("False or False =>", False or False)
# False

# Ejercicio con OR y valores numericos
print(10 > 5 or 5 < 10)
print(10 > 5 or 5 > 10)

# Ejercicio de usuario segun las reglas del negocio
role = input("Digital el rol=> ")
print(role == "admin" or role == "seller")
# En este caso si ingresamos admin retorna True
# Por otro lado si ingresamos seller retorna True
# Si ingresamos uno distinto a estos retorna False
