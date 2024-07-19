
<div align="center">

# **Sobrecarga de operadores y constructores en Python**


<p align="center">
  <img src="https://i.postimg.cc/cLT7ZjVV/image-2.png" alt="Aquí va el texto del enlace" width="400">
</p>


</div>

# **Tabla de contenido**
- [**Sobrecarga de operadores y constructores en Python**](#sobrecarga-de-operadores-y-constructores-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Sobrecarga de Operadores en Clases en Python**](#1-sobrecarga-de-operadores-en-clases-en-python)
  - [1.1. ***Operadores Aritméticos***](#11-operadores-aritméticos)
    - [**\_Ejemplo de sobrecarga de operadores aritméticos en una clase en Python**](#_ejemplo-de-sobrecarga-de-operadores-aritméticos-en-una-clase-en-python)
  - [1.2. ***Operadores de Comparación***](#12-operadores-de-comparación)
  - [1.3. ***Operadores de Asignación***](#13-operadores-de-asignación)
  - [1.4. ***Operadores Unarios***](#14-operadores-unarios)
- [2. **Sobrecarga de constructores de Clases**](#2-sobrecarga-de-constructores-de-clases)

# 1. **Sobrecarga de Operadores en Clases en Python**

La **sobrecarga de operadores** en Python permite definir el comportamiento de los operadores en las clases personalizadas. Esto significa que se puede definir cómo se comportan los operadores como `+`, `-`, `*`, `/`, `==`, `!=`, `>`, `<`, `>=`, `<=`, entre otros, en las clases personalizadas.

- Para sobrecargar un operador en una clase en Python **se debe definir un método especial que corresponda al operador que se desea sobrecargar**. Algunos de los métodos especiales más comunes para sobrecargar operadores son:

## 1.1. ***Operadores Aritméticos***

<div align="center">

| Operador | Método especial | Descripción |
|----------|-----------------|-------------|
| `+` | `__add__(self, other)` | Sobrecarga del operador `+` |
| `-` | `__sub__(self, other)` | Sobrecarga del operador `-` |
| `*` | `__mul__(self, other)` | Sobrecarga del operador `*` |
| `/` | `__truediv__(self, other)` | Sobrecarga del operador `/` |
| `//` | `__floordiv__(self, other)` | Sobrecarga del operador `//` |
| `%` | `__mod__(self, other)` | Sobrecarga del operador `%` |
| `**` | `__pow__(self, other)` | Sobrecarga del operador `**` |

</div>

### **_Ejemplo de sobrecarga de operadores aritméticos en una clase en Python**

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Punto(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Punto(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Punto(self.x / other.x, self.y / other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

punto1 = Punto(1, 2)
punto2 = Punto(3, 4)
print(punto1 + punto2) # Output: (4, 6)
print(punto1 - punto2) # Output: (-2, -2)
print(punto1 * punto2) # Output: (3, 8)
print(punto1 / punto2) # Output: (0.3333333333333333, 0.5)
```

## 1.2. ***Operadores de Comparación***

<div align="center">

| Operador | Método especial | Descripción |
|----------|-----------------|-------------|
| `<` | `__lt__(self, other)` | Sobrecarga del operador `<` |
| `>` | `__gt__(self, other)` | Sobrecarga del operador `>` |
| `<=` | `__le__(self, other)` | Sobrecarga del operador `<=` |
| `>=` | `__ge__(self, other)` | Sobrecarga del operador `>=` |
| `==` | `__eq__(self, other)` | Sobrecarga del operador `==` |
| `!=` | `__ne__(self, other)` | Sobrecarga del operador `!=` |

</div>

## 1.3. ***Operadores de Asignación***

<div align="center">

| Operador | Método especial | Descripción |
|----------|-----------------|-------------|
| `-=` | `__isub__(self, other)` | Sobrecarga del operador `-=` |
| `+=` | `__iadd__(self, other)` | Sobrecarga del operador `+=` |
| `*=` | `__imul__(self, other)` | Sobrecarga del operador `*=` |
| `/=` | `__idiv__(self, other)` | Sobrecarga del operador `/=` |
| `//=` | `__ifloordiv__(self, other)` | Sobrecarga del operador `//=` |
| `%=` | `__imod__(self, other)` | Sobrecarga del operador `%=` |
| `**=` | `__ipow__(self, other)` | Sobrecarga del operador `**=` |

</div>

## 1.4. ***Operadores Unarios***

<div align="center">

| Operador | Método especial | Descripción |
|----------|-----------------|-------------|
| `-` | `__neg__(self)` | Sobrecarga del operador `-` |
| `+` | `__pos__(self)` | Sobrecarga del operador `+` |
| `~` | `__invert__(self)` | Sobrecarga del operador `~` |

</div>

# 2. **Sobrecarga de constructores de Clases**

La **sobrecarga de constructores** en Python se refiere a la capacidad de una clase de tener **múltiples constructores** con diferentes parámetros.

- Para sobrecargar un constructor en Python se puede utilizar el método especial `__init__` con valores por defecto en los parámetros o tambien mediante un metodo de clase `@classmethod`.

```python
class Persona:
    def __init__(self, nombre, apellido)
        self.nombre = nombre
        self.apellido = apellido
    
    @classmethod
    def crear_persona_vacia(cls)
        return cls(None, None)
    @classmethod
    def crear_persona_con_valores(cls, nombre, apellido)
        return cls(nombre, apellido)

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}"

persona1 = Persona("Juan", "Perez")
print(persona1) # Output: Nombre: Juan, Apellido: Perez
persona_vacia = Persona.crear_persona_vacia()
print(persona1) # Output: Nombre: None, Apellido: None
persona_con_valores = Persona.crear_persona_con_valores("Ana", "Gomez")
print(persona_con_valores) # Output: Nombre: Ana, Apellido: Gomez
```

- En el ejemplo anterior, se sobrecarga el constructor de la clase **`Persona`** con dos métodos de clase `crear_persona_vacia()` y `crear_persona_con_valores()` que permiten crear instancias de la clase **`Persona`** con valores por defecto o con valores específicos.

  - En el primer objeto **`persona1`** se crea una instancia de la clase **`Persona`** con valores específicos, que es la forma tradicional de crear instancias de una clase.
  
  - En el segundo objeto **`persona_vacia`** se crea un método estático `crear_persona_vacia()` que crea una instancia de la clase **`Persona`** con valores por defecto.
  
  - En el tercer objeto **`persona_con_valores`** se crea un método estático `crear_persona_con_valores()` que crea una instancia de la clase **`Persona`** con valores específicos.







