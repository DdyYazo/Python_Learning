
<div align="center">

# **Clases Abstractas, Contexto Estático y Dinamico en Python**


<p align="center">
  <img src="https://i.postimg.cc/25hJPRKs/image.png" alt="Aquí va el texto del enlace" width="500">
</p>


</div>

# **Tabla de contenido**
- [**Clases Abstractas, Contexto Estático y Dinamico en Python**](#clases-abstractas-contexto-estático-y-dinamico-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Clases Abstractas en Python**](#1-clases-abstractas-en-python)
- [2. **Métodos Estaticos y de Clase en Python**](#2-métodos-estaticos-y-de-clase-en-python)
  - [2.1. **Métodos Estaticos en Python**](#21-métodos-estaticos-en-python)
    - [2.1.1. **¿Cuál es la `función de un método estático`?**](#211-cuál-es-la-función-de-un-método-estático)
  - [2.2. **Metodos de Clase en Python**](#22-metodos-de-clase-en-python)
  - [2.3. **¿Cuándo se debe utilizar un `método estático` y un `método de clase`?**](#23-cuándo-se-debe-utilizar-un-método-estático-y-un-método-de-clase)
- [3. **Contexto Estático *(variables y métodos de clase)* y Dinamico *(variables y métodos de instancia)* de una clase en Python**](#3-contexto-estático-variables-y-métodos-de-clase-y-dinamico-variables-y-métodos-de-instancia-de-una-clase-en-python)
  - [3.1. **El `contexto estático` de una clase `(atributos y metodos estáticos -> clase)`**](#31-el-contexto-estático-de-una-clase-atributos-y-metodos-estáticos---clase)
  - [3.2. **El `contexto dinamico` de una clase `(atributos y metodos dinamicos -> instancia)`**](#32-el-contexto-dinamico-de-una-clase-atributos-y-metodos-dinamicos---instancia)
  - [4.3. **`Variables de clase al vuelo`**](#43-variables-de-clase-al-vuelo)
- [4. **Constantes de Clases en Python**](#4-constantes-de-clases-en-python)
- [5. **Diseño de Clases en Python**](#5-diseño-de-clases-en-python)

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

# 2. **Métodos Estaticos y de Clase en Python**

## 2.1. **Métodos Estaticos en Python**

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

Los métodos estaticos se utilizan para **realizar operaciones que no dependen de los atributos de la clase o de los objetos de la clase.**

## 2.2. **Metodos de Clase en Python**

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

## 2.3. **¿Cuándo se debe utilizar un `método estático` y un `método de clase`?**

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

# 3. **Contexto Estático *(variables y métodos de clase)* y Dinamico *(variables y métodos de instancia)* de una clase en Python**

<p align="center">
  <img src="https://i.postimg.cc/W1zzTSmp/imagen-2024-06-25-200223843.png" alt="Aquí va el texto del enlace" width="600">
</p>
<p align="center"><strong> Contexto Estático y Dinamico de una clase en Python</strong></p>


## 3.1. **El `contexto estático` de una clase `(atributos y metodos estáticos -> clase)`**
 
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

 
## 3.2. **El `contexto dinamico` de una clase `(atributos y metodos dinamicos -> instancia)`**

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

## 4.3. **`Variables de clase al vuelo`**

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


# 5. **Diseño de Clases en Python**





