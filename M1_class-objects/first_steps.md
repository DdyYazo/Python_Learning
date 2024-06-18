
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

# 1. **¿Que es una clase y un objeto en Python?**

<img align='right' width="350px" alt="coding web" src="https://i.postimg.cc/JtVvX2pR/imagen-2024-06-17-173325415.png" style="margin-left: 20px; margin-top: 20px;">

Una **clase** es una `plantilla` para crear `objetos`. 

- Define los atributos y métodos comunes a todos los objetos de un tipo. 

Los **objetos** son `instancias` de una clase. 

- Cada objeto tiene sus propios valores para los atributos de la clase y puede realizar los métodos definidos en la clase

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






