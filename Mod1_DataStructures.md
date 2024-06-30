
<div align="center">

# **Estructuras de datos (`sets`, `listas`, `diccionarios`) y funciones con comprehension**


<p align="center">
  <img src="https://i.postimg.cc/xCMNj95T/imagen-2024-06-14-175959797.png" alt="Aquí va el texto del enlace" width="500">
</p>


</div>

# **Tabla de contenido**
- [**Estructuras de datos (`sets`, `listas`, `diccionarios`) y funciones con comprehension**](#estructuras-de-datos-sets-listas-diccionarios-y-funciones-con-comprehension)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Conjuntos `(sets)`**](#1-conjuntos-sets)
  - [1.1. **Creación y manipulación de `sets` en Python**](#11-creación-y-manipulación-de-sets-en-python)
  - [1.2. **Características de los `sets` en Python**](#12-características-de-los-sets-en-python)
  - [1.3. **Estructuras de datos transformadas a `sets`**](#13-estructuras-de-datos-transformadas-a-sets)
    - [1.3.1. *Ejemplo de transformación de una cadena (`string`) a un conjunto (`set`)*](#131-ejemplo-de-transformación-de-una-cadena-string-a-un-conjunto-set)
    - [1.3.2. *Ejemplo de transformación de una `tupla` a un conjunto (`set`)*](#132-ejemplo-de-transformación-de-una-tupla-a-un-conjunto-set)
    - [1.3.3. *Ejemplo de transformación de una `lista` a un conjunto (`set`)*](#133-ejemplo-de-transformación-de-una-lista-a-un-conjunto-set)
  - [1.4. **Transformación de `(sets)` a estructuras como `(list)`**](#14-transformación-de-sets-a-estructuras-como-list)
  - [**Y mas usos que se verán en los siguientes subtemas.**](#y-mas-usos-que-se-verán-en-los-siguientes-subtemas)
  - [1.5. **Operaciones `CRUD` en `sets` de Python**](#15-operaciones-crud-en-sets-de-python)
    - [1.5.1. *Crear (`Create`)*](#151-crear-create)
    - [1.5.2. *Leer (`Read`)*](#152-leer-read)
    - [1.5.3. *Actualizar (`Update`)*](#153-actualizar-update)
    - [1.5.4. *Eliminar (`Delete`)*](#154-eliminar-delete)
    - [1.5.5. *Limpiar (`Clear`)*](#155-limpiar-clear)
  - [1.6. **`Operaciones de conjuntos` en `sets` de Python**](#16-operaciones-de-conjuntos-en-sets-de-python)
    - [1.6.1. *Unión (`union`)*](#161-unión-union)
    - [1.6.2. *Intersección (`intersection`)*](#162-intersección-intersection)
    - [1.6.3. *Diferencia (`difference`)*](#163-diferencia-difference)
    - [1.6.4. *Diferencia simétrica (`symmetric_difference`)*](#164-diferencia-simétrica-symmetric_difference)
    - [1.6.5. *Subconjunto (`issubset`)*](#165-subconjunto-issubset)
    - [1.6.6. *Superconjunto (`issuperset`)*](#166-superconjunto-issuperset)
- [2. **`list comprenhention` y `dictionary comprenhention`**](#2-list-comprenhention-y-dictionary-comprenhention)
  - [2.1. **`list comprenhention` en Python**](#21-list-comprenhention-en-python)
    - [2.1.1. *Sintaxis de `list comprenhention`*](#211-sintaxis-de-list-comprenhention)
    - [2.1.2. *Ejemplos de una `list` sin comprensión y con comprensión*](#212-ejemplos-de-una-list-sin-comprensión-y-con-comprensión)
    - [2.1.3. *Uso de condicionales con y sin `list comprenhention`*](#213-uso-de-condicionales-con-y-sin-list-comprenhention)
      - [2.1.3.1. **Sintaxis de `list comprenhention` con condicionales**](#2131-sintaxis-de-list-comprenhention-con-condicionales)
      - [2.1.3.2. **Ejemplos de una `list` con condición sin comprensión y con comprensión**](#2132-ejemplos-de-una-list-con-condición-sin-comprensión-y-con-comprensión)
  - [2.2. **`dictionary comprenhention` en Python**](#22-dictionary-comprenhention-en-python)
    - [2.2.1. *Sintaxis de `dictionary comprenhention`*](#221-sintaxis-de-dictionary-comprenhention)
    - [2.2.2. *Ejemplo de un diccionario (`dict`) sin y con comprensión*](#222-ejemplo-de-un-diccionario-dict-sin-y-con-comprensión)
    - [2.2.3. *Ejemplo de un diccionario (`dict`) sin y con comprensión a partir de una `lista`*](#223-ejemplo-de-un-diccionario-dict-sin-y-con-comprensión-a-partir-de-una-lista)
    - [2.2.4. *`dictionary comprenhention` a partir de dos listas **haciendo uso de la función `zip` y `len`***](#224-dictionary-comprenhention-a-partir-de-dos-listas-haciendo-uso-de-la-función-zip-y-len)
      - [2.2.4.1. **\_Primera forma: Uso de la función `zip` para crear un diccionario a partir de dos listas**](#2241-_primera-forma-uso-de-la-función-zip-para-crear-un-diccionario-a-partir-de-dos-listas)
      - [2.2.4.2. **\_Segunda forma: Uso de la función `len` para crear un diccionario a partir de dos listas**](#2242-_segunda-forma-uso-de-la-función-len-para-crear-un-diccionario-a-partir-de-dos-listas)
    - [2.2.5. *Uso de condicionales con y sin `dictionary comprenhention`*](#225-uso-de-condicionales-con-y-sin-dictionary-comprenhention)
      - [2.2.5.1. **Sintaxis de `dictionary comprenhention` con condicionales**](#2251-sintaxis-de-dictionary-comprenhention-con-condicionales)
      - [2.2.5.2. **Ejemplo de un `dictionary` con condición sin comprensión y con comprensión**](#2252-ejemplo-de-un-dictionary-con-condición-sin-comprensión-y-con-comprensión)
      - [2.2.5.. **Ejemplo de un `dictionary comprenhention` con condición a partir de un Texto**](#225-ejemplo-de-un-dictionary-comprenhention-con-condición-a-partir-de-un-texto)
  - [Diferencias entre `List` vs `Tuples` vs `Sets`](#diferencias-entre-list-vs-tuples-vs-sets)


# 1. **Conjuntos `(sets)`**

## 1.1. **Creación y manipulación de `sets` en Python**

Los conjuntos en Python **son estructuras de datos que representan una colección de elementos únicos en un orden no garantizado**. Se definen de manera **similar a las listas y las tuplas, pero en lugar de usar corchetes `[]` o paréntesis `()`, se usan llaves `{}`**. 

## 1.2. **Características de los `sets` en Python**

1. **`Únicos`**: Los conjuntos automáticamente eliminan los duplicados.
   
2. **`Desordenados`**: Los conjuntos no mantienen un orden de los elementos.
   
3. **`Inmutables`**: Los elementos dentro de un conjunto deben ser de un tipo de dato inmutable, como números, cadenas y tuplas.

4. **`Mutables`**: Aunque los elementos dentro del conjunto son inmutables, el conjunto en sí es mutable. Podemos agregar o eliminar elementos de él.

5. **`No soportan indexación`**: Debido a que los conjuntos son desordenados, no puedes acceder a los elementos de un conjunto por un índice.

## 1.3. **Estructuras de datos transformadas a `sets`**

Los `sets` en Python **también pueden ser creados a partir de otras estructuras de datos como cadenas (`strings`), `tuplas` o `listas`**

### 1.3.1. *Ejemplo de transformación de una cadena (`string`) a un conjunto (`set`)*

- Se crea un `set` a partir de la cadena **"HolaaaMundo"**. El conjunto resultante contiene cada carácter único de la cadena. **Los caracteres duplicados, como las tres `'a'`, se eliminan en el conjunto resultante.**

```python
# Crear un conjunto a partir de una cadena

cadena = "HolaaaMundo"
conjunto_cadena = set(cadena)
print(conjunto_cadena)  # Output: {'a', 'd', 'H', 'l', 'n', 'o', 'M', 'u'}
```

### 1.3.2. *Ejemplo de transformación de una `tupla` a un conjunto (`set`)*

- Se crea un conjunto a partir de la tupla `('abc', 'cbv', 'as','abc')`. El conjunto resultante contiene cada elemento único de la tupla. **Los elementos duplicados, como `'abc'`, se eliminan en el conjunto resultante.**

```python
# Crear un conjunto a partir de una tupla
tupla = ('abc', 'cbv', 'as','abc')
conjunto_tupla = set(tupla)
print(conjunto_tupla)  # Output: {'as', 'abc', 'cbv'}
```

### 1.3.3. *Ejemplo de transformación de una `lista` a un conjunto (`set`)*

- Además, se puede crear un conjunto a partir de una `lista`. **Cuando se crea un conjunto a partir de una lista, el conjunto contiene los elementos únicos de la lista.** Los elementos duplicados se eliminan en el conjunto resultante.

```python
# Crear un conjunto a partir de una lista
lista = ['manzana', 'banana', 'cereza', 'manzana', 'cereza']
conjunto_lista = set(lista)
print(conjunto_lista)  # Output: {'manzana', 'banana', 'cereza'}
```
## 1.4. **Transformación de `(sets)` a estructuras como `(list)`** 

Los conjuntos en Python pueden ser convertidos de nuevo a listas. 
> [!NOTE]
>
> Esto es útil cuando necesitas restaurar el orden de los elementos, **ya que los conjuntos no mantienen un orden específico.** 

Para convertir un `set` a una `lista`, se puede usar la función `list()`.

```python
# Tomando de base el output del set anterior: {'manzana', 'banana', 'cereza'}

# Convertir el conjunto a una lista con el mismo output
lista = list(lista)
print(lista)  # Output: ['manzana', 'banana', 'cereza']
```

> [!TIP]
>
> Algunos usos practicos de los conjuntos en Python son:
> - **Eliminar duplicados de una lista**
> - **Comprobar si un elemento existe en un conjunto.**
> - **Comprobar si un conjunto es un subconjunto o superconjunto de otro.**

**Y mas usos que se verán en los siguientes subtemas.**
---


## 1.5. **Operaciones `CRUD` en `sets` de Python**

En Python, los conjuntos permiten realizar operaciones CRUD (`Create`, `Read`, `Update`, `Delete`). 

### 1.5.1. *Crear (`Create`)*

Se puede crear un conjunto usando llaves `{}` o la función `set()`. Cada elemento debe ser único.

```python
# Crear un conjunto con tres elementos
conjunto = {'manzana', 'banana', 'cereza'}
```

### 1.5.2. *Leer (`Read`)* 

Para leer un conjunto, **se puede iterar sobre él usando un bucle `for`**. También se puede comprobar si un elemento existe en un conjunto usando la palabra clave `in`.
```python
# Leer e imprimir cada elemento del conjunto
conjunto = {'manzana', 'banana', 'cereza'}

for fruta in conjunto:
    print(fruta) # Output: manzana, banana, cereza

# Comprobar si un elemento existe en el conjunto
print('manzana' in conjunto)

# Del mismo modo saber el tamaño
size = len(conjunto)
```
### 1.5.3. *Actualizar (`Update`)*

Se puede **agregar un elemento a un conjunto usando el método `add()`**.
- **Para agregar varios elementos, se usa el método `update()`**.

```python
conjunto = {'manzana', 'banana', 'cereza'}

# Agregar un elemento al conjunto
conjunto.add('naranja')
print(conjunto)  # Output: {'manzana', 'banana', 'cereza', 'naranja'}

# Agregar varios elementos al conjunto
conjunto.update(['kiwi', 'mango'])
print(conjunto)  # Output: {'manzana', 'banana', 'cereza', 'naranja', 'kiwi', 'mango'}
```

### 1.5.4. *Eliminar (`Delete`)*

Se puede **eliminar un elemento de un conjunto usando los métodos `remove()` o` discard()`**. 
- La diferencia es que **` remove()` lanzará un error si el elemento no existe, mientras que `discard()` no**.

```python
conjunto = {'manzana', 'banana', 'cereza'}

# Eliminar un elemento del conjunto
conjunto.remove('kiwi')
print(conjunto)  # Output: Error

# Intentar eliminar un elemento que puede no estar en el conjunto
conjunto.discard('kiwi')
print(conjunto)  # Output: {'manzana', 'banana', 'cereza'}
```

### 1.5.5. *Limpiar (`Clear`)*

Tambien se pueden **eliminar todos los elementos de un conjunto usando el método `clear()`**.

```python
conjunto = {'manzana', 'banana', 'cereza'}

# Limpiar un conjunto
conjunto.clear()
print(conjunto)  # Output: set()
```
---


## 1.6. **`Operaciones de conjuntos` en `sets` de Python**

### 1.6.1. *Unión (`union`)*

La unión de dos conjuntos es un nuevo conjunto que contiene **todos los elementos que están en al menos uno de los dos conjuntos.** 
- **En Python, se puede usar el método `union()` o el operador `|` para obtener la unión de dos conjuntos.**

```python
# Crear dos conjuntos
setCountriesA = {'USA', 'Canada', 'Mexico'}
setCountriesB = {'UK', 'France', 'Germany'}

# Unión de conjuntos
unionSet = setCountriesA.union(setCountriesB)
print(unionSet)  # Output: {'USA', 'Canada', 'Mexico', 'UK', 'France', 'Germany'}

# Usando el operador |
unionSet = setCountriesA | setCountriesB
print(unionSet)  # Output: {'USA', 'Canada', 'Mexico', 'UK', 'France', 'Germany'}
```

### 1.6.2. *Intersección (`intersection`)*

La intersección de dos conjuntos es un nuevo conjunto que contiene **todos los elementos que están en ambos conjuntos**. 
- **En Python, se puede usar el método `intersection()` o el operador `&` para obtener la intersección de dos conjuntos.**

```python
# Crear dos conjuntos
setCountriesA = {'USA', 'Canada', 'Mexico'}
setCountriesB = {'UK', 'France', 'Germany'}

# Intersección de conjuntos
intersectionSet = setCountriesA.intersection(setCountriesB)
print(intersectionSet)  # Output: set()

# Usando el operador &
intersectionSet = setCountriesA & setCountriesB
print(intersectionSet)  # Output: set()
```

### 1.6.3. *Diferencia (`difference`)*

La diferencia de dos conjuntos es un nuevo conjunto que contiene **todos los elementos que están en el primer conjunto pero no en el segundo.**
- **En Python, se puede usar el método `difference()` o el operador `-` para obtener la diferencia de dos conjuntos.**
```python
# Crear dos conjuntos
setCountriesA = {'USA', 'Canada', 'Mexico'}
setCountriesB = {'UK', 'France', 'Germany'}

# Diferencia de conjuntos
differenceSet = setCountriesA.difference(setCountriesB)
print(differenceSet)  # Output: {'USA', 'Canada', 'Mexico'}

# Usando el operador -
differenceSet = setCountriesA - setCountriesB
print(differenceSet)  # Output: {'USA', 'Canada', 'Mexico'}
```

### 1.6.4. *Diferencia simétrica (`symmetric_difference`)*

La diferencia simétrica de dos conjuntos es un nuevo conjunto que contiene **todos los elementos que están en uno de los conjuntos, pero no en ambos.** 
- En Python, se puede usar el método `symmetric_difference()` o el operador `^` para obtener la diferencia simétrica de dos conjuntos.
```python
# Crear dos conjuntos
setCountriesA = {'USA', 'Canada', 'Mexico'}
setCountriesB = {'UK', 'France', 'Germany'}

# Diferencia simétrica de conjuntos
symDifferenceSet = setCountriesA.symmetric_difference(setCountriesB)
print(symDifferenceSet)  # Output: {'USA', 'Canada', 'Mexico', 'UK', 'France', 'Germany'}

# Usa el operador ^
symDifferenceSet = setCountriesA ^ setCountriesB
print(symDifferenceSet)  # Output: {'USA', 'Canada', 'Mexico', 'UK', 'France', 'Germany'}
```

### 1.6.5. *Subconjunto (`issubset`)*

Un conjunto es un subconjunto de otro si **todos sus elementos también están en el otro conjunto.** 
- **En Python, puedes usar el método `issubset()` para comprobar si un conjunto es un subconjunto de otro.**

```python
# Crear dos conjuntos
setCountriesA = {'USA', 'Canada', 'Mexico'}
setCountriesB = {'UK', 'France', 'Germany'}

# Comprobar si un conjunto es un subconjunto de otro
isSubset = setCountriesA.issubset(setCountriesB)
print(isSubset)  # Output: False
```

### 1.6.6. *Superconjunto (`issuperset`)*

Un conjunto es **un superconjunto de otro si contiene todos los elementos del otro conjunto.**
- En Python, puedes usar el método `issuperset()` para comprobar si un conjunto es un superconjunto de otro.

```python
# Crear dos conjuntos
setCountriesA = {'USA', 'Canada', 'Mexico'}
setCountriesB = {'UK', 'France', 'Germany'}

# Comprobar si un conjunto es un superconjunto de otro
isSuperset = setCountriesA.issuperset(setCountriesB)
print(isSuperset)  # Output: False
```
---



# 2. **`list comprenhention` y `dictionary comprenhention`**

## 2.1. **`list comprenhention` en Python**

Es una característica que permite crear y transformar listas de una manera concisa y legible.

### 2.1.1. *Sintaxis de `list comprenhention`* 
La sintaxis es muy similar a la de los conjuntos, pero en lugar de usar llaves, se usan corchetes.

```python
[element for element in iterable]
```
- **`element`**: Es la variable que se va a agregar a la lista
- **`iterable`**: **Es una colección de elementos como una `list`, un `set`, una `tupla`, etc.**

### 2.1.2. *Ejemplos de una `list` sin comprensión y con comprensión*

**LISTA SIN COMPRENSIÓN**

```python
# Forma habitual de un ciclo 
numbers = []
for element in range(1, 11):
    numbers.append(element*2)
print(numbers) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
- Este código **crea una `lista de números` del `1` al `10`, cada uno multiplicado por `2`, sin utilizar la comprensión de listas.**

**LISTA CON COMPRENSIÓN**

```python
# Forma con la aplicación de la comprensión
numbers_Com = [element*2 for element in range(1, 11)]
print(numbers_Com) # Output: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
```
- Como se puede ver, **el código es más conciso y legible** al usar la comprensión de listas obteniendo el mismo resultado.

### 2.1.3. *Uso de condicionales con y sin `list comprenhention`*

Tambien es posible agregar condicionales a la lista de comprensión siguiendo la siguiente sintaxis:

#### 2.1.3.1. **Sintaxis de `list comprenhention` con condicionales**

```python
[element for element in iterable if condition]
```
- **`element`**: Es la variable que se va a agregar a la lista
- **`iterable`**: **Es una colección de elementos como una `list`, un `set`, una `tupla`, etc.**
- **`condition`**: Es una condición que se debe cumplir para agregar el elemento a la `lista`

#### 2.1.3.2. **Ejemplos de una `list` con condición sin comprensión y con comprensión**

Empleando el mismo ejemplo de la lista anterior, se puede **agregar una condición para que solo se agreguen los números pares**:

**LISTA CON CONDICIÓN SIN COMPRENSIÓN**
```python
# Forma habitual de un ciclo
for i in range(1, 11):
    if i % 2 == 0: # La condición es que el numero sea par
        numbersCon.append(i*2) # Y cada número agregado a la lista se multiplica por 2
print(numbersCon) # Output: [4, 8, 12, 16, 20]
```
**LIST COMPRENSIÓN CON CONDICIÓN**

Ahora se puede reducir el código anterior empleando la comprensión de listas:

```python
# Forma con la aplicación de la comprensión
numbers_V3 = [i*2 for i in range(1, 11) if i % 2 == 0] 
print(numbers_V3) # Output: [4, 8, 12, 16, 20]
```
- **Al aplicar la comprensión de listas en una sola línea, el código es más conciso y legible.**


## 2.2. **`dictionary comprenhention` en Python**

La **comprensión de diccionarios es una forma concisa de crear diccionarios a partir de estructuras de datos existentes.**

### 2.2.1. *Sintaxis de `dictionary comprenhention`*

Al igual que las `listas` **los `diccionarios` tambien permite implementear comprensiones**

```python
 {key: value for value in iterable} 
```

- **`key`**: Es el nombre de la llave.
- **`value`**: Es el valor de la llave.
- **`iterable`**: Es el iterable que se va a recorrer.

### 2.2.2. *Ejemplo de un diccionario (`dict`) sin y con comprensión*

- En el siguiente ejemplo se muestra cómo se puede usar la comprensión de diccionarios para crear un nuevo diccionario que contenga solo los pares clave-valor de un diccionario existente.

**DICCIONARIO SIN COMPRENSIÓN**

```python
dict1 = {}
for i in range(1, 5):
    dict1[i] = i+3 # Se incrementa el valor de la clave en 3

print(dict1) # Output: {1: 4, 2: 5, 3: 6, 4: 7}
```

- **En este caso, se crea un diccionario con claves del `1` al `4`, donde cada valor es el número de la clave más `3`.**

**DICCIONARIO SIN COMPRENSIÓN**

```python
dict2 = {i: i+3 for i in range(1, 5)} # En este se emplea la sintaxis de un diccionario con comprension
print(dict2) # Output: {1: 4, 2: 5, 3: 6, 4: 7}
```

- **Al aplicar la comprensión de diccionarios, reduce significativamente la cantidad de código y hace que sea más fácil de leer.**

### 2.2.3. *Ejemplo de un diccionario (`dict`) sin y con comprensión a partir de una `lista`*

- En el siguiente ejemplo se tiene una lista de países y se desea crear un diccionario donde cada país tenga una población aleatoria entre `1` y `100`.

**DICCIONARIO SIN COMPRENSIÓN**

```python
import random
countries = ["MX", "COL", "ARG", "USA"]
population = {}
for country in countries:
    population[country] = random.randint(1, 100) # Se genera un numero aleatorio entre 1 y 100 para cada pais
print(population) # Output: {'MX': 18, 'COL': 25, 'ARG': 30, 'USA': 40}
```

**DICCIONARIO CON COMPRENSIÓN**

```python
import random
countries = ["MX", "COL", "ARG", "USA"]
population_v2 = {country: random.randint(1, 100) for country in countries} # En este se emplea la sintaxis de un diccionario con comprension
print(population_v2) # Output: {'MX': 18, 'COL': 25, 'ARG': 30, 'USA': 40}
```

- **Como se puede visualizar, se obtiene el mismo resultado con menos líneas de código y de manera más legible.**

###  2.2.4. *`dictionary comprenhention` a partir de dos listas **haciendo uso de la función `zip` y `len`***

#### 2.2.4.1. **_Primera forma: Uso de la función `zip` para crear un diccionario a partir de dos listas**
   
La función `zip` permite combinar dos listas en un diccionario en este caso, algo similar a `UNION` en SQL.

En el siguiente ejemplo, se tienen dos listas: **una con nombres (`names`)** y **otra con edades (`ages`)**. 
- Se desea crear un diccionario donde **las claves sean los `names`** y **los valores sean las `ages`** correspondientes.

```python

# Se crean dos listas: una con nombres y otra con edades
names = ["Juan", "Maria", "Pedro", "Luisa"]
ages = [18, 25, 30, 40, 50]

## 1. List: Se utiliza la función zip para unir las dos listas convirtiendolas principalmente en una lista utilizando la función list

print(list(zip(names, ages))) # Output: [('Juan', 18), ('Maria', 25), ('Pedro', 30), ('Luisa', 40)]
""" --------------------------------------------- """

# 2. Dict Compren: Utilizando la función `zip` para crear un diccionario a partir de dos listas utilizando la comprensión de diccionarios

new_dict = {names: ages for (names, ages) in zip(names, ages)} # Output: {'Juan': 18, 'Maria': 25, 'Pedro': 30, 'Luisa': 40}
```
- Este código genera un diccionario donde las claves son los nombres y los valores son las edades correspondientes, utilizando la función zip para unir las dos listas

#### 2.2.4.2. **_Segunda forma: Uso de la función `len` para crear un diccionario a partir de dos listas**

La función `len` **permite obtener la longitud de una lista**, en este caso, se utiliza para recorrer las listas a partir de un `iterador` y crear el diccionario.

- En el siguiente ejemplo, se tienen dos listas: **una con nombres (`names`)** y **otra con edades (`ages`) **utilizando la función `len` para recorrer las listas mediante un `diccionario` con comprensión.**

```python

# Se crean dos listas: una con nombres y otra con edades
names = ["Juan", "Maria", "Pedro", "Luisa"]
ages = [18, 25, 30, 40, 50]

# Se utiliza un iterador para recorrer las listas y se crea un diccionario con comprensión
dict3 = {names[i]: ages[i] for i in range(len(names))}
print(dict3)  # Output: {'Juan': 18, 'Maria': 25, 'Pedro': 30, 'Luisa': 40}
```
- Para este caso, **es importante el iterador `i` ya que permite recorrer las listas y crear el diccionario.** Al imprimirlo, cumple la misma función que el ejemplo anterior.


> [!NOTE]
>
> **La primera forma es más eficiente que la segunda para evitar errores de indexación. **

> [!IMPORTANT]
> 
> Además, como se pudo visualizar **al unir las dos listas se obtiene un diccionario con las claves y valores con una misma longitud** por lo tanto **la edad de 50 no se agrega al diccionario**, ya que no hay un nombre correspondiente en la lista de nombres por ende se descarta.


### 2.2.5. *Uso de condicionales con y sin `dictionary comprenhention`*

Al igual que `list comprenhention`, **`dictionary comprenhention` también permite agregar condicionales para filtrar los elementos que se agregan al diccionario.**

#### 2.2.5.1. **Sintaxis de `dictionary comprenhention` con condicionales**

```python
 {key: value for value in iterable} 
```
- **`key`**: Es el nombre de la llave.
- **`value`**: Es el valor de la llave.
- **`iterable`**: Es el iterable que se va a recorrer.
- **`condition`**: Es la condicion que se debe cumplir para que se agregue el elemento o no al diccionario

#### 2.2.5.2. **Ejemplo de un `dictionary` con condición sin comprensión y con comprensión**

- Tomando el ejemplo anterior de la **lista de países y la población aleatoria**, se puede **agregar una condición para que solo se agreguen los países con una población mayor a `20`.**

**DICCIONARIO CON COMPRENSIÓN PARA INICIALIZAR EL DICCIONARIO CON COMPRENSIÓN A PARTIR DE UNA LISTA**

```python
import random

countries = ["MX", "COL", "ARG", "USA"]

population_V2 = {country: random.randint(1, 100) for country in countries} # diccionario con comprensión
```

**DICCIONARIO CON COMPRENSIÓN Y CONDICIONAL**

Luego de establecer a cada país con su respectiva población, se puede agregar una condición para que solo se agreguen los países con una población mayor a `20`. Ademas **se emplea en este caso la funcion `items()` para recorrer el diccionario de *population_V2***.

```python

# Codigo anterior

result ={country: population for (country, population) in population_V2.items() if population > 20}
print
```

#### 2.2.5.. **Ejemplo de un `dictionary comprenhention` con condición a partir de un Texto**
   
En este ejemplo **a partir de un texto se va a crear un `dictionary comprenhention` con condicional donde imprima las vocales y la cantidad de veces que aparecen en el texto, para ello se emplea la funcion `upper` para que las vocales aparezcan en mayuscula** y se agrega la condicion de que solo se agreguen las vocales al diccionario unique

```python
# 
text = "Hi, my name is Juan and I am a software developer"
# 
character_count = {character: text.lower().count(character) for character in 'aeiou' if text.lower().count(character) > 0} # Se incluye una condición para solo agregar las vocales al diccionario si aparecen en el texto (es decir, su conteo es mayor a 0).
print(character_count)
print(unique)
```
> [!IMPORTANT]
>
> **En el siguiente Módulo se exploran las funciones con el fin de profundizar mas acerca de los diccionarios con condicionales**


## Diferencias entre `List` vs `Tuples` vs `Sets`
<p align="center">
  <img src="https://i.postimg.cc/zGMXtDWy/imagen-2024-02-22-151915705.png" alt="Aquí va el texto del enlace">
</p>



