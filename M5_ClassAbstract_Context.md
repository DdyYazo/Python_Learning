
<div align="center">

# **Clases Abstractas, Contexto Estático (`atributos` y `métodos` de Clase) y Dinamico (`atributos` y `métodos` de Instancia), Constantes en Clases y Diseño de Clases y Relación de Agregación en Python**


<p align="center">
  <img src="https://i.postimg.cc/25hJPRKs/image.png" alt="Aquí va el texto del enlace" width="500">
</p>


</div>

# **Tabla de contenido**
- [**Clases Abstractas, Contexto Estático (`atributos` y `métodos` de Clase) y Dinamico (`atributos` y `métodos` de Instancia), Constantes en Clases y Diseño de Clases y Relación de Agregación en Python**](#clases-abstractas-contexto-estático-atributos-y-métodos-de-clase-y-dinamico-atributos-y-métodos-de-instancia-constantes-en-clases-y-diseño-de-clases-y-relación-de-agregación-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Clases Abstractas en Python**](#1-clases-abstractas-en-python)
- [2. **Métodos Estaticos (`staticmethod`) y de Clase (``classmethod``) en Python**](#2-métodos-estaticos-staticmethod-y-de-clase-classmethod-en-python)
  - [2.1. ***Métodos Estaticos `staticmethod` en Python***](#21-métodos-estaticos-staticmethod-en-python)
    - [2.1.1. **¿Cuál es la `función de un método estático`?**](#211-cuál-es-la-función-de-un-método-estático)
  - [2.2. ***Metodos de Clase `classmethod` en Python***](#22-metodos-de-clase-classmethod-en-python)
  - [2.3. ***¿Cuándo se debe utilizar un `método estático` y un `método de clase`?***](#23-cuándo-se-debe-utilizar-un-método-estático-y-un-método-de-clase)
- [3. **Contexto Estático *(atributos y métodos de clase)* y Dinamico *(atributos y métodos de instancia)* de una clase en Python**](#3-contexto-estático-atributos-y-métodos-de-clase-y-dinamico-atributos-y-métodos-de-instancia-de-una-clase-en-python)
  - [3.1. ***El contexto estático de una clase (`atributos` y `metodos estáticos -> clase`)***](#31-el-contexto-estático-de-una-clase-atributos-y-metodos-estáticos---clase)
  - [3.2. **El `contexto dinamico` de una clase (`atributos` y `metodos dinamicos -> instancia`)**](#32-el-contexto-dinamico-de-una-clase-atributos-y-metodos-dinamicos---instancia)
  - [3.3. ***Atributos de clase `al vuelo`***](#33-atributos-de-clase-al-vuelo)
- [4. **Constantes de Clases en Python**](#4-constantes-de-clases-en-python)
- [5. **Diseño de Clases en Python y relación de agregación**](#5-diseño-de-clases-en-python-y-relación-de-agregación)
  - [5.1. **Consultar más sobre el diseño de clases en *diagramas de clases y las relaciones existentes***](#51-consultar-más-sobre-el-diseño-de-clases-en-diagramas-de-clases-y-las-relaciones-existentes)
  - [5.2. ***Ejemplo de diseño de clases en Python (`«aggregation» relation`)***](#52-ejemplo-de-diseño-de-clases-en-python-aggregation-relation)
- [6. **Decoradores de Clases en Python**](#6-decoradores-de-clases-en-python)
  - [6.1. ***Ejemplo basico de decorador de clase `@` en Python***](#61-ejemplo-basico-de-decorador-de-clase--en-python)
  - [6.2. ***¿Cuándo se debe utilizar un `decorador de clase`?***](#62-cuándo-se-debe-utilizar-un-decorador-de-clase)
  - [6.3. ***Ejemplo real de la utilidad de un `decorador de clase` implementado en el patrón de diseño `Singleton`***](#63-ejemplo-real-de-la-utilidad-de-un-decorador-de-clase-implementado-en-el-patrón-de-diseño-singleton)
    - [6.3.1. **Patrón de diseño `Singleton`**](#631-patrón-de-diseño-singleton)
- [7. **Data classes `@dataclass` en Python**](#7-data-classes-dataclass-en-python)
  - [7.1. ***Caracteristicas de las data classes en Python***](#71-caracteristicas-de-las-data-classes-en-python)
  - [7.2. ***Ejemplo de uso de data classes en Python***](#72-ejemplo-de-uso-de-data-classes-en-python)
  - [7.3. ***Uso de los argumentos `eq` y `frozen` en las data classes***](#73-uso-de-los-argumentos-eq-y-frozen-en-las-data-classes)
  - [7.4. ***Caso de uso real en el que se utilizan las data classes***](#74-caso-de-uso-real-en-el-que-se-utilizan-las-data-classes)

# 1. **Clases Abstractas en Python**

<img align='right' width="300px" alt="coding web" src="https://i.postimg.cc/ZRD5ymK9/imagen-2024-06-25-170803304.png" style="margin-left: 20px;">

Las clases abstractas **son clases que no se pueden instanciar y que se utilizan como plantillas** para otras clases. Es decir que **deben ser obligatoriamente heredadas por otras clases** para poder ser utilizadas.


A partir del ejemplo de **Herencia Múltiple** **"[Figura Geometrica](./scripts/Herencia/Herencia%20Multiple/FigureGeometry_HM.py)"** al momento de heredarlo a las clases **[Cuadrado](./scripts/Herencia/Herencia%20Multiple/Cuadrado_HM.py)** y **[Triangulo](./scripts/Herencia/Herencia%20Multiple/Rectangulo_HM.py)** el metodo `area()` se debe implementar en cada una de las clases hijas, pero si se desea que el metodo `area()` sea obligatorio en todas las clases hijas, se puede utilizar una **Clase Abstracta**.

> [!IMPORTANT]
> 
> Al crear un método abstracto en una clase, **la clase en si se vuelve abstracta por lo que no se pueden crear instancias de la clase abstracta**, ya que en este caso **no tendria sentido instanciarla si no se sabe el tipo de figura geometrica que se desea crear.**

- Para crear una **Clase Abstracta** en Python se debe importar el modulo `abc` para heredar de la **clase `ABC`** y utilizar el decorador `@abstractmethod` para los métodos que se desean que sean obligatorios en las **clases hijas**.

```python
from abc import ABC, abstractmethod
""" Primera clase padre """
class FiguraGeometrica(ABC):
  """ Demas metodos de la clase"""

    @abstractmethod
    def area(self):
        pass

""" Clase hija """
class Cuadrado(FiguraGeometrica):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

""" Clase hija """
class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2

figura = FiguraGeometrica() # Error: TypeError: Can't instantiate abstract class FiguraGeometrica with abstract methods area
triangulo = Triangulo(10, 5)
print(triangulo.area()) # Output: 25.0
```

- En el ejemplo anterior, la clase `FiguraGeometrica` se convierte en una **Clase Abstracta** al heredar de la clase `ABC` y al utilizar el decorador `@abstractmethod` en el método `area()`. Por lo tanto las clases hijas están obligadas a implementar el método `area()`. 
  
  - Ademas, como ejemplo en la clase `Triangulo` se trato de crear una instancia de la clase `FiguraGeometrica` y **se obtuvo un error** ya que no se pueden crear instancias de una clase abstracta.
---


# 2. **Métodos Estaticos (`staticmethod`) y de Clase (``classmethod``) en Python**

## 2.1. ***Métodos Estaticos `staticmethod` en Python***

Los métodos estáticos **son métodos que se pueden acceder sin necesidad de crear una instancia (objeto)** de la clase
> [!IMPORTANT]
> 
> **No tienen acceso a los atributos de la clase o variables de instancia, por lo tanto no pasa como argumento el atributo `self`.** Pero si puede acceder a los atributos de clase.

- Para crear un **método estático** en Python se utiliza el decorador **`@staticmethod`** antes de la declaración del método.

```python
class MiClase:
    variable_clase = "Variable de clase"
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print("Este es un metodo estatico")
        print(MiClase.variable_clase)

MiClase.metodo_estatico() # Output: Este es un metodo estatico
```

- En el ejemplo anterior, se crea un método estático `metodo_estatico` en la clase `MiClase` con el decorador `@staticmethod`. Y al llamar al método estático con la clase `MiClase` mediante la notación de punto `(.)`, se imprime el mensaje del método estático y se accede a la variable de clase `variable_clase` de la clase `MiClase`.

### 2.1.1. **¿Cuál es la `función de un método estático`?**

Los métodos estaticos se utilizan para **realizar operaciones que no dependen de los atributos de la clase o de los objetos de la clase.** Estan posicionados en la clase por que tienen relación con la clase, pero no dependen de los atributos de la clase.

## 2.2. ***Metodos de Clase `classmethod` en Python***

Los métodos de clase **son métodos que se pueden acceder sin necesidad de crear una instancia de la clase**, pero que pueden acceder a los atributos de la clase.

> [!IMPORTANT]
>
> **Los métodos de clase reciben como argumento la clase misma, pasando como parametro el atributo *`cls`(class)*** y se accede a los atributos de clase mediante la clase misma.

- Para crear un método de clase en Python se utiliza el decorador `@classmethod` antes de la declaración del método.

```python
class MiClase:
    variable_clase = "Valor de la variable de clase"
    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia
        
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

MiClase.metodo_clase() # Output: Valor de la variable de clase
```

## 2.3. ***¿Cuándo se debe utilizar un `método estático` y un `método de clase`?***

- **Método estático:** Es útil cuando se desea realizar operaciones que no dependen del estado de ningún objeto de la clase ni de la clase misma
  
  - Por ejemplo, suponiendo que se tiene una clase `Calculadora` que realiza operaciones matemáticas básicas. Un método para calcular el área de un círculo podría ser estático, ya que solo necesita el radio como argumento y no depende de ningún objeto de la clase `Calculadora`.

```python
class Calculadora:
    PI = 3.1416
    
    @staticmethod
    def area_circulo(radio):
        return Calculadora.PI * (radio ** 2)

print(Calculadora.area_circulo(5)) # Output: 78.54
```

- **Método de clase:** Es útil cuando se desea realizar operaciones que dependen de los atributos de la clase misma, pero no de los atributos de una instancia de la clase.

  - Por ejemplo, si se tiene una clase `Empleado` y se quiere mantener un conteo de cuántos empleados se han creado, se puede utilizar un método de clase para mantener el conteo. **Esto es útil para operaciones que deben ser comunes a todas las instancias de la clase.**

```python
class Empleado:
  conteo_empleados = 0

  def __init__(self, nombre):
    self.nombre = nombre
    Empleado._incrementar_conteo()

  @classmethod
  def _incrementar_conteo(cls):
    cls.conteo_empleados += 1

  @classmethod
  def obtener_conteo_empleados(cls):
    return cls.conteo_empleados

# Creando instancias de Empleado, lo cual incrementa el conteo
empleado1 = Empleado("Juan")
empleado2 = Empleado("Ana")

# Accediendo al conteo de empleados a través de un método de clase
print(Empleado.obtener_conteo_empleados()) # Output: 2
```
---


# 3. **Contexto Estático *(atributos y métodos de clase)* y Dinamico *(atributos y métodos de instancia)* de una clase en Python**

<p align="center">
  <img src="https://i.postimg.cc/W1zzTSmp/imagen-2024-06-25-200223843.png" alt="Aquí va el texto del enlace" width="600">
</p>
<p align="center"><strong> Contexto Estático y Dinamico de una clase en Python</strong></p>


## 3.1. ***El contexto estático de una clase (`atributos` y `metodos estáticos -> clase`)***
 
Se refiere a los **atributos y métodos de la clase** que se pueden acceder sin necesidad de crear una instancia de la clase.

- Para acceder a los atributos y métodos estáticos de una clase se utiliza la notación de punto `(.)` con el nombre de la clase.

```python
class MiClase:
    nombre = "Juan"
    apellido = "Perez"
    edad = 28
    def __init__(self):
        pass

print(MiClase.nombre) # Output: Juan
```

- En el ejemplo anterior, se accede al atributo `nombre` de la clase `Persona` sin necesidad de crear una instancia de la clase.

 
## 3.2. **El `contexto dinamico` de una clase (`atributos` y `metodos dinamicos -> instancia`)**

Se refiere a los **atributos y métodos de la clase** que se pueden acceder **solo mediante una instancia de la clase.**

- Para acceder a los atributos y métodos dinámicos de una clase se utiliza la notación de punto `(.)` con el nombre de la instancia de la clase.

```python
class MiClase:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Juan", "Perez", 30)
print(persona1.nombre) # Output: Juan
```

- En el ejemplo anterior, se accede al atributo `nombre` de la instancia `persona1` de la clase `Persona` mediante la notación de punto `(.)`.

## 3.3. ***Atributos de clase `al vuelo`***

Se pueden agregar atributos a una clase al vuelo, es decir, **sin necesidad de declararlos en la clase.**

- Para agregar un atributo a una clase al vuelo se utiliza la notación de punto `(.)` con el nombre de la clase y el nombre del atributo.

```python
class MiClase:
    pass

MiClase.nombre = "Juan"
print(MiClase.nombre) # Output: Juan
```

- En el ejemplo anterior, se agrega el atributo `nombre` a la clase `MiClase` al vuelo y se accede a este mediante la notación de punto `(.)`.
---


# 4. **Constantes de Clases en Python**

Las constantes de clase son **atributos de clase que no cambian de valor durante la ejecución del programa.** Se utilizan para almacenar valores que no deben ser modificados.

- Para crear una constante de clase en Python se debe declarar un atributo de clase y asignarle un valor.

```python
class MiClase:
    PI = 3.1416
    GRAVEDAD = 9.8

print(MiClase.PI) # Output: 3.1416
```

> [!NOTE]
>
> las constante **siempre se deben declarar en mayúsculas y separadas por guiones bajos `_`** para especificar que son constantes.
---


# 5. **Diseño de Clases en Python y relación de agregación**

Pueden haber muchos casos para relacionar clases entre sí, por lo que es importante tener en cuenta el ***diseño de las clases*** para que sean **reutilizables, mantenibles y fáciles de entender.**

En este caso para entender como se puede establecer el **diseño de una clase** cuando se trabaja con varias clases es importante entender los conceptos de **relaciones entre clases** que considera **una relación de una clase con otra clase.** dependiendo de la relación que se desee establecer.

## 5.1. **Consultar más sobre el diseño de clases en *[diagramas de clases y las relaciones existentes](https://uniminuto0-my.sharepoint.com/:b:/g/personal/david_yazo_uniminuto_edu_co/EYXHyvF2llhPthLzTvGC8XQBejvTK0ax2EgrEgAKaFlqEg?e=iR7JMZ)*** 


## 5.2. ***Ejemplo de diseño de clases en Python (`«aggregation» relation`)***

En este ejemplo es importante comprender la relación de `«agregación»` entre las clases **`Orden`** y **`Producto`**.

1. Una clase **`Orden`** con el atributo de clase `contador_ordenes` que lleva la cuenta de cuántas órdenes se han creado y los atributos de instancia `id_orden` y `productos` que representan el identificador de la orden y una **lista de los productos** que se agregan a la orden.

2. Se tiene una clase **`Producto`** que tiene el atributo de clase `contador_productos` con los atributos de instancia `id_producto`, `nombre` y `precio` que representan el identificador del producto, el nombre del producto y el precio del producto respectivamente.


<img align='right' width="300px" alt="coding web" src="https://i.postimg.cc/rFwr85Cw/imagen-2024-06-27-192508855.png" style="margin-left: 20px;">


**Para entender como funciona la relación de `«agregación»`** entre las clases **`Orden`** y **`Producto`** se da por la **Relación Todo-Parte** que representa una relación todo-parte, pero con una asociación más débil que la `«composición»`. Aquí, la clase **`Orden`** actúa como el **"todo"** y los objetos **`Producto`** son las **"partes"**. Sin embargo, **estas "partes" (Producto) no están exclusivamente ligadas a una única "todo" (Orden)**, pudiendo ser compartidas entre diferentes Ordenes.

> [!IMPORTANT]
>
> Cuando se trabaja con varias clases, **se suele empezar por la clase que no tiene relación con otras clases, y luego se continúa con las clases que tienen relación con la clase inicial** como lo es el caso de la clase **`Orden`** y **`Producto`** en la que la clase **`Orden`** depende de la clase **`Producto`** para poder agregar productos a la orden.

```python

""" Clase Producto sin relación con la clase Orden """

class Producto:
    contador_productos = 0

    @classmethod
    def _incrementar_contador(cls):
        cls.contador_productos += 1
        return cls.contador_productos

    def __init__(self, nombre, precio):
        self._id_producto = Producto._incrementar_contador()
        self._nombre = nombre
        self._precio = precio
    
    # Getters y Setters omitidos

    def __str__(self):
        return f"Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}"

""" Clase Orden con relación de agregación con la clase Producto """

class Orden:
    contador_ordenes = 0

    @classmethod
    def _incrementar_contador(cls):
        cls.contador_ordenes += 1
        return cls.contador_ordenes

    def __init__(self, productos):
        self._id_orden = Orden._incrementar_contador()
        self._productos = list(productos)

    # Getters y Setters omitidos

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total (self):
        total = 0
        for producto in self._productos:
            total += producto.precio # metodo getter de precio
        return total


    def __str__(self):
        productos_str = ""
        for producto in self._productos:
            productos_str += producto.__str__() + '|'
        return f"Orden: {self._id_orden}\nProductos:\n{productos_str} \nTotal: {self.calcular_total()}"

# Creando productos
producto1 = Producto("Camisa", 100.00)
producto2 = Producto("Pantalon", 150.00)
producto3 = Producto("Zapatos", 200.00)

# Creando orden
productos = [producto1, producto2]
orden1 = Orden(productos)
print(orden1) # Output: Orden: 1 Productos: Id Producto: 1, Nombre: Camisa, Precio: 100.0 Id Producto: 2, Nombre: Pantalon, Precio: 150.0 | Total: 250.0

orden1.agregar_producto(producto3)
print(orden1) # Output: Orden: 1 Productos: Id Producto: 1, Nombre: Camisa, Precio: 100.0 Id Producto: 2, Nombre: Pantalon, Precio: 150.0 Id Producto: 3, Nombre: Zapatos, Precio: 200.0 | Total: 450.0
```

- En el ejemplo anterior, se crean las clases **`Producto`** y **`Orden`**. La clase **`Producto`** no tiene relación con la clase **`Orden`** y la clase **`Orden`** tiene una relación de **agregación** con la clase **`Producto`**. Se crean instancias de la clase **`Producto`** y se agregan a la clase **`Orden`** mediante el método `agregar_producto()`, ademas se calcula el total de la orden mediante el método `calcular_total()` el cual mediante un ciclo `for` suma el precio de cada producto en la orden accediendo al metodo `getter` de `precio` de la clase **`Producto`**. Luego se imprime la orden con los productos agregados a partir de una variable de tipo lista `productos` trayendo los datos del producto mediante el método `__str__()` de la clase **`Producto`**.


---


# 6. **Decoradores de Clases en Python**

Los decoradores de clases en Python son funciones que se utilizan para **modificar o extender el comportamiento de una clase** sin modificar directamente su código.

- Es similar a los decoradores de funciones, es decir que se utilizan para **añadir funcionalidades a una clase** sin modificar su código.

- Para crear un decorador de clase en Python se utiliza la función `@decorador` antes de la declaración de la clase.

## 6.1. ***Ejemplo basico de decorador de clase `@` en Python***

```python
import inspect


def decorador_repr(cls):
    print('1. Se ejecuta decorador')
    print(f'Recibimos el objeto de la clase: {cls.__name__}')

    atributos = vars(cls)
    # Revisamos si se ha sobreescrito el método __init__
    if '__init__' not in atributos:
        raise TypeError(f'{cls.__name__} no ha sobreescrito el método __init__')

    firma_init = inspect.signature(cls.__init__)
    print(f'Firma método __init__: {firma_init}')
    # Recuperamos los parámetros, excepto el primero que es self usando un slice [1:]
    parametros_init = list(firma_init.parameters)[1:]
    print(f'Parámetros init: {parametros_init}')

     # Revisamos si cada parámetro tiene un método property asociado
    for parametro in parametros_init:
        # property es un valor de tipo built-in para preguntar si se esta utilizando el decorador property
        es_metodo_property = isinstance(atributos.get(parametro), property)
        if not es_metodo_property:
            raise TypeError(f'No existe un método property para el parámetro: {parametro}')
    # Crear el método __repr__ dinámicamente es decir en tiempo de ejecución
    def metodo_repr(self):
        nombre_clase = self.__class__.__name__
        print(f'Nombre clase: {nombre_clase}')
        # Obtenemos los nombres de las propiedades y sus valores dinámicamente
        # Expresion Generadora, crear nombre_atr=valor_atr
        generador_arg = (f'{nombre}={getattr(self, nombre)!r}' for nombre in parametros_init)
        # Lista de argumentos
        lista_arg = list(generador_arg)
        print(f'Lista del generador: {lista_arg}')
        argumentos = ', '.join(lista_arg)
        print(f'Argumentos del método repr: {argumentos}')
        
        # Creamos la forma del método __repr__, sin su nombre, solo la firma
        resultado_metodo_repr = f'{nombre_clase}({argumentos})'
        print(f'Resultado método repr: {resultado_metodo_repr}')
        return resultado_metodo_repr

    # Agregar dinámicamente el método repr a nuestra clase
    setattr(cls,'__repr__', metodo_repr)
    return cls

@decorador_repr
class Persona:
    def __init__(self, nombre, apellido, edad):
        print('2. Se ejecuta el inicializador')
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @property
    def apellido(self):
        return self._apellido

    @property
    def edad(self):
        return self._edad

    # def __repr__(self):
    #     return f'Persona(nombre={self._nombre}, apellido={self._apellido})'

persona1 = Persona('Juan','Perez', 28)
print(persona1) # Output: Persona(nombre=Juan, apellido=Perez, edad=28)
pesona2 = Persona('Karla','Gomez', 30)
print(pesona2) # Output: Persona(nombre=Karla, apellido=Gomez, edad=30)
#Tiene los métodos de propiedad nombre, apellido, repr
print(dir(Persona))
# Tiene el método repr sobreescrito
codigo_repr = inspect.getsource(persona1.__repr__)
print(codigo_repr) # Output: 'Persona(nombre=Juan, apellido=Perez, edad=28)'
```

- En el ejemplo anterior:
   
   1. Se crea un decorador de clase `decorador_repr` que se encarga de verificar si la clase que recibe como argumento tiene un método `__init__` y si los parámetros del método `__init__` tienen métodos `property` asociados. Ademas, mediante la libreria `inspect` se obtiene la firma del método `__init__` utilizando el método `signature` y se obtienen los parámetros del método `__init__` mediante el método `parameters`.
   
   2. Luego se crea un método `metodo_repr` que se encarga de devolver una representación de la clase con los argumentos del método `__init__` utilizando el método `getattr` para obtener los valores de los atributos de la clase. Finalmente, se asigna el método `metodo_repr` a la clase `Persona` mediante la función `setattr`.

## 6.2. ***¿Cuándo se debe utilizar un `decorador de clase`?***

- Los decoradores de clase se utilizan cuando se desea **añadir funcionalidades a una clase sin modificar su código**. 

## 6.3. ***Ejemplo real de la utilidad de un `decorador de clase` implementado en el patrón de diseño `Singleton`***

Un caso real donde los decoradores de clase son particularmente utiles es en el desarrollo de aplicaciones con el patrón de diseño `Singleton`.

### 6.3.1. **Patrón de diseño `Singleton`**

El patrón Singleton **es un patrón de diseño que restringe la instanciación de una clase a un solo objeto.**

- Esto **es útil en situaciones donde se necesita controlar el acceso a algún recurso compartido, como una conexión a una base de datos en una aplicación web.**

**PROPOSITO DE LA IMPLEMENTACIÓN DE UN DECORADOR DE CLASE PARA EL PATRÓN SINGLETON**

El propósito de implementar un decorador de clase para el patrón Singleton es **asegurar que una clase solo tenga una instancia en toda la aplicación y proporcionar un punto de acceso global a esa instancia.** 

- Esto **se hace sin modificar la clase en sí, manteniendo el código limpio y facilitando la reutilización del decorador en otras clases** que también deban implementar el patrón Singleton.

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Database:
    def __init__(self):
        print("Creando la instancia de la base de datos")

# Intentando crear múltiples instancias
db1 = Database()
db2 = Database()

# Verificando que ambas variables apunten a la misma instancia
print(db1 == db2)  # Salida: True
```

- En el ejemplo anterior, se crea un decorador de clase `singleton` que se encarga de asegurar que una clase solo tenga una instancia en toda la aplicación. Se crea un diccionario `instances` que almacena las instancias de la clase y se crea un método `get_instance` que se encarga de crear una instancia de la clase si no existe en el diccionario `instances`. Finalmente, se asigna el método `get_instance` a la clase `Database` mediante el decorador `@singleton`.

# 7. **Data classes `@dataclass` en Python**

Las data classes son una característica de Python que permite **crear clases que se utilizan principalmente para almacenar datos.**

## 7.1. ***Caracteristicas de las data classes en Python***

- Las data classes son **clases que se utilizan para almacenar datos y no tienen métodos personalizados.**

- Para crear una data class en Python **se utiliza el decorador `@dataclass` antes de la declaración de la clase y es necesario importar la librería `dataclasses`.**

> [!IMPORTANT]
>
> - Por lo general al declarar los atributos de una `data class` si es necesario utilizar ***anotaciones de tipo*** para **especificar el tipo de dato de los atributos**, que a diferencia de los atributos de una clase normal, en una data class no es necesario inicializar los atributos en el método `__init__`.

## 7.2. ***Ejemplo de uso de data classes en Python***

```python
from dataclasses import dataclass
from typing import ClassVar

@dataclass(eq=True, frozen=True)
class Domicilio:
    calle: str
    numero: int = 0

@dataclass(eq=True, frozen=True)
class Persona:
    nombre: str
    apellido: str
    domicilio: Domicilio
    contador_personas: ClassVar[int] = 0

    def __post_init__(self):
        if not self.nombre:
            raise ValueError(f'Valor nombre vacío: {self.nombre}')

# Definir una instancia de la clase Domicilio
domicilio1 = Domicilio('Saturno', 15)
persona1 = Persona('Juan','Perez', domicilio1)
print(f'{persona1!r}') # Output: Persona(nombre='Juan', apellido='Perez', domicilio=Domicilio(calle='Saturno', numero=15))
# Variable de clase
print(f'Variable clase: {Persona.contador_personas}') # Output: Variable clase: 0

# Variables de instancia
print(f'Variables de instancia: {persona1.__dict__}') # Output: Variables de instancia: {'nombre': 'Juan', 'apellido': 'Perez', 'domicilio': Domicilio(calle='Saturno', numero=15)}

# Variable con valores vacíos
persona_vacia = Persona('Karla','', None)
print(f'Persona vacía: {persona_vacia}') # Output: ValueError: Valor nombre vacío: 

# Revisar igualdad entre objetos (__eq__)
persona2 = Persona('Juan','Perez', Domicilio('Saturno', 15))
print(f'Objetos iguales?: {persona1 == persona2}') # Output: True

# Agregar esta clase a una colecciones
coleccion = {persona1, persona2}
print(coleccion) # Output: {Persona(nombre='Juan', apellido='Perez', domicilio=Domicilio(calle='Saturno', numero=15))}

# Frozen = True
# coleccion[0].nombre='Juan Carlos'
# persona1.nombre = 'Juan Carlos'
```

- En el ejemplo anterior, se crean las data classes `Domicilio` y `Persona` utilizando el decorador `@dataclass`, con los argumentos `eq=True` y `frozen=True` para que las instancias de las data classes sean inmutables y se puedan comparar mediante el método `__eq__`. 

  1. La data class `Domicilio` tiene los atributos `calle` asignandole un valor por defecto que es un string y `numero` asignandole un valor por defecto que es un entero igual a 0.
  
  2. La data class `Persona` tiene los atributos `nombre` que tiene un string como valor por defecto, `apellido` que tiene un string como valor por defecto, `domicilio` que tiene un objeto de la clase `Domicilio` como valor por defecto y `contador_personas` que es una variable de clase con un valor por defecto igual a 0. Ademas, se sobreescribe el método `__post_init__` para verificar que el atributo `nombre` no esté vacío.
       - Para el atributo de `contador_personas` se utiliza la librearía `typing` para definir una variable de clase `ClassVar` que se utiliza para definir una variable de clase que no es una variable de instancia.

## 7.3. ***Uso de los argumentos `eq` y `frozen` en las data classes***

- **`eq=True`:** Se utiliza para que las instancias de la data class sean compar

- **`frozen=True`:** Se utiliza para que las instancias de la data class sean inmutables, es decir que no se puedan modificar una vez creadas.

## 7.4. ***Caso de uso real en el que se utilizan las data classes***

Un caso real donde las data classes son particularmente **útiles es en el desarrollo de aplicaciones que requieren el manejo de configuraciones complejas o el procesamiento de datos estructurados**, como los **provenientes de un archivo `JSON` o una base de datos.**

- Si se está desarrollando una aplicación web y se tiene un **archivo de configuración `JSON`** que contiene información sobre la base de datos, autenticación, y otros parámetros de configuración. En lugar de manejar este archivo de configuración **como un diccionario y acceder a sus valores mediante claves de cadena (*lo cual es propenso a errores debido a posibles `errores tipográficos`***), **se puede definir una data class que represente esta configuración de manera más estructurada y segura.**

```python
from dataclasses import dataclass
import json

@dataclass
class AppConfig:
    database_url: str
    secret_key: str
    debug_mode: bool
    allowed_hosts: list

def load_config_from_json(json_file: str) -> AppConfig:
    with open(json_file, 'r') as file:
        config_data = json.load(file)
    return AppConfig(**config_data)

# Cargando la configuración desde un archivo JSON
config = load_config_from_json('config.json')

print(config.database_url)  # Acceso seguro y tipado a la configuración
```

- En el ejemplo anterior, se crea una data class `AppConfig` que representa la configuración de una aplicación web. Se define una función `load_config_from_json` que carga la configuración desde un archivo `JSON` y devuelve una instancia de la data class `AppConfig`. Luego se carga la configuración desde un archivo `JSON` y se accede a los valores de la configuración mediante los atributos de la data class `AppConfig`.