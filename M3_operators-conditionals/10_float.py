import os

os.system('clear')
x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x==y) # False

# Primera forma de comparar los flotantes mediante Strings

# 1. Aproximar el valor para cortar las presiciones transformandolo en String

# Para este caso se usaria la función format y designando dos digitos al numero mediante la g acompañada al 2 en este caso

# forma str
y_str = format(y, ".2g")
print('str =>' , y_str)

# Segunda Alternativa

# Evaluando la comparación tambien transformando la x en String

print(y_str == str(x)) # True

# Segunda forma mas matematica

# forma round
y = round(y,1)
print(x == y)


print('*'*10) # Imprimir el separador

print(y, x)
# 1. Designar una tolerancia

tolerence = 0.00001
print(abs(x-y) < tolerence) # La tolerancia seriael valor aproximado

# En la anterior ecuación se esta determinando primero la diferencia de x y y luego se extrae el valor absoluto mediante la palabra reservada abs y por ultimo hallando el margen de error para lograr una comparación 

