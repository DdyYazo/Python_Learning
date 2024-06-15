import os

os.system("clear")

if True:
    print("Esto siempre se ejecuta")

# Esta condicion no se ejecuta por que siempre es falsa
if False:
    print("Esto no se ejecuta")


# Programa que pregunta al usuario cual es su mascota preferida
pet = input("¿Cual es tu mascota favorita? ")
if pet == "Perro":
    print("Genial tienes un buen gusto")

elif pet == "Gato":
    print("Espero tengas suerte")

elif pet == "Pez":
    print("Es un animal lindo")

else:
    print("Veo que no te agradan las mascotas")
    """
"""
# Aplicando el ejemplo de Stock con la condicional if y la condicional else
stock = int(input("Ingrese el numero de Stock=> "))
if stock >= 100 and stock <= 1000:
    print("El Stock es adecuado")
else:  # Si la condicion resulta ser False entonces imprimira el siguiente mensaje
    print("El Stock es insuficiente")
"""
"""
# Programa que evalua si un numero es par o impar
number = int(input("Ingrese un numero=> "))
if number % 2 == 0:  # Operador modulo % para determinar si el numero es par o impar
    print("El numero es par")
else:
    print("El numero es impar")
