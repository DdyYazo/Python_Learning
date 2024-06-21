
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
