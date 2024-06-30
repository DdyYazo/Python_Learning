import random
import os
os.system("clear")

""" Las funciones tambien permiten establecer parametros por defecto y a su vez retornar multiples valores """

## 1. Ejemplo de una funcion con retorno de multiples parametros donde requiere establecer los argumentos
def find_volume(lenth, width, depth): # En este caso se establecen los argumentos
    return lenth*width*depth # Se retorna el resultado de la operacion

result = find_volume(2,3,4) # Se declara la variable result y se le asigna el valor de la funcion find_volume
print(f"El volumen es: {result}") 

## 2. Ejemplo de una función con retorno de multiples parametros por defecto
def find_volume2(length=2, width=3, depth=4): # En este caso se establecen los argumentos por defecto
    return length*width*depth, width, 'hola' # Se retorna el resultado de la operacion
print(f"El volumen es: {find_volume2()}") # En este caso se imprime el resultado de la funcion con los valores por defecto

# 2.1 Si solo se quiere saber el ancho se puede hacer lo siguiente
print(f"El volumen es: {find_volume2(width=5)}") # En este caso se reasigna el valor del width a 5 dando como resultado el volumen de 40

# 2.2 Si se queire retornar mas de una funcion se puede hacer lo siguiente considerando que se declaro su retorno en la funcion
result2, width, saludo = find_volume2() # En este caso se declara las variables result2, width y saludo y se le asigna el valor de la funcion find_volume2
print(f"El volumen es: {result2}") # Se imprime el valor de la variable result2
print(f"El ancho es: {width}") # Se imprime el valor de la variable width
print(f"El saludo es: {saludo}") # Se imprime el valor de la variable saludo