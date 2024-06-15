import os

os.system("clear")
# Operador NOT
print("NOT")
print(not True)
# Retorna False
print(not False)
# Retorna True

# Operador NOT
print("NOT")
print("not True and True =>", not (True and True))
# Retorna False
print("not True and False =>", not (True and False))
# Retorna True
print("not False and True =>", not (False and True))
# Retorna True
print("not False and False =>", not (False and False))
# Retorna True

stock = int(input("Ingrese el numero de Stock=> "))

print(not (stock >= 100 and stock <= 1000))
