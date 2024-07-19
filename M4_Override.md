
<div align="center">

# **Representación o sobreescritura de objetos en Python**


<p align="center">
  <img src="https://i.postimg.cc/cLT7ZjVV/image-2.png" alt="Aquí va el texto del enlace" width="400">
</p>


</div>

# **Tabla de contenido**
- [**Representación o sobreescritura de objetos en Python**](#representación-o-sobreescritura-de-objetos-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Sobreescritura (Override) del método `__str__`**](#1-sobreescritura-override-del-método-__str__)
  - [1.1. ***Ejemplo de Herencia con sobreescritura del `método __str__` y buenas practicas***](#11-ejemplo-de-herencia-con-sobreescritura-del-método-__str__-y-buenas-practicas)
    - [**¿Por qué no se encapsularón los atributos ni se declararón los métodos `getter` y `setter` en este ejemplo?**](#por-qué-no-se-encapsularón-los-atributos-ni-se-declararón-los-métodos-getter-y-setter-en-este-ejemplo)
- [2. **Representación de un objeto en Python mediante el método `__repr__`**](#2-representación-de-un-objeto-en-python-mediante-el-método-__repr__)
  - [2.1. ***Ejemplo de uso del método `__repr__`***](#21-ejemplo-de-uso-del-método-__repr__)
  - [2.2. ***Forma alternativa para llamar al método `__repr__` usando `!r`***](#22-forma-alternativa-para-llamar-al-método-__repr__-usando-r)
  - [2.3. ***Llamar el nombre de la clase medainte el método especial `__class__.__name__`***](#23-llamar-el-nombre-de-la-clase-medainte-el-método-especial-__class____name__)
- [3. **Diferencia entre el método `__str__` y `__repr__`**](#3-diferencia-entre-el-método-__str__-y-__repr__)
  - [3.1. ***Orden de prioridad de llamada de los métodos `__str__` y `__repr__`***](#31-orden-de-prioridad-de-llamada-de-los-métodos-__str__-y-__repr__)
- [4. **Método `__format__` en Python**](#4-método-__format__-en-python)

# 1. **Sobreescritura (Override) del método `__str__`**

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

## 1.1. ***Ejemplo de Herencia con sobreescritura del `método __str__` y buenas practicas***

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

### **¿Por qué no se encapsularón los atributos ni se declararón los métodos `getter` y `setter` en este ejemplo?**

Recapitulando, los métodos **`getters`** y **`setters`** **se utilizan principalmente para controlar el acceso a los atributos de una clase y para realizar validaciones o cálculos adicionales cuando se accede o se modifica un atributo**. Si no se necesita realizar ninguna validación o cálculo adicional, no hay necesidad de implementar métodos **`getters`** y **`setters`**.

> [!TIP]
>
> **La mejor práctica para este caso y un caso futuro, es diseñar siempre las clases de manera que sean fáciles de usar y de mantener**. Si en el futuro se necesita proteger los atributos o realizar validaciones o cálculos adicionales, si seria necesario agregar métodos **`getters`** y **`setters`** sin problemas. Sin embargo, si no se necesita hacerlo ahora, no hay necesidad de complicar el código agregando estos métodos innecesariamente.
--- 
<br>

# 2. **Representación de un objeto en Python mediante el método `__repr__`**

El método `__repr__` se utiliza para devolver una representación de cadena de un objeto que se puede utilizar para recrear el objeto. **Cuando se imprime un objeto, se llama automáticamente al método `__repr__`**.

> [!NOTE]
>
> Es exclusivo para el entendimiento del lado del programador, no para el usuario final.

## 2.1. ***Ejemplo de uso del método `__repr__`***

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __repr__(self):
        return f"Persona(nombre: {self.nombre}, apellido: {self.apellido})"

persona1 = Persona("Juan", "Perez")
print(persona1) # Persona(nombre: Juan, apellido: Perez)
```

- En el ejemplo anterior, se sobrescribe el método `__repr__` en la clase `Persona` para devolver una representación de cadena del objeto que se puede utilizar para recrear el objeto.

## 2.2. ***Forma alternativa para llamar al método `__repr__` usando `!r`***

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __repr__(self):
        return f"Persona(nombre: {self.nombre}, apellido: {self.apellido})"

persona1 = Persona("Juan", "Perez")
print(f'Mi objeto persona1: {persona1!r}') # Mi objeto persona1: Persona(nombre: Juan, apellido: Perez)
```

- En el ejemplo anterior, se utiliza la forma alternativa de llamar al método `__repr__` en la clase `Persona` mediante el uso de `!r` en la cadena de formato.

## 2.3. ***Llamar el nombre de la clase medainte el método especial `__class__.__name__`***

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def __repr__(self):
        return f"{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})"

persona1 = Persona("Juan", "Perez")
print(persona1) # Persona(nombre: Juan, apellido: Perez)
```

- En el ejemplo anterior, se utiliza el método especial `__class__.__name__` para obtener el nombre de la clase del objeto y devolver una representación de cadena del objeto que se puede utilizar para recrear el objeto.

> [!NOTE]
>
> En casos como la herecia de clases, el método `__class__.__name__` es útil para obtener el nombre de la clase del objeto de donde se hereda.

# 3. **Diferencia entre el método `__str__` y `__repr__`**

- **`__str__`** se utiliza para devolver una representación de cadena **legible para el usuario final.**

- **`__repr__`** se utiliza para devolver una representación de cadena que se puede utilizar para recrear el objeto, **util para el programador.**

El orden de prioridad de llamada de los métodos es el siguiente:

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})"

    def __str__(self):
        return f"Persona: {self.nombre}, {self.apellido}"

persona1 = Persona("Juan", "Perez")
print(persona1) # Persona: Juan, Perez
print(repr(persona1)) # Persona(nombre: Juan, apellido: Perez)
```

- En el ejemplo anterior, se sobrescribe el método `__str__` y `__repr__` en la clase `Persona` para devolver una representación de cadena del objeto que se puede utilizar para recrear el objeto y una representación de cadena legible para el usuario final.

## 3.1. ***Orden de prioridad de llamada de los métodos `__str__` y `__repr__`***

1. **`__str__`** se llama automáticamente cuando se imprime un objeto mediante la función `print`.

2. **`__repr__`** se llama automáticamente cuando se imprime un objeto y no se ha definido el método `__str__`.

# 4. **Método `__format__` en Python**

El método `__format__` se utiliza para personalizar la representación de cadena de un objeto cuando se utiliza con la función `format`.

- La implementación por defecto del método `__format__` es el método `__str__`.

> [!NOTE]
> 
> - Al igual que el método `__str__`, el método `__format__` esta diseñado para devolver una representación de cadena **legible para el usuario final.**

```python
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def __repr__(self):
        return f"{self.__class__.__name__}(nombre: {self.nombre}, apellido: {self.apellido})"

    def __str__(self):
        return f"{self.__class__.__name__}: {self.nombre}, {self.apellido}"

    def __format__(self, format_spec):
        return f"{self.__class__.__name__}: con nombre {self.nombre} y apellido {self.apellido}".format(format_spec)

persona1 = Persona("Juan", "Perez")
print(persona1) # Persona: Juan, Perez
print(repr(persona1)) # Persona(nombre: Juan, apellido: Perez)
print(f'{persona1}') # Persona: con nombre Juan y apellido Perez
```

- En el ejemplo anterior, se sobrescribe el método `__format__` en la clase `Persona` para personalizar la representación de cadena del objeto cuando se utiliza con la función `format` o un `f string`.


