# Declaración de cadenas
name = "Ntcolas"
last_name = "Malina Monroy"
print(name)
print(last_name)

# Concatenación
full_name = (
    name + " " + last_name
)  # Para que la concatenación no se muestre unida se pone " " para representar un espacio vacio
print(full_name)

# Diferenciar entre comillas simples y comillas dobles
quote = "I'm David"
print(quote)
"""en comparación cuando se pone 'I'm David"""

quote2 = 'She said "Hello"'
print(quote2)
"""en comparación cuando se pone "She said "David"""

# String concatenado
nombre_variable = "Hola mi nombre es " + name + "y mi apellido es " + last_name
print("V1 =>" + nombre_variable)

# String con función format
nombre_variable = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
print(nombre_variable)

# String con f -> Abreviatura de format
nombre_variable = f"Hola mi nombre es {name} y mi apellido es {last_name}"
print(nombre_variable)
