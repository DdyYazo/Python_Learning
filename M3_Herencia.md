
<div align="center">

# **Herencia en Python**


<p align="center">
  <img src="https://i.postimg.cc/cLT7ZjVV/image-2.png" alt="Aquí va el texto del enlace" width="400">
</p>


</div>

# **Tabla de contenido**
- [**Herencia en Python**](#herencia-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **¿Qué es la Herencia?**](#1-qué-es-la-herencia)
  - [1.1. **`Ejemplo de Herencia`**](#11-ejemplo-de-herencia)
- [2. **Sobreescritura (Override) del método `__str__`**](#2-sobreescritura-override-del-método-__str__)
  - [2.1. **`Ejemplo de Herencia con sobreescritura del método __str__ y buenas practicas`**](#21-ejemplo-de-herencia-con-sobreescritura-del-método-__str__-y-buenas-practicas)
      - [**¿Por qué no se encapsularón los atributos ni se declararón los métodos `getter` y `setter` en este ejemplo?**](#por-qué-no-se-encapsularón-los-atributos-ni-se-declararón-los-métodos-getter-y-setter-en-este-ejemplo)
- [3. **¿Qué es la Herencia Múltiple?**](#3-qué-es-la-herencia-múltiple)
  - [3.1. **`Ejemplo de Herencia Múltiple (no se usa el método super())`**](#31-ejemplo-de-herencia-múltiple-no-se-usa-el-método-super)
- [4. **Método MRO "Method Resolution Order" (Orden de las clases)**](#4-método-mro-method-resolution-order-orden-de-las-clases)

# 1. **¿Qué es la Herencia?**

<img align='right' width="230px" alt="coding web" src="https://i.postimg.cc/h4T0fdSK/imagen-2024-06-20-210740854.png" style="margin-left: 20px;">

La **herencia** es un **mecanismo que permite que una clase herede `atributos` y `métodos` de otra clase**. La clase que hereda se conoce como ***clase derivada*** o ***subclase***, y la clase de la que se hereda se conoce como ***clase base*** o ***superclase***.

La herencia es una de las características más importantes de la programación orientada a objetos. **Permite la *reutilización del código* y la reducción de la complejidad de un programa**.

<br>
<br>


## 1.1. **`Ejemplo de Herencia`**

<p align="center">
  <img src="https://i.postimg.cc/vm73CxcY/imagen-2024-06-20-215046818.png" alt="Aquí va el texto del enlace" width="500">
</p>
<p align="center"><strong> Ejemplo de Herencia en Python</strong></p>

En este ejemplo se tiene una superclase llamada `Persona` con los atributos privados `nombre` y `edad`, y una subclase llamada `Empleado` que hereda de `Persona` y agrega un atributo `salario`.

```python
""" Clase padre """
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_nombre(self):
        return self.nombre

    def mostrar_edad(self):
        return self.edad

""" Clase hija """
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def mostrar_salario(self):
        return self.salario

# Crear un objeto de la clase Empleado
empleado1 = Empleado("Juan", 30, 5000)
print(empleado1.mostrar_nombre())
print(empleado1.mostrar_edad())
print(empleado1.mostrar_salario())
```

- En el ejemplo anterior, la clase `Empleado` hereda de la clase `Persona` y agrega un atributo `salario`. 

- Para llamar al constructor de la clase base, se utiliza la función `super()` llamando al método `__init__` de la clase base, pero tambien es importante que se debe pasar como parametro los atributos que se desean heredar en este caso `nombre` y `edad` en el metodo `__init__` de la clase `Empleado`.

> [!IMPORTANT]
>
> **Es crucial llamar al constructor de la clase base en la clase derivada utilizando la función `super()`**, para que los atributos de la clase base se inicialicen correctamente.

# 2. **Sobreescritura (Override) del método `__str__`**

En Python, el método `__str__` se utiliza para sobrescribir **(*Override*)** la representación de cadena de un objeto. **Cuando se imprime un objeto, se llama automáticamente al método `__str__`**.

**Archivo 1: persona.py**

```python
""" Clase padre """
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

""" Clase hija """
class Empleado(Persona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.salario = salario

    def __str__(self):
        return f"{super().__str__()}, Salario: {self.salario}"

# Crear un objeto de la clase Empleado
empleado1 = Empleado("Juan", 30, 5000)
print(empleado1) # Nombre: Juan, Edad: 30, Salario: 5000
```
**Archivo 2: main.py**

```python	

from persona import *

persona1 = Persona("Juan", 30)
print(persona1) # Nombre: Juan, Edad: 30

emple1 = Empleado("Pedro", 25, 4000)
print(emple1) # Nombre: Pedro, Edad: 25, Salario: 4000
```

- En el ejemplo anterior, se sobrescribe el método `__str__` en las clases `Persona` y `Empleado` para personalizar la representación de cadena de los objetos al momento de importar el modulo `persona.py` en el archivo `main.py`.

- Al imprimir los objetos `persona1` y `emple1`, se llama automáticamente al método `__str__` de cada clase.

## 2.1. **`Ejemplo de Herencia con sobreescritura del método __str__ y buenas practicas`**

Para este caso se tiene una superclase llamada **`Vehiculo`** con los atributos de `color` y `ruedas`, y sus metodos `__init__` y `__str__`, y dos subclases llamadas **`Coche`** con el atributo `velocidad` y tambien con sus metodos `__init__` y `__str__`, y **`Bicicleta`** con el atributo `tipo` y tambien con sus metodos `__init__` y `__str__`, los cuales heredan de la clase **`Vehiculo`**, tanto sus atributos como sus metodos.

```python
class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Mi vehículo tiene: [Color: {self.color}, Ruedas: {self.ruedas}]'

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Mi coche tiene: [Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} km/hr]'

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Mi bicicleta tiene: [Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}]'

# Creación de objeto de prueba
Vehiculo1 = Vehiculo('Rojo', 4)
print(Vehiculo1)
print()
Vehiculo2 = Coche('Azul', 4, 120)
print(Vehiculo2)
print()
Vehiculo3 = Bicicleta('Verde', 2, 'Montaña')
print(Vehiculo3)
```

- De esta manera se puede ver como se puede sobrescribir el metodo `__str__` en las clases `Vehiculo`, `Coche` y `Bicicleta` para personalizar la representación de cadena de los objetos.

#### **¿Por qué no se encapsularón los atributos ni se declararón los métodos `getter` y `setter` en este ejemplo?**

Recapitulando, los métodos **`getters`** y **`setters`** **se utilizan principalmente para controlar el acceso a los atributos de una clase y para realizar validaciones o cálculos adicionales cuando se accede o se modifica un atributo**. Si no se necesita realizar ninguna validación o cálculo adicional, no hay necesidad de implementar métodos **`getters`** y **`setters`**.

> [!TIP]
>
> **La mejor práctica para este caso y un caso futuro, es diseñar siempre las clases de manera que sean fáciles de usar y de mantener**. Si en el futuro se necesita proteger los atributos o realizar validaciones o cálculos adicionales, si seria necesario agregar métodos **`getters`** y **`setters`** sin problemas. Sin embargo, si no se necesita hacerlo ahora, no hay necesidad de complicar el código agregando estos métodos innecesariamente.
--- 
<br>

# 3. **¿Qué es la Herencia Múltiple?**

<img align='right' width="350px" alt="coding web" src="https://i.postimg.cc/zfPJg92m/imagen-2024-06-21-220044137.png" style="margin-left: 20px;">

La **herencia múltiple** es un mecanismo en el que **una *`clase`* puede heredar `atributos` y `métodos` de más de una *`clase base`***. En Python, una clase puede heredar de múltiples clases base.

La herencia múltiple es una característica poderosa, pero también **puede ser complicada y propensa a errores**. **Se recomienda utilizar la herencia múltiple con precaución**.

> [!IMPORTANT]
>
> En la Herencia Multiple, cuando se hereda de varias clases, **no se puede llamar al metodo `super()` para llamar al constructor de las clases padres**, por lo que **se debe llamar a los constructores de las clases padres de manera explicita**.

<br>

## 3.1. **`Ejemplo de Herencia Múltiple (no se usa el método super())`**

En este ejemplo se tiene principalmente una clase padre llamada **`FiguraGeometrica`** con los atributos `ancho` y `alto` de tipo privado con sus metodos `__init__` , `getter` y `setter`, otra clase padre llamada `Color` con el atributo `color` de tipo privado con sus metodos `__init__` , `getter` y `setter`, y una clase hija llamada **`Cuadrado`** que hereda de las clases `FiguraGeometrica` y `Color` y ademas tiene su atributo `lado` con sus metodos `__init__` , con el metodo `calcula_area`.

```python
""" Primera clase padre """
class FiguraGeometrica:
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

    def get_alto(self):
        return self.__alto

    def set_alto(self, alto):
        self.__alto = alto

""" Segunda clase padre """
class Color:
    def __init__(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

""" Clase hija """
from figura_geometrica import FiguraGeometrica
from color import Color

Class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, color, lado):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)

    def calcula_area(self):
        return self.get_ancho() * self.get_alto()
```

- En el ejemplo anterior, la clase `Cuadrado` hereda de las clases `FiguraGeometrica` y `Color` y agrega un atributo `lado`.

---

**Por que para el caso de los atributos de `ancho` y `alto`se paso como parametro el atributo de lado en el metodo `__init__` de la clase `Cuadrado`?** 

- Porque el cuadrado es una figura geometrica que tiene todos sus lados iguales, por lo tanto, el ancho y el alto son iguales, por lo que se paso el atributo `lado` como parametro en el metodo `__init__` de la clase `Cuadrado`.

# 4. **Método MRO "Method Resolution Order" (Orden de las clases)**

El **MRO** es el **orden en el que se buscan los métodos en las clases base** cuando se llama a un método en una clase derivada. En Python, el MRO se calcula utilizando el algoritmo **C3 Linearization**.

El MRO se puede obtener utilizando el atributo **`__mro__`** o la función **`mro()`**.

```python
from ClassCuadrado_HM import Cuadrado

cuadrado1 = Cuadrado(12, 'verde')
print(f'Cálculo área del Cuadrado: {cuadrado1.calcular_area()}')

# MRO - Method Resolution Order
print(Cuadrado.__mro__) # Output: (<class '__main__.Cuadrado'>, <class 'figura_geometrica.FiguraGeometrica'>, <class 'color.Color'>, <class 'object'>)
print(Cuadrado.mro()) # Output: [<class '__main__.Cuadrado'>, <class 'figura_geometrica.FiguraGeometrica'>, <class 'color.Color'>, <class 'object'>]
```
> [!NOTE]
> 
> Este método es util **cuando se quiere saber la jerarquia de las clases que se estan heredando en una clase hija** y como es el orden de busqueda de los metodos en las clases padres.