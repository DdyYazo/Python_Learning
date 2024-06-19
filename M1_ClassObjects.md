
<div align="center">

# **Clases y objetos en Python**


<p align="center">
  <img src="https://i.postimg.cc/mD3X5WWq/image-1.png" alt="Aquí va el texto del enlace" width="500">
</p>


</div>

# **Tabla de contenido**
- [**Clases y objetos en Python**](#clases-y-objetos-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **¿Que es una clase y un objeto en Python?**](#1-que-es-una-clase-y-un-objeto-en-python)
  - [1.1. `¿Como declarar una clase en Python?`](#11-como-declarar-una-clase-en-python)
  - [1.2. `¿Como agregar metodos y atributos a una clase en Python?`](#12-como-agregar-metodos-y-atributos-a-una-clase-en-python)
- [2. **Objetos en Python**](#2-objetos-en-python)
  - [2.1. `Objetos con argumentos`](#21-objetos-con-argumentos)
  - [2.3. `Referencia en memoria de un objeto`](#23-referencia-en-memoria-de-un-objeto)
  - [2.4. `Modificando atributos de un objeto`](#24-modificando-atributos-de-un-objeto)
  - [2.4. `Metodos de instancia`](#24-metodos-de-instancia)
  - [2.4. `Mas sobre "sefl" y atributos de instancia`](#24-mas-sobre-sefl-y-atributos-de-instancia)
  - [2.5. `Metodos de instancia con parametros *args y **kwargs`](#25-metodos-de-instancia-con-parametros-args-y-kwargs)

# 1. **¿Que es una clase y un objeto en Python?**

<img align='right' width="350px" alt="coding web" src="https://i.postimg.cc/JtVvX2pR/imagen-2024-06-17-173325415.png" style="margin-left: 20px; margin-top: 20px;">

Una **clase** es una `plantilla` para crear `objetos`. 

- Define los atributos y métodos comunes a todos los objetos de un tipo. 

Los **objetos** son `instancias` de una clase. 

- Cada objeto tiene sus propios valores para los atributos de la clase y puede realizar los métodos definidos en la clase

  - Los **atributos:** son las `características` de un objeto.
  - Los **métodos:** son las `acciones` que un objeto puede realizar. 

>[!NOTE]
>
> Al crear un archivo para una clase en Python, **se recomienda declarar el nombre del archivo con la primera letra en mayúscula y sin espacios.** Ejemplo: `MiClase.py`

<br>
<br>

## 1.1. `¿Como declarar una clase en Python?`
```python
class Persona:
    pass
print(type(Persona)) # <class 'type'>
```

- `class`: Palabra reservada para **definir una clase.** En este caso, la clase se llama `Persona`.

> [!IMPORTANT]
> 
> - `pass`: Palabra reservada para **indicar que el tipo de dato no va a retornar nada.** En este caso, se utiliza para indicar que la clase `Persona` no tiene atributos ni métodos. **Tambien se suele utilizar en funciones o bucles.**


## 1.2. `¿Como agregar metodos y atributos a una clase en Python?`

```python 
class Persona:
    def __init__(self):
        self.nombre = "Juan"
        self.apellido = "Perez"
        self.edad = 28

persona1 = Persona()
persona1 = Persona()
print(f'Hola mi nombre es {persona1.nombre} {persona1.apellido} y tengo {persona1.edad} años')
```

<p align="center">
  <img src="https://i.postimg.cc/Dw84mfSQ/imagen-2024-06-17-185237803.png" alt="Aquí va el texto del enlace" width="500">
</p>
<p align="center"><strong> Metodos y atributos mediante "self"</strong><p>

- `__init__`: **Método especial** que se llama **constructor**. Se ejecuta automáticamente cuando se crea un objeto de la clase. Y sirve para **inicializar los atributos de la clase.**

>[!IMPORTANT]
> ### **`dunder method. (double underscore)`**
> El método `__init__` es especial debido al doble guion bajo al principio y al final del nombre cuando se esta trabajando con clases en Python, **ya que es un hace parte de los `dunder methods` o métodos especiales de Python.**

- `self`: Palabra reservada que se utiliza para **hacer referencia a los atributos y métodos de la clase.** (similar al `this` de otros lenguajes de programación), 
>  [!IMPORTANT]
> Esta siempre debe ser el primer parámetro de los métodos de la clase.


# 2. **Objetos en Python**

## 2.1. `Objetos con argumentos`

```python
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Juan", "Perez", 30) 
print(f'Objeto Persona 1 :{persona1.nombre} {persona1.apellido} {persona1.edad}') 

persona2 = Persona("Karla", "Gomez", 25)
print(f'Objeto Persona 2 :{persona2.nombre} {persona2.apellido} {persona2.edad}')  
```

- **Declaración de los parametros `nombre`, `apellido` y `edad`:** en el método `__init__` de la clase `Persona`.

- **Inicialización de los atributos de la clase `Persona`:** mediante `self` y los argumentos del método `__init__` **(Deben estar nombrados igual).**

- **Declaración de los objetos `persona1` y `persona2`:** con los **argumentos** `"Juan", "Perez", 30` y `"Karla", "Gomez", 25`.

- **Impresión de los objetos:** con los atributos `nombre`, `apellido` y `edad` de los objetos `persona1` y `persona2

## 2.3. `Referencia en memoria de un objeto`
<img align='right' width="350px" alt="coding web" src="https://i.postimg.cc/Y9NYHp96/imagen-2024-06-17-211957066.png" style="margin-left: 20px; margin-top: 20px;">

Estableciendo un punto de interrupción en la línea `persona1 = Persona("Juan", "Perez", 30)`al lado izquierdo de la linea y ejecutando el código en modo debug, se puede observar la referencia en memoria del objeto `persona1`, y la función de la variable `self` en la clase `Persona`, que apunta a la dirección de memoria del objeto.
<br>
<br>

Esto hace un recorrido de cada uno de los atributos de la clase `Persona` y los asigna a la dirección de memoria del objeto `persona1` o los objetos que poseen los atributos de la clase `Persona`.


## 2.4. `Modificando atributos de un objeto`

```python
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Juan", "Perez", 30)
print(f'Objeto Persona 1 :{persona1.nombre} {persona1.apellido} {persona1.edad}') # Output: Juan Perez 30

""" Modificación de los atributos por valores diferentes"""
persona1.nombre = "Juan Carlos"
persona1.apellido = "Gonzales"
persona1.edad = 35
print(f'Objeto Persona 1 :{persona1.nombre} {persona1.apellido} {persona1.edad}') # Output: Juan Carlos Gonzales 35
```

- **Modificación de los atributos de un objeto:** Para modificar los atributos de un objeto, se debe hacer referencia al objeto y al atributo que se desea modificar, y asignarle un nuevo valor. 

  - Ejemplo: `persona1.nombre = "Juan Carlos"` . En este caso, se modifica el atributo `nombre` del objeto `persona1` por `"Juan Carlos"`.

> [!NOTE]
>
> Este es un tema muy de la mano con el **encapsulamiento** en la programación orientada a objetos, ya que se puede controlar el acceso a los atributos de un objeto y se puede modificar los atributos de un objeto de manera controlada.

## 2.4. `Metodos de instancia`

<p align="center">
  <img src="https://i.postimg.cc/4ykQ8jqM/Screenshot-2024-06-18-172302.png" alt="Aquí va el texto del enlace" width="500">
</p>
<p align="center"><strong> Diagrama UML de la clase "Persona" y sus metodos de instancia</strong><p>

```python
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, tu edad es: {self.edad}')

persona1 = Persona("Juan", "Perez", 30)
persona1.mostrarDetalle() # Output: Persona: Juan Perez, tu edad es: 30
```

- **Declaración de un método de instancia:** Los metodos de instancia son **funciones** que se definen dentro de una clase y se pueden llamar desde un objeto de la clase mediante la notación de punto `(.)` ya que estas hacen parte del nivel de la clase y se declaran mediante la palabra reservada `def`.

  - En este caso, se declara el método `mostrarDetalle` que imprime los atributos `nombre`, `apellido` y `edad` del objeto. Y al llamarlo con el objeto `persona1`, mediante la notación de punto `(.)` se imprime el mensaje con los atributos del objeto. 

> [!IMPORTANT]
>
> Cuando se hace referencia a los atributos de la clase en un método de instancia, **se debe hacer mediante el atributo `self` para acceder a estos.**


## 2.4. `Mas sobre "sefl" y atributos de instancia`

```python
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, tu edad es: {self.edad}')

persona1 = Persona("Juan", "Perez", 30)
persona1.mostrarDetalle() # Output: Persona: Juan Perez, tu edad es: 30

""" Agregar un nuevo atributo a un objeto que no es visible por otros objetos"""
persona1.telefono = "123456789"

""" Llamar al metodo no desde el objeto sino directamente desde la clase"""
Persona.mostrarDetalle(persona1) # Output: Persona: Juan Perez, tu edad es: 30
print(persona1.telefono) # Output: 123456789

persona2 = Persona("Karla", "Gomez", 25)
print(persona2.telefono) # Error: AttributeError: 'Persona' object has no attribute 'telefono'

```
- **Atributos de un objeto:** Se pueden agregar atributos a un objeto que no son visibles por otros objetos. 

  - En este caso, se agrega el atributo `telefono` al objeto `persona1` con el valor `"123456789"`. Y al llamar al método `mostrarDetalle` desde la clase `Persona` con el objeto `persona1`, se imprime el mensaje con los atributos del objeto.
  
> [!IMPORTANT]
>
> Un atributo que hace parte de un objeto pero no de la clase no es un caso común en la programación orientada a objetos con Python y puede llevar a problemas de mantenimiento y de lectura del código. Por lo que se recomienda **no agregar atributos a un objeto que no sean visibles por otros objetos.**

- **Llamada a un método desde la clase:** Se puede llamar a un método de instancia desde la clase `Persona` con el objeto `persona1` mediante la notación de punto `(.)` y pasando el objeto como argumento al método.  
  
  - En este caso, se llama al método `mostrarDetalle` desde la clase `Persona` con el objeto `persona1` y se obtiene el mismo resultado que al llamar al método con el objeto `persona1`. Pero **no es una buena práctica** ya que se pierde la referencia al objeto y se puede perder el control de los atributos del objeto.

## 2.5. `Metodos de instancia con parametros *args y **kwargs`

```python
class Persona:
    def __init__(self, nombre, apellido, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido}, tu edad es: {self.edad}' y tambien tienes los siguientes valores de una tupla: {self.args} y un diccionario: {self.kwargs}'

persona1 = Persona("Juan", "Perez", 30, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, , telefono="123456789", ciudad = "Bogota")
```

- **Parametros** ***args** y ****kwargs:** Se pueden agregar parametros `*args` y `**kwargs` a un método de instancia para recibir una tupla de argumentos y un diccionario de argumentos con nombre.

  - En este caso, se agregan los parametros `*args` y `**kwargs` al método `__init__` de la clase `Persona` para recibir una tupla de argumentos y un diccionario de argumentos con nombre. Y se inicializan los atributos `args` y `kwargs` con los valores de los parametros `*args` y `**kwargs`.

  - Al llamar al método `mostrarDetalle` con el objeto `persona1`, se imprime el mensaje con los atributos del objeto y los valores de los parametros `*args` y `**kwargs`.

> [!IMPORTANT]
>
> Al declarar los argumentos `*args` y `**kwargs` en el objeto `persona1`, **no se pueden duplicar los argumentos ya existentes como por ejemplo `nombre`, `apellido` y `edad`** ya que estos ya están declarados en el método `__init__` de la clase `Persona`.
