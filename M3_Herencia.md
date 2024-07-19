
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
  - [1.1. ***Ejemplo de Herencia Simple***](#11-ejemplo-de-herencia-simple)
  - [1.2. ***Ejemplo Avanzado de `Herecia Simple` usando métodos `build in`***](#12-ejemplo-avanzado-de-herecia-simple-usando-métodos-build-in)
- [2. **¿Qué es la Herencia Múltiple?**](#2-qué-es-la-herencia-múltiple)
  - [2.1. ***Ejemplo de `Herencia Múltiple` (no se usa el `método super()`)***](#21-ejemplo-de-herencia-múltiple-no-se-usa-el-método-super)
- [3. **Método MRO `Method Resolution Order` (Orden de las clases)**](#3-método-mro-method-resolution-order-orden-de-las-clases)

# 1. **¿Qué es la Herencia?**

<img align='right' width="230px" alt="coding web" src="https://i.postimg.cc/h4T0fdSK/imagen-2024-06-20-210740854.png" style="margin-left: 20px;">

La **herencia** es un **mecanismo que permite que una clase herede `atributos` y `métodos` de otra clase**. La clase que hereda se conoce como ***clase derivada*** o ***subclase***, y la clase de la que se hereda se conoce como ***clase base*** o ***superclase***.

La herencia es una de las características más importantes de la programación orientada a objetos. **Permite la *reutilización del código* y la reducción de la complejidad de un programa**.

<br>
<br>


## 1.1. ***Ejemplo de Herencia Simple***

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

## 1.2. ***Ejemplo Avanzado de `Herecia Simple` usando métodos `build in`***

En este ejemplo se tiene una superclase llamada `Lista Simple` con el atributo de elementos de lista y varios métodos **build in** (métodos ya definidos en Python) de los cuales va heredar la subclase `Lista Ordenada` para ordenar los elementos de la lista. 

```python
""" Clase padre """
class ListaSimple:
    def __init__(self, elementos):
        self.elementos = list(elementos)

    def agregar_elemento(self, elemento):
        self.elementos.append(elemento)

    def __getitem__(self, index):
        return self.elementos[index]
    
    def sort (self):
        self.elementos.sort()

    def __len__(self):
        return len(self.elementos)
    
    def __repr__(self):
        return f'{self.__class__.__name__}({self.elementos})'

""" Clase hija """
class ListaOrdenada(ListaSimple):
    def __init__(self, elementos):
        super().__init__(elementos)
        self.sort()

    def agregar_elemento(self, elemento):
        super().agregar_elemento(elemento)
        self.sort()

""" Segunda clase hija """
class ListaEnteros(ListaSimple):
    def __init__(self, elementos):
        for elemento in elementos:
            self._validar_elemento(elemento)
        super().__init__(elementos)
            
    def _validar_elemento(self, elemento):
        if not isinstance(elemento, int):
            raise ValueError(f'El elemento {elemento} debe ser un entero')
    
    def agregar_elemento(self, elemento):
        self._validar_elemento(elemento)
        super().agregar_elemento(elemento)


# Crear un objeto de la clase ListaOrdenada
SimpleList = ListaSimple([4, 2, 1, 3])
print(SimpleList) # Output: ListaSimple([4, 2, 1, 3])
listSort = ListaOrdenada([4,3,6,9,10,-1])
print(listSort) # Output: ListaOrdenada([-1, 3, 4, 6, 9, 10])
listSort.agregar_elemento(5)
print(listSort) # Output: ListaOrdenada([-1, 3, 4, 5, 6, 9, 10])
print(len(listSort)) # Output: 7

IntegerList = ListaEnteros([1, 12,1,33])
print(IntegerList) # Output: ListaEnteros([1, 12, 1, 33])
```

- En el ejemplo anterior, la clase `ListaOrdenada` hereda de la clase `ListaSimple` y agrega un método `sort()` para ordenar los elementos de la lista. Posterirmente tambien se crea una subclase llamada `ListaEnteros` que hereda de la clase `ListaSimple` y agrega un metodo `_validar_elemento` para validar que los elementos de la lista sean enteros.

# 2. **¿Qué es la Herencia Múltiple?**

<img align='right' width="350px" alt="coding web" src="https://i.postimg.cc/zfPJg92m/imagen-2024-06-21-220044137.png" style="margin-left: 20px;">

La **herencia múltiple** es un mecanismo en el que **una *`clase`* puede heredar `atributos` y `métodos` de más de una *`clase base`***. En Python, una clase puede heredar de múltiples clases base.

La herencia múltiple es una característica poderosa, pero también **puede ser complicada y propensa a errores**. **Se recomienda utilizar la herencia múltiple con precaución**.

> [!IMPORTANT]
>
> En la Herencia Multiple, cuando se hereda de varias clases, **no se puede llamar al metodo `super()` para llamar al constructor de las clases padres**, por lo que **se debe llamar a los constructores de las clases padres de manera explicita**.

<br>

## 2.1. ***Ejemplo de `Herencia Múltiple` (no se usa el `método super()`)***

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


# 3. **Método MRO `Method Resolution Order` (Orden de las clases)**

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