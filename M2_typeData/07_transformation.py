# declarar un string
name = "David"
print(type(name))

# cambiar a flotante
name = 12
print(type(name))

# cambiar a booleano
name = True
print(type(name))

# concatenación  (cuidad el tipo de datos)
print("David" + "Yazo")
print(10 + 12)
print("David" + "12")

# concatenar valores de diferentes tipos de datos
age = 12
print("Mi edad es " + str(age))
# pasar un dato a string o cadena de texto y poderlo utilizarlo en una función

print("Mi edad es", age)

age = input("Escribe tu edad => ")
print(type(age))  # a pesar de ingresar un dato tipo entero se imprimer como string
age = int(age)  # para leerlo como entero se debe declarar como tipo int
age += 10
print(f"Tu edad en 10 años sera {age}")

# ¿que pasaria si se digitara un texto en vez de un valor numerico?
# como se muestra por consola, arrojaria un error de traceback
