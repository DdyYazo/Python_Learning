
<div align="center">

# **Funciones en Python (Las mas utilizadas y sus diferencias)**

<p align="center">
  <img src="https://i.postimg.cc/BvY85nSf/image-1.png" alt="Aquí va el texto del enlace" width="350">
</p>
<p align="center">
<strong>Diferencias entre `List` vs `Tuples` vs `Sets`</strong>
</p>

</div>

# **Tabla de contenido**
- [**Funciones en Python (Las mas utilizadas y sus diferencias)**](#funciones-en-python-las-mas-utilizadas-y-sus-diferencias)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Funciones `def` en Python**](#1-funciones-def-en-python)
  - [1.1. **Definición de Funciones**](#11-definición-de-funciones)
  - [1.2. **Llamada de Funciones**](#12-llamada-de-funciones)
    - [1.2.1. ***Función `def` sin Parámetros***](#121-función-def-sin-parámetros)
    - [1.2.2. ***Función `def` con Parámetros***](#122-función-def-con-parámetros)
  - [1.3. **Diferencia entre `Parámetros` y `Argumentos`**](#13-diferencia-entre-parámetros-y-argumentos)
  - [1.4. **Función `def` dentro de otra función**](#14-función-def-dentro-de-otra-función)
  - [1.5. **Principio DRY**](#15-principio-dry)
- [2. **Funciones con retorno de variables `def.. return`**](#2-funciones-con-retorno-de-variables-def-return)
  - [2.1. **Llamada de Funciones con Retorno**](#21-llamada-de-funciones-con-retorno)
    - [2.2. ***Comprendiendo el uso del `return` mediante un `ciclo for`***](#22-comprendiendo-el-uso-del-return-mediante-un-ciclo-for)
    - [2.3. ***Implementación de una Función `def` para agilizar el caso anterior***](#23-implementación-de-una-función-def-para-agilizar-el-caso-anterior)
  - [2.4. **Implementación de una `Función con retorno`**](#24-implementación-de-una-función-con-retorno)
- [3. **Funciones con retorno de multiples valores y valores por defecto**](#3-funciones-con-retorno-de-multiples-valores-y-valores-por-defecto)
  - [3.1. **Funciones con `Retorno de Múltiples Valores`**](#31-funciones-con-retorno-de-múltiples-valores)
  - [3.2. **Funciones con `parámetros por defecto`**](#32-funciones-con-parámetros-por-defecto)
  - [3.3. **Reasignar un `nuevo argumento a un parametro` especifico**](#33-reasignar-un-nuevo-argumento-a-un-parametro-especifico)
  - [3.4. **Retornar más de una párametro por separado**](#34-retornar-más-de-una-párametro-por-separado)
- [4. **Alcance de variables o `scope` en Python**](#4-alcance-de-variables-o-scope-en-python)
  - [4.1. **Variables Globales (`Fuera del def`)**](#41-variables-globales-fuera-del-def)
  - [4.2. **Variables Locales (`Dentro del def`)**](#42-variables-locales-dentro-del-def)
  - [4.3. **Conversión de Variables `Locales` en `Globales`**](#43-conversión-de-variables-locales-en-globales)
  - [4.4. **Diferencia entre una variable `global` y una variable `local`**](#44-diferencia-entre-una-variable-global-y-una-variable-local)
- [5. **Funciones `lamba` o anónimas**](#5-funciones-lamba-o-anónimas)
  - [5.1. **Sintaxis**](#51-sintaxis)
  - [5.2. **Uso de Funciones Lambda**](#52-uso-de-funciones-lambda)
  - [5.3. **Función declarativa `(def)` vs Función `Lambda`**](#53-función-declarativa-def-vs-función-lambda)
    - [5.3.1. ***Función declarativa***](#531-función-declarativa)
  - [5.3.2. **Función `Lambda`**](#532-función-lambda)
- [6. **HOF `(Higher Order Functions)` implementando Funciones Declarativas `def` y Funciones `lambda` dentro de otras**](#6-hof-higher-order-functions-implementando-funciones-declarativas-def-y-funciones-lambda-dentro-de-otras)
  - [6.1. **Funciones declarativas `def` que reciben como paramatro una función**](#61-funciones-declarativas-def-que-reciben-como-paramatro-una-función)
  - [6.2. **Función que retorna otra función utilizando `Funciones Lambda`**](#62-función-que-retorna-otra-función-utilizando-funciones-lambda)
  - [6.3. **Declarar `Funciones lambdas` directamente al designar los argumentos de una función**](#63-declarar-funciones-lambdas-directamente-al-designar-los-argumentos-de-una-función)
- [7. **Funciones más utilizadas en Python y su comportamiento**](#7-funciones-más-utilizadas-en-python-y-su-comportamiento)
  - [7.1. **Función `map`**](#71-función-map)
    - [7.1.1. ***Sintaxis***](#711-sintaxis)
    - [7.1.2. ***Ejemplo contextual para las función `map` explicado mediante un ciclo for***](#712-ejemplo-contextual-para-las-función-map-explicado-mediante-un-ciclo-for)
    - [7.1.3. ***Utilidad de las Función `map` para un codigo mas legible***](#713-utilidad-de-las-función-map-para-un-codigo-mas-legible)
    - [7.1.4. ***Implementación de la función `map`***](#714-implementación-de-la-función-map)
    - [7.1.5. ***Ejemplo donde se reemplaza los valores iniciales de una lista por los de otra lista***](#715-ejemplo-donde-se-reemplaza-los-valores-iniciales-de-una-lista-por-los-de-otra-lista)
  - [7.1. **Función `map` en diccionarios**](#71-función-map-en-diccionarios)
    - [7.1.6. ***Implementación de función `map` en dictionarios***](#716-implementación-de-función-map-en-dictionarios)
      - [1. **\_Primer caso: Solo imprimir una lista de precios utilizando la `función map` y el `método list`**](#1-_primer-caso-solo-imprimir-una-lista-de-precios-utilizando-la-función-map-y-el-método-list)
      - [2. **\_Segundo caso: Agregar un nuevo campo `taxes` que calcule el impuesto de los precios, lo cual no basta con declararlo en una sola linea sino que se debe definir una función que retorne la operación**](#2-_segundo-caso-agregar-un-nuevo-campo-taxes-que-calcule-el-impuesto-de-los-precios-lo-cual-no-basta-con-declararlo-en-una-sola-linea-sino-que-se-debe-definir-una-función-que-retorne-la-operación)
    - [7.1.7. ***Precauciones a tener en cuenta cuando se implementa `map` en diccionarios, uso de la libreria `copy`***](#717-precauciones-a-tener-en-cuenta-cuando-se-implementa-map-en-diccionarios-uso-de-la-libreria-copy)
      - [**\_Diferencia entre `copy` y `deepcopy` de la libreria `copy`**](#_diferencia-entre-copy-y-deepcopy-de-la-libreria-copy)
    - [7.1.8. ***Alternativa a la libreria `copy` con otra modo mediante la función `map`***](#718-alternativa-a-la-libreria-copy-con-otra-modo-mediante-la-función-map)
  - [7.2. **Función `filter`**](#72-función-filter)
    - [7.2.1. ***Sintaxis de la función `filter`***](#721-sintaxis-de-la-función-filter)
    - [7.2.2. ***Función `filter` en `list`***](#722-función-filter-en-list)
    - [7.2.3. ***Función `filter` en `diccionarios`***](#723-función-filter-en-diccionarios)
  - [7.3. **Función `reduce` y uso de la libreria `functools` con el módulo `reduce`**](#73-función-reduce-y-uso-de-la-libreria-functools-con-el-módulo-reduce)
    - [7.3.1. ***Sintaxis de la función `reduce`***](#731-sintaxis-de-la-función-reduce)
    - [7.3.2. ***Importación de la libreria `functools`***](#732-importación-de-la-libreria-functools)
    - [7.3.3. ***Función `reduce` en `list`***](#733-función-reduce-en-list)
    - [7.3.4. ***Función `reduce` en `diccionarios`***](#734-función-reduce-en-diccionarios)
- [8. **La diferencia entre una función declarativa `def` y una función `lambda` en cuanto a su legibilidad y mantenibilidad**](#8-la-diferencia-entre-una-función-declarativa-def-y-una-función-lambda-en-cuanto-a-su-legibilidad-y-mantenibilidad)
  - [8.1. **En términos de "Mantenibilidad"**](#81-en-términos-de-mantenibilidad)
  - [8.2. **¿Cuándo usar `def` y `lambda`?**](#82-cuándo-usar-def-y-lambda)

# 1. **Funciones `def` en Python**

Son un conjunto de instrucciones que realizan una tarea específica y que pueden ser reutilizadas en cualquier parte del programa.

## 1.1. **Definición de Funciones**
Las funciones se definen con la palabra clave `def`, seguida del nombre de la función y un par de paréntesis que contienen los parámetros. El cuerpo de la función está indentado y contiene las instrucciones que se ejecutarán cuando se llame a la función.

## 1.2. **Llamada de Funciones**

**Se llaman por su nombre**, **seguido de un par de paréntesis que contienen los `argumentos`**.

### 1.2.1. ***Función `def` sin Parámetros***

```python
def saludo(): # Definicion de la funcion
    print("Hola, soy una funcion") # Cuerpo de la funcion
    print("Hola de nuevo, soy una funcion") # Cuerpo de la funcion
saludo() # Output: Hola, soy una funcion
```
### 1.2.2. ***Función `def` con Parámetros***

```python
def suma(number): # Definicion de la funcion
    print(number * 2) # Cuerpo de la funcion
suma(5) # Output: 10
```

## 1.3. **Diferencia entre `Parámetros` y `Argumentos`**

>[!IMPORTANT]
> - **El valor que ingresas cuando llamas la funcion se llama `PARAMETRO`**
> 
> - Mientras que **el valor que usamos dentro de la funcion se llama `ARGUMENTO`**

<p align="center">
  <img src="https://i.postimg.cc/XYV0jZy2/imagen-2024-01-19-185546469.png" alt="Aquí va el texto del enlace" width="400">
<p align="center">
<strong>Forma de llamar una función</strong>
</p>

## 1.4. **Función `def` dentro de otra función**	

```python
def suma(number): # Definicion de la funcion
    print(number * 2) # Cuerpo de la funcion
def suma2(a,b): # Definicion de la funcion
        suma(a+b) # En este caso se llama a la funcion suma() dentro de la funcion suma2()
suma2(5,10) # Ouput: 30
```

## 1.5. **Principio DRY**
> [!IMPORTANT]
>
> Las funciones nos ayudan a cumplir con uno de los principios más importantes de la programación como lo es el principio **DRY (don’t repeat yourself)** o (no te repitas).
> 
> Al tener la lógica en una función evitas tener que escribir la misma lógica una y otra vez, de modo que tienes un código más limpio y más escalable.


# 2. **Funciones con retorno de variables `def.. return`**

Son un conjunto de instrucciones que realizan una tarea específica, **retornan un valor y pueden ser reutilizadas en cualquier parte del programa.**

<p align="center">
  <img src="https://i.postimg.cc/L8K02hnJ/imagen-2024-01-19-202454349.png" alt="Aquí va el texto del enlace">
</p>


## 2.1. **Llamada de Funciones con Retorno**

Las funciones con retorno se definen con la palabra clave `def`, seguida del nombre de la función y un par de paréntesis que contienen los parámetros. El cuerpo de la función está indentado y contiene las instrucciones que se ejecutarán cuando se llame a la función. **Al final del cuerpo de la función, se utiliza la palabra clave `return` para indicar el valor que la función retornará.**

### 2.2. ***Comprendiendo el uso del `return` mediante un `ciclo for`***

```python
sum = 0
for x in range(1,10):
    sum += x
print(sum) # Output: 45
```
- Este codigo imprime la suma de los numeros del 1 al 9, pero **si se quisiera hacer la suma del `1` a `1000` se tendria que modificar el codigo repetidas veces y esto no es eficiente por eso se crean las `funciones con retorno (return)`**

### 2.3. ***Implementación de una Función `def` para agilizar el caso anterior***

```python
def sum_with_range(min,max): # Toma como parametro el minimo y maximo de la suma
    sum = 0 # Initializa la variable sum
    for x in range(min,max): 
        sum += x 
    print(sum)
    
sum_with_range(1,10) # Output: 45  -> 1+..+9
sum_with_range(20,30) # Output: 245 -> 20+..+29
sum_with_range(1,100) # Output: 4950 -> 1+..+99
```

## 2.4. **Implementación de una `Función con retorno`**

```python
def sum_with_range2(min,max): 
    print(f"Entrada de los parametros minimo '{min}' y maximo '{max}' ")
    sum = 0 
    for x in range(min,max):
        sum += x 
    return sum 

result = sum_with_range2(1, 10) # Variable que almacena el resultado de la funcion
print(f"El resultado de la suma de los parametros es: {result}") # Output: El resultado de la suma de los parametros es: 45 

result_2 = sum_with_range2(result, result+10)
print(f"El resultado de la suma de los parametros es: {result_2}") # Output: El resultado de la suma de los parametros es: 100 -> 1+..+9 = 45 + 45+10 = 100
```

- En este caso la función `sum_with_range2` toma como parametro el minimo y maximo de la suma y retorna el resultado de la suma de los parametros ingresados

> [!IMPORTANT]
>
> Luego de establecer la función con retorno **es necesario declarar una variable que almacene el valor de retorno de la funcion de lo contrario no se podra imprimir el resultado de la funcion.**


# 3. **Funciones con retorno de multiples valores y valores por defecto**

## 3.1. **Funciones con `Retorno de Múltiples Valores`** 

**Las funciones pueden retornar múltiples valores o parámetros**, que se pueden almacenar en varias variables.

```python
def find_volume(lenth, width, depth): 
    return lenth*width*depth 

result = find_volume(2,3,4) # Variable que almacena el resultado de la funcion
print(f"El volumen es: {result}") # Output: El volumen es: 24
```

## 3.2. **Funciones con `parámetros por defecto`**

Las funciones pueden tener parámetros con valores por defecto, que **se utilizarán si no se proporciona un argumento para ese parámetro al llamar a la función.**

```python
def find_volume2(length=2, width=3, depth=4): # Se establecen los argumentos por defecto para cada parametro
    return length*width*depth, width, 'hola'
print(f"El volumen es: {find_volume2()}") # Output: El volumen es: 24
```

- En este caso la función `find_volume2` toma como parametro el largo, ancho y profundidad de un objeto y retorna el volumen del objeto, **en este caso se establecen los argumentos por defecto para cada parametro**

## 3.3. **Reasignar un `nuevo argumento a un parametro` especifico**

Reasignar el valor de un parametro especifico en este caso el `width` a 5

```python
def find_volume2(length=2, width=3, depth=4): 
    return length*width*depth, width, 'hola'

print(f"El volumen es: {find_volume2(width=5)}") # Output: El volumen es: 40
```

## 3.4. **Retornar más de una párametro por separado**

```python
def find_volume2(length=2, width=3, depth=4): 
    return length*width*depth, width, 'hola'

result2, width, saludo = find_volume2() # Variables result2, width y saludo y se le asigna el valor de la funcion find_volume2

print(f"El volumen es: {result2}") # Output: El volumen es: 24
print(f"El ancho es: {width}") # Output: El ancho es: 3
print(f"El saludo es: {saludo}") # Output: El saludo es: hola
```

# 4. **Alcance de variables o `scope` en Python**

El scope es la visibilidad de una variable dentro de un programa, es decir, en qué partes del programa se puede acceder a una variable o no.

## 4.1. **Variables Globales (`Fuera del def`)**

Las variables globales **se pueden acceder desde cualquier parte del programa.**

```python
name = "Juan" # Variable global
print(f"El nombre es: {name}") # Output: El nombre es: Juan
```

- En este caso la variable global es `'name'` y se puede acceder a ella desde cualquier parte del programa

## 4.2. **Variables Locales (`Dentro del def`)**

Las variables locales s**olo se pueden acceder desde el bloque de código donde se declararon, generalmente dentro de una función.**

```python

def print_name():
    name = "Luisa" # Variable local
    print(f"El nombre es: {name}")

print_name() # Output: El nombre es: Luisa
```
- En este caso la variable local es `'name'` y solo se puede acceder a ella desde el bloque de código donde se declaró, es decir llamando a la función `print_name()`

## 4.3. **Conversión de Variables `Locales` en `Globales`**

**Una variable local puede convertirse en global utilizando la palabra clave `global`.**

```python
name = "" # Variable global
def print_name():
    global name # Se declara la variable global
    name = "Luisa" # Variable local

print_name() # Se ejecuta la funcion
print(f"El nombre es: {name}") # Output: El nombre es: Luisa

```

- En este caso la variable local `name` se convierte en global utilizando la palabra clave `global` y se puede acceder a ella desde cualquier parte del programa

## 4.4. **Diferencia entre una variable `global` y una variable `local`**

**La variable global se puede acceder desde cualquier parte del programa** mientras que **la variable local solo se puede acceder desde el bloque de codigo donde se declaro mayormente dentro de una funcion**


# 5. **Funciones `lamba` o anónimas**

Las funciones lambda **se definen con la palabra clave `lambda`, seguida de los parámetros y una expresión que constituye el cuerpo de la función.**

## 5.1. **Sintaxis** 

```python
 lambda argumentos: expresion
```

- **`lambda`:** Es la palabra reservada para indicar que es una funcion lambda

- **`argumentos`:** Son los parametros de la funcion, **estos pueden ser uno o varios**

- **`expresion`:** Es el cuerpo de la funcion, es decir, lo que hace la funcion


## 5.2. **Uso de Funciones Lambda**

> [!IMPORTANT]
> 
> Las funciones lambda **son útiles cuando se quiere crear una función que se va a usar una sola vez.**

## 5.3. **Función declarativa `(def)` vs Función `Lambda`**

<p align="center">
  <img src="https://i.postimg.cc/ncpXBkwm/imagen-2024-01-24-171139328.png" alt="Aquí va el texto del enlace" width="300">
</p>

### 5.3.1. ***Función declarativa***


```python
 def increment(n):
    return n + 1

result = increment(10)
print(result)
```

- En este caso la función declarativa `increment` requiere mas lineas de codigo que una función lambda

## 5.3.2. **Función `Lambda`**

```python
## Crear una lambda que devuelve el nombre completo
full_name = lambda first, last: f'The fullname is {first.title()} {last.title()}'

print(full_name('juan', 'perez')) # Output: The fullname is Juan Perez
```

- La sintaxis de la función `lambda` es la misma que la de una funcion `def` pero en este caso se compone por:

  - **`full_name`:** **Es el nombre de la función** lambda
  
  - **`lambda`:** Es la palabra reservada para indicar que es una funcion lambda
  
  - **`first, last`:** **Son los parametros** de la función lambda
  
  - **`f'The fullname is {first.title()} {last.title()}'`:** **Es el cuerpo de la función lambda**, en este caso se retorna el nombre completo de una persona con la primera letra en mayuscula usando la función `title()`




# 6. **HOF `(Higher Order Functions)` implementando Funciones Declarativas `def` y Funciones `lambda` dentro de otras**

**Son funciones que pueden tomar otras funciones como argumentos dentro de los parametros** de lo devolver funciones como resultado.

## 6.1. **Funciones declarativas `def` que reciben como paramatro una función**

```python
def increment(n): # Declara la funcion increment
    return n + 1 

def high_order_function(x, func): # Esta funcion recibe como parametro un numero y una funcion
    return x + func(x) # Retorna el numero ingresado mas el resultado de la funcion que se ingreso como parametro

result = high_order_function(2, increment) 
print(result) # Output: operacion 2 + (2 + 1) = 5
```

- En el caso anterior la función `high_order_function` recibe como parametro un numero y una función y retorna el numero ingresado mas el resultado de la función que se ingreso como parametro llama a la función `increment` que incrementa el numero ingresado en 1

## 6.2. **Función que retorna otra función utilizando `Funciones Lambda`**

```python
increment_V2 = lambda x : x + 1 
high_order_function_V2 = lambda x, func: x + func(x) # 

result = high_order_function_V2(2, increment_V2) # 
print(result) # la salida seria la operacion 2 + (2 + 1) = 5 
```

- En este caso la función `high_order_function_V2` recibe como parametro un numero y una función y retorna el numero ingresado mas el resultado de la función que se ingreso como parametro llama a la función `increment_V2` que incrementa el numero ingresado en 1, generando el mismo resultado que la función declarativa pero en una sola linea

## 6.3. **Declarar `Funciones lambdas` directamente al designar los argumentos de una función**
```python
## Primero es necesario definir la función inicial como lambda
high_order_function_V2 = lambda x, func: x + func(x)
result = high_order_function_V2(2, lambda x: x + 1) # Al declararse la variable permite establecer como parametro una función lambda
print(result) # Output: 5
```

- En este caso la **función lambda** `high_order_function_V2` recibe como parametro un numero y una función y retorna el numero ingresado mas el resultado de la función que se ingreso como parametro. Posteriormente se llama la función en una variable y se le asigna como parametro una función lambda que incrementa el numero ingresado en 1

# 7. **Funciones más utilizadas en Python y su comportamiento**
<p align="center">
  <img src="https://i.postimg.cc/h4sX8YQB/imagen-2024-01-24-181612046.png" alt="Aquí va el texto del enlace">
</p>




## 7.1. **Función `map`**

La función `map` **es una funcion que recibe como parametro una funcion y un iterable y retorna un objeto map** que es un iterador que permite recorrer cada elemento del iterable y aplicarle la funcion que se ingreso como parametro a cada elemento del iterable

### 7.1.1. ***Sintaxis*** 

```python
  map(funcion, iterable)
```

- **`map`:** Es la palabra reservada para indicar que es una funcion map

- **`funcion`:** Es la funcion que se va a aplicar a cada elemento del iterable

- **`iterable`:** Es el objeto que se va a recorrer y aplicar la funcion

### 7.1.2. ***Ejemplo contextual para las función `map` explicado mediante un ciclo for***

```python
numbers = [2, 4, 6, 8, 10]
numbers_plus_one = [] 
for number in numbers: 
    numbers_plus_one.append(number * 2) # método append para agregar un elemento al final de la lista
print(numbers) # Output: [2, 4, 6, 8, 10]
print(numbers_plus_one) # Output: [4, 8, 12, 16, 20]
```

- En este caso se crea una lista con numeros y se recorre la lista `numbers` para ser almacenada en una lista vacia `numbers_plus_one` multiplicando cada numero por 2 mediante un ciclo for y agregandolo al final de la lista con el método `append`

### 7.1.3. ***Utilidad de las Función `map` para un codigo mas legible***

>[!NOTE]
>
> La función map es una de las funciones más utilizadas en Python, ya que permite aplicar una función a cada elemento de un iterable (lista, tupla, etc.) y retornar un iterador para recorrer los resultados y permite reducir el código y hacerlo más legible utilizando ademas funciones lambda.

### 7.1.4. ***Implementación de la función `map`***

- Siguiendo el ejemplo anterior se puede implementar la función `map` para hacer el código más legible y reducir las lineas de código usando una función `lambda`

```python
numbers = [2, 4, 6, 8, 10]

numbersv3 = map(lambda number: number * 2, numbers) 
print(numbersv3) # Output: <map object ></map>
list_numbersv3 = list(numbersv3) 
print(list_numbersv3) # Output: [4, 8, 12, 16, 20]
```

- En este caso se crea una lista con numeros y se crea un `objeto map` que incorpora la funcion `lambda` que multiplica por 2 cada numero de la `lista numbers` y se convierte el `objeto map` en una `lista` **obteniendo el mismo resultado que el `ciclo for` pero en menos lineas de codigo**

### 7.1.5. ***Ejemplo donde se reemplaza los valores iniciales de una lista por los de otra lista*** 

En algunos casos una lista puede tener una longitud de datos mayor que otra para ello el output se tomara de la lista con menor cantidad

```python
list1 = [1, 2, 3, 4, 5]# Se crea una lista con numeros
list2 = [6, 7, 8, 9] # Se crea una lista con numeros
list3 = map(lambda a, b: a + b, list1, list2) # Se crea un objeto map que incorpora la funcion lambda que suma los valores de las dos listas
print(list1) # Output: [1, 2, 3, 4, 5]
print(list2) # Output: [6, 7, 8, 9]
print(list3) # Output: <map object at 0x7f1d9f7d7a90>
list3 = list(list3) # Se convierte el objeto map en una lista
print(list3) # Output: [7, 9, 11, 13] debido a que la lista 2 tiene un elemento menos que la lista 1 el resultado es una lista con 4 elemen
```
- En este caso se crean dos listas de números `list1` y `list2` y se crea un `objeto map` declarada como `list3` que incorpora la funcion `lambda` para sumar los valores de las dos listas y seguidamente se convierte el `objeto map` en una `lista`.

  - Es importante señalar que **el resultado de la lista `list3` es una lista con 4 elementos debido a que `lista2` tiene un elemento menos que `lista1`**


## 7.1. **Función `map` en diccionarios**

La función `map` tambien se puede usar en diccionarios

### 7.1.6. ***Implementación de función `map` en dictionarios***

Para este ejemplo primero **se crea una lista de diccionarios con productos y precios** 

```python
items = [
    {
     'product': 'laptop',
     'price': 800,
     },
    {
        'product': 'mouse',
        'price': 40,
    },
    {
        'product': 'monitor',
        'price': 400,
    }
]
```

#### 1. **_Primer caso: Solo imprimir una lista de precios utilizando la `función map` y el `método list`**

```python
prices = list(map(lambda item: item['price'], items))
print(prices) # Output: [800, 40, 400]
```

- En este caso se crea un `objeto map` que incorpora la función `lambda` que retorna los precios de los productos del diccionario `items` y se convierte el `objeto map` en una `lista` de principio.

#### 2. **_Segundo caso: Agregar un nuevo campo `taxes` que calcule el impuesto de los precios, lo cual no basta con declararlo en una sola linea sino que se debe definir una función que retorne la operación**

```python

def add_taxes(item):
    item['taxes'] = item['price'] * 0.8
    return item

new_item = list(map(add_taxes, items)) 

print(new_item) # Output: [{'product': 'laptop', 'price': 800, 'impuesto': 640.0}, {'product': 'mouse', 'price': 40, 'impuesto': 32.0}, {'product': 'monitor', 'price': 400, 'impuesto': 320.0}]
```

- En este caso se crea una función `add_taxes` que agregue un nuevo campo al diccionario `items` llamado `taxes` que corresponde al calculo del impuesto del campo `price` para posteriormente retornar el nuevo diccionario con el impuesto. 
  
- Posterioemente se crea una función `map` bajo el nombre de `new_item` que incorpora la función `add_taxes` y se convierte el `objeto map` en una `lista` de principio, obteniendo el output del diccionario con el impuesto (`taxes`) de cada producto.	

### 7.1.7. ***Precauciones a tener en cuenta cuando se implementa `map` en diccionarios, uso de la libreria `copy`***

> [!WARNING]
>
> El utilizar estas funciones se debe tener precación debido a:
> 
> - **Puede generar un cambio en el array original lo que puede ocasionar problemas en el codigo o errores de logica**,
> 
> Entonces **para solucionar ello se puede utilizar la biblioteca `copy` para crear una copia del array original y no modificarlo** o otro logica que evite esta excepción.

- Antes de crear la función `map` donde se desea crear un nuevo campo **se puede generar una copia en memoria del array original mediante la *libreria `copy`***

```python
import copy

## Primer modo de crear una copia del array original
items_cp = copy.copy(items)
print(items_cp) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]

## Segundo modo de crear una copia del array original
items_copy = copy.deepcopy(items)
print(items_copy) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]

## Resto del codigo donde se crea la función map
```

En este caso hay dos modos de crear una copia del array original mediante la libreria `copy` que son `copy` y `deepcopy` que permiten crear una copia superficial (copy) y profunda (deepcopy) del array original respectivamente. 

- Para ello se importa la libreria `copy` y se crea una copia del array original `items` en una variable `items_cp` y `items_copy` respectivamente, utilizando estos modulos.

---

**Tambien se puede declarar dentro de la función que establece el nuevo campo `taxes` una copia del array original mediante la libreria `copy` de la siguiente manera**

```python
import copy

items = [
    {
     'product': 'laptop',
     'price': 800,
     },
    {
        'product': 'mouse',
        'price': 40,
    },
    {
        'product': 'monitor',
        'price': 400,
    }
]

def add_taxes(item):
    item = copy.deepcopy(item) # Se crea una copia del array original
    item['taxes'] = item['price'] * 0.19
    return item
  
new_items = list(map(add_taxes, items))
print(new_items) # Output: [{'product': 'laptop', 'price': 800, 'taxes': 152.0}, {'product': 'mouse', 'price': 40, 'taxes': 7.6}, {'product': 'monitor', 'price': 400, 'taxes': 76.0}]

print(items) # Output: [{'product': 'laptop', 'price': 800}, {'product': 'mouse', 'price': 40}, {'product': 'monitor', 'price': 400}]
```

#### **_Diferencia entre `copy` y `deepcopy` de la libreria `copy`**

Con respecto al ejemplo anterior al generar una copia del array original **con `copy` solo crea una copia superficial del array original**, mientras que **`deepcopy` crea una copia profunda del array original, es decir, si el array original tiene un array dentro de otro array entonces deepcopy crea una copia de cada array.**

### 7.1.8. ***Alternativa a la libreria `copy` con otra modo mediante la función `map`***

De otro modo tambien se puede añadir una nueva **clave-valor** sin afectar el array original, directamente en la linea del `map` de la siguiente manera

```python

# --------------- Codigo donde esta declarado laàlista de diccionarios items ----------------

newItems = map(lambda item: {**item, 'tax': item['price'] * .19}, items) 

print(list(newItems)) # Output: [{'product': 'tshirt', 'price': 100, 'tax': 19.0}, {'product': 'pants', 'price': 300, 'tax': 57.0}, {'product': 'blue white pants', 'price': 200, 'tax': 38.0}]
print(items) # Output: [{'product': 'tshirt', 'price': 100}, {'product': 'pants', 'price': 300}, {'product': 'blue white pants', 'price': 200}]
```

- En este caso para no alterar el array original `items` se crea un `objeto map` que incorpora la función `lambda` que desempaqueta el diccionario de `items` y agrega un nuevo campo llamado `tax` que es el impuesto del producto mediante una expresión `**[NombreDeLaVaria]` que en este caso es `item`, de esta manera se obtiene el mismo resultado que el ejemplo anterior pero haciendo uso de una sola linea de código.


## 7.2. **Función `filter`**

La función `filter` **es una función que recibe como parametro una función y un iterable y retorna un objeto filter** Esta función permite filtrar los elementos de un iterable que cumplan con una condición.

### 7.2.1. ***Sintaxis de la función `filter`*** 

```python
filter(función, iterable)
```

- **`función`:** Es la función que se va a aplicar a cada elemento del iterable

- **`iterable`:** Es el objeto que se va a recorrer y aplicar la función

### 7.2.2. ***Función `filter` en `list`***

 ```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # 
print(even_numbers) # output: [2, 4, 6, 8, 10]
print(numbers) # output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]```
```
- En este caso se crea una lista de números `numbers` y se crea un `objeto filter` que incorpora la función `lambda` la cual retorna los números pares de la lista `numbers` y se convierte el `objeto filter` en una `lista` de principio.

### 7.2.3. ***Función `filter` en `diccionarios`***

 ```python
matches = [
  {
    'home_team': 'Bolivia',
    'away_team': 'Uruguay',
    'home_team_score': 3,
    'away_team_score': 1,
    'home_team_result': 'Win'
  },
  {
    'home_team': 'Brazil',
    'away_team': 'Mexico',
    'home_team_score': 1,
    'away_team_score': 1,
    'home_team_result': 'Draw'
  },
  {
    'home_team': 'Ecuador',
    'away_team': 'Venezuela',
    'home_team_score': 5,
    'away_team_score': 0,
    'home_team_result': 'Win'
  },
] 
print(f'Lista original: {matches} ') # Output: Lista original: [{'home_team': 'Bolivia', 'away_team': 'Uruguay', 'home_team_score': 3, 'away_team_score': 1, 'home_team_result': 'Win'}, {'home_team': 'Brazil', 'away_team': 'Mexico', 'home_team_score': 1, 'away_team_score': 1, 'home_team_result': 'Draw'}, {'home_team': 'Ecuador', 'away_team': 'Venezuela', 'home_team_score': 5, 'away_team_score': 0, 'home_team_result': 'Win'}]
print(len(matches)) # Output: 3
print('\n')
## Ahora se desea filtrar una lista con solo los partidos que ganó el equipo local
new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(f'Lista nueva: {new_list}') 
print(len(new_list)) # Output: 2
```
- En este caso se crea una lista de diccionarios `matches` que muestra los resultados de los partidos de futbol y se crea un `objeto filter` que incorpora la función `lambda` la cual retorna los partidos mediante el campo `home_team_result` que sean `Win` de la lista `matches` y se convierte el `objeto filter` en una `lista` de principio.

## 7.3. **Función `reduce` y uso de la libreria `functools` con el módulo `reduce`**

La función `reduce` **es una función que recibe como parametro una función y un iterable y retorna un solo valor**. Esta función permite reducir una lista a un solo valor aplicando una función a cada elemento de la lista.


### 7.3.1. ***Sintaxis de la función `reduce`***

```python
reduce(función, iterable)
```

- **`función`:** Es la función que se va a aplicar a cada elemento del iterable.

- **`iterable`:** Es el objeto que se va a recorrer y aplicar la función sea una lista o diccionario.


### 7.3.2. ***Importación de la libreria `functools`***

La función reduce no está disponible por defecto en Python, por lo que es necesario importarla desde el módulo `functools` de la siguiente manera

```python
import functools
```

### 7.3.3. ***Función `reduce` en `list`***

En este caso se utiliza la función `reduce` con una función `lambda` para sumar todos los números en la lista.

```python

import functools

numbers = [1, 2, 3, 4, 5]

result = functools.reduce(lambda counter, item: counter + item, numbers)

print(result) # Output: 15
```

- En este caso se crea una lista de números `numbers` y se crea un `objeto reduce` que incorpora la función `lambda` la cual suma todos los números de la lista `numbers` y se convierte el `objeto reduce` en un solo valor de principio.

### 7.3.4. ***Función `reduce` en `diccionarios`***

```python

import functools

matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'
    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'
    },
]

# Utilizamos reduce con una función lambda para sumar los goles de los partidos de fútbol
total_goals = functools.reduce(lambda counter, item: counter + item['home_team_score'] + item['away_team_score'], matches, 0) # El 0 es el valor inicial de la variable counter
****
# Imprimimos el resultado
print(total_goals) # Output: 11 ya que la suma de los goles de los partidos de futbol es 11
```

- En este caso se crea una lista de diccionarios `matches` que muestra los resultados de los partidos de futbol y se crea un `objeto reduce` que incorpora la función `lambda` la cual suma los goles de los partidos de futbol de la lista `matches` a partir de los campos `home_team_score` y `away_team_score` dando como resultado un solo valor.
  
  - **El valor de counter corresponde al número inicializado en `0`** que se indica al final de la función `reduce`

# 8. **La diferencia entre una función declarativa `def` y una función `lambda` en cuanto a su legibilidad y mantenibilidad**

- **`def`:** Se utiliza para definir funciones normales. 
  - Pueden tener cualquier número de argumentos y cualquier cantidad de código dentro de ellas. 
  - También pueden tener un nombre, lo que **permite reutilizarlas en diferentes partes del código.**

- **`lambda`:** **Se utiliza para definir funciones anónimas pequeñas.** 
  - Estas funciones son de una sola línea y no tienen un nombre. 
  - Son útiles cuando necesitas una función pequeña para una operación única, como pasarla como argumento a funciones como `map()`, `filter()`, etc.


## 8.1. **En términos de "Mantenibilidad"**

- **Las funciones `def`**
  
  - Son **más fáciles de leer y mantener, especialmente para funciones más largas y complejas.** 
  
  - Pueden tener un nombre, lo que facilita la comprensión de su propósito. **También pueden tener documentación a través de `docStrings`.**

- **Las funciones `lambda`** 
  - Son útiles para operaciones simples y de una sola línea, pero **pueden ser difíciles de leer y mantener si se utilizan para operaciones más complejas.**
  - **No pueden tener un nombre ni `docStrings`**, lo que puede hacer que sea más difícil entender su propósito.

## 8.2. **¿Cuándo usar `def` y `lambda`?**

Si estás escribiendo una función más larga y compleja que **se utilizará en varias partes de tu código, probablemente deberías usar `def`.**
 
 Por otro lado, **si solo necesitas una función simple para una operación única, `lambda` puede ser una buena opción.**