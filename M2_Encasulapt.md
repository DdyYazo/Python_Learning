
<div align="center">

# **Encapsulamiento en Python**


<p align="center">
  <img src="https://i.postimg.cc/505FVqmK/image-1.png" alt="Aquí va el texto del enlace" width="500">
</p>


</div>

# **Tabla de contenido**
- [**Encapsulamiento en Python**](#encapsulamiento-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **¿Qué es el encapsulamiento?**](#1-qué-es-el-encapsulamiento)
- [2. **Métodos `getter` y `setter`**](#2-métodos-getter-y-setter)
  - [2.1. **`Método getter`**](#21-método-getter)
    - [2.1.1 **`Variables de solo lectura`**](#211-variables-de-solo-lectura)
  - [2.2. **`Método setter`**](#22-método-setter)
  - [2.4. **`Encapsulamiento de atributos en un solo método getter y setter`**](#24-encapsulamiento-de-atributos-en-un-solo-método-getter-y-setter)
- [3. **Uso de `Módulos` y `Clases` en Python**](#3-uso-de-módulos-y-clases-en-python)
- [4. **Destructor de objetos de una clase (práctica no tan común)**](#4-destructor-de-objetos-de-una-clase-práctica-no-tan-común)

# 1. **¿Qué es el encapsulamiento?**

Es un **mecanismo que permite restringir el acceso a ciertos `métodos` y `atributos` de un objeto**, con el fin de prevenir modificaciones no deseadas y garantizar la integridad de los datos.

En Python, el encapsulamiento se logra mediante la **convención de nombres**. Si un atributo o método comienza con dos guiones bajos `__`, se considera privado y no se puede acceder desde fuera de la clase. 

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
   
   def mostrar_nombre(self):
        print(f'Persona: Hola {self.__nombre} tu edad es: {self.edad}')

p = Persona('Juan', 25)
print(p.__nombre) # AttributeError: 'Persona' object has no attribute '__nombre'
```

- En el ejemplo anterior, la variable `__nombre` es privada y no se puede acceder desde fuera de la clase. Al intentar acceder a ella, se genera un error de tipo `AttributeError`. 

> [!NOTE]
>
> Normalmente en Python se hace referencia a un atributo de encapsulamiento como `privado`, cuando se indica un solo guion bajo `(_nombre)`, pero si se quiere manejar la accesibilidad de un atributo con mas control de estos se utilizan los métodos `getter` y `setter`.

# 2. **Métodos `getter` y `setter`**

## 2.1. **`Método getter`**

Es un método que se utiliza para **obtener el valor de un atributo de la clase**. En Python, se puede implementar un método `getter` utilizando la convención de nombres `@property`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

p = Persona('Juan', 25)
print(p.nombre) # Juan
print(p.edad) # 25
```

- En el ejemplo anterior, los métodos `get_nombre` y `get_edad` son métodos `getter` que permiten obtener el valor de los atributos `__nombre` y `__edad` respectivamente. 

### 2.1.1 **`Variables de solo lectura`**

En Python, también es posible **crear atributos de solo lectura** utilizando únicamente el método `getter` y no el método `setter`. De esta forma, el atributo solo se puede leer y no se puede modificar.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

p = Persona('Juan', 25)
print(p.nombre) # Juan
print(p.edad) # 25
	
```

- En el ejemplo anterior, los atributos `__nombre` y `__edad` son de solo lectura, ya que solo se ha implementado el método `getter` y no el método `setter`. Por lo tanto, **no se pueden modificar los valores de estos atributos**.

## 2.2. **`Método setter`**

Es un método que se utiliza para **modificar el valor de un atributo de la clase**. En Python, se puede implementar un método `setter` utilizando la convención de nombres `@nombre.setter`.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

p = Persona('Juan', 25)
p.nombre = 'Pedro'
p.edad = 30
print(p.nombre) # Pedro
print(p.edad) # 30
```

- En el ejemplo anterior, los métodos `set_nombre` y `set_edad` son métodos `setter` que permiten **modificar el valor de los atributos `__nombre` y `__edad`** haciendo referencia al metodo `getter` de cada atributo, mediante el decorador `@nombre.setter` y luego estableciendolo como un metodo `setter` para modificar el valor de los atributos. Ademas **es importante tener en cuenta que dentro del metodo `setter` se debe especificar el parametro que se va a modificar que en este caso es `nombre` y `edad` respectivamente.**

> [!IMPORTANT]
>
> Aunque se puede acceder a los atributos privados de una clase en Python, **no es una buena práctica**. Es preferible **utilizar métodos `getter` y `setter` para acceder y modificar los atributos de una clase, ya que esto permite un mayor control sobre el acceso** a los datos y garantiza la integridad de los mismos.



## 2.4. **`Encapsulamiento de atributos en un solo método getter y setter`**

En Python, también es posible **encapsular varios atributos en un solo método `getter` y `setter`**. De esta forma, se puede acceder y modificar varios atributos a la vez.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def datos(self):
        return self.__nombre, self.__edad

    @datos.setter
    def datos(self, datos):
        self.__nombre, self.__edad = datos

```

- En el ejemplo anterior, los atributos `__nombre` y `__edad` se han encapsulado en un solo método `getter` y `setter` llamado `datos`. De esta forma, se puede acceder y modificar ambos atributos a la vez como si fuera una **`tupla`**.

# 3. **Uso de `Módulos` y `Clases` en Python**

Todo archivo con extensión `.py` en Python es considerado un módulo. Un módulo puede contener variables, funciones y clases. En este caso para acceder por ejemplo a la clase `Persona` que se encuentra en el archivo `persona.py` se debe importar el módulo `Persona` y luego instanciar la clase `Persona`.

```python
from persona import Person as pl

people = pl('Juan', 25)
people.mostrar_detalle() # Juan 25
```
- En el ejemplo anterior, se importa la clase `Persona` del módulo `persona` y se instancia la clase `Persona` con los valores `Juan` y `25`. Luego se llama al método `mostrar_detalle` para mostrar los valores de la clase `Persona`. 

- Sin embargo en algunos casos puede haber objetos ya instanciados de la clase `Persona` lo que hara que se imprima en el archivo que importa el modulo a lo cual no se desea acceder al importar el módulo, por lo que se debe establer un `entry point` en el archivo `persona.py` que tiene el name de `__main__` para que solo se ejecute el código del archivo cuando se ejecute el archivo `persona.py` directamente y no al importar el módulo.

```python
if __name__ == '__main__':
    people = Person('Juan', 25)
    people.mostrar_detalle()
```

# 4. **Destructor de objetos de una clase (práctica no tan común)**

En Python, el método `__del__` es un método especial (`dunder method`) que se utiliza para **destruir un objeto de una clase**. Este método se llama automáticamente cuando el objeto ya no se necesita y se libera la memoria que ocupaba.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    def __del__(self):
        print(f'Persona: {self.__nombre} ha sido eliminada')

p = Persona('Juan', 25)
del p # Persona: Juan ha sido eliminada
```

- En el ejemplo anterior, el método `__del__` se llama automáticamente cuando se elimina el objeto `p` con la instrucción `del p`. En este caso, se imprime un mensaje indicando que el objeto ha sido eliminado.

> [!IMPORTANT]
>
> El método `__del__` no se recomienda utilizarlo en Python, ya que **no se puede predecir cuándo se llamará** y **puede causar problemas de rendimiento**. ademas que es una anotación explicita no tan comunmente utilizada, Por lo tanto, es preferible utilizar el **método `__exit__`** de la clase `contextlib` para liberar recursos y cerrar conexiones de forma segura.


