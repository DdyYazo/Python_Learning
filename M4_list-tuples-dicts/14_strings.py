import os

os.system("clear")

# metodo in en los String
text = "Ella sabe programar en Python"
"""
print('JavaScript' in text)
print('Python' in text)

if 'JavaScript' in text:
    print('Hiciste la eleccion correcta')
else:
  print('No es la eleccion correcta')
"""

# Metodo len en String para saber el tamaño de un String
size = len(text)
print(size)

# forma directa
# print(len(text))


# Metodo upper en los String para transformar toda la cadena en mayuscula
print(text)
print(text.upper())

# print(text.upper().isupper())

# Metodo lower en los String para transformar toda la cadena en minuscula
print(text.lower())


# Metodo count para saber la cantidad de veces que se repite la letra especificada en el String
print(text.count("a"))

# Metodo swapcase para transformar toda letra en minuscula a Mayuscual en un String
print(text.swapcase())


# Metodo startswith para saber si el String empieza con cierta letra
print(text.startswith("Ella"))

# Metodo endswith para saber si el String termina con cierta letra
print(text.endswith("Rust"))

# Metodo replace para reemplazar una letra en un String por otra
print(text.replace("Python", "Go"))

text_2 = "este es un titulo"

# Metodo capitalize para transformar la primera letra de cada palabra en mayuscula
print(text_2.capitalize())

# Metodo title para transformar la primera letra de cada palabra en mayuscula y lo demas en minuscula
print(text_2.title())

# Funcion isdigit para saber si es un numero o no
print(text_2.isdigit())
print("2122".isdigit())
print("2122a".isdigit())

print(text_2.isalpha())


quote = "I'm David"
print(quote)
