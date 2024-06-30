import random
import os
os.system("clear")

""" Las funciones tambien retornan valores """
""" Sintaixs de una funcion con retorno """
""" def nombreFuncion(parametros):
return valor
donde:
    nombreFuncion: es el nombre de la funcion
    parametros: son los parametros que recibe la funcion, estos son opcionales
    return: es la palabra reservada que indica que la funcion retornara un valor
    valor: es el valor que retornara la funcion """
    
### Ejemplo para enterder como funcion mediante un ciclo for
sum = 0
for x in range(1,10):
    sum += x
print(sum) # Este codigo imprime la suma de los numeros del 1 al 9 sin embargo si se quiere hacer la suma de los numeros del 1 al 1000 se tendria que modificar el codigo repetidas veces y esto no es eficiente por eso se crean las funciones con retorno

## Ejemplo de una función implementando el codigo anterior
def sum_with_range(min,max): # Definicion de la funcion
    sum = 0 # Variable que almacena la suma de los numeros
    for x in range(min,max): # Ciclo for que recorre los numeros del 1 al 1000
        sum += x # Esta linea suma los numeros del 1 al 1000
    print(sum)
    
sum_with_range(1,10) # En este caso el resultado seria 10 porque se suman los numeros del 1 al 9 como factorial
sum_with_range(20,30) # Este codigo imprime la suma de los numeros del 20 al 29
sum_with_range(1,100) # Este codigo imprime la suma de los numeros del 1 al 99

## Ejemplo de una función con retorno del codigo anterior
def sum_with_range2(min,max): # Definicion de la funcion
    print(f"Entrada de los parametros minimo '{min}' y maximo '{max}' ")
    sum = 0 # Variable que almacena la suma de los numeros
    for x in range(min,max): # Ciclo for que recorre los numeros del 1 al 1000
        sum += x # Esta linea suma los numeros del 1 al 1000
    return sum # Esta linea retorna el valor de la suma

# Luego de esto es necesario declarar una variable que almacene el valor de retorno de la funcion de lo contrario no se podra imprimir el resultado de la funcion

result = sum_with_range2(1,10) # Se declara una variable que almacena el valor de retorno de la funcion
print(f"El resultado de la suma de los parametros es: {result}")

result_2 = sum_with_range2(result,result+10)
print(f"El resultado de la suma de los parametros es: {result_2}")