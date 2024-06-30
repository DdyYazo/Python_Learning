
<div align="center">

# **Polimorfismo en Python**


<p align="center">
  <img src="https://i.postimg.cc/fW9mcnTX/image.png" alt="Aquí va el texto del enlace" width="500">
</p>


</div>

# **Tabla de contenido**
- [**Polimorfismo en Python**](#polimorfismo-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Polimorfismo (Multiples formas) en Python**](#1-polimorfismo-multiples-formas-en-python)
  - [1.1. **Ejemplo basico de `Polimorfismo`**](#11-ejemplo-basico-de-polimorfismo)
  - [1.2. **Método que llama a un `método polimorfico`**](#12-método-que-llama-a-un-método-polimorfico)
  - [1.3. **Método `isinstance()` en el polimorfismo**](#13-método-isinstance-en-el-polimorfismo)
  - [1.4. **Ejemplo avanzado de `Polimorfismo`**](#14-ejemplo-avanzado-de-polimorfismo)


# 1. **Polimorfismo (Multiples formas) en Python**

<img align='right' width="300px" alt="coding web" src="https://i.postimg.cc/tRDFgCsq/imagen-2024-06-29-182355934.png" style="margin-left: 20px;">

El polimorfismo en programación se refiere a *la capacidad que tienen los objetos de diferentes clases de responder al mismo mensaje o método de manera única a su propia clase.* En otras palabras, **un objeto puede tener múltiples formas o comportamientos según la clase a la que pertenece.**

Para entenderlo mejor, piensa en **un ejemplo cotidiano**: **Un teléfono móvil** puede realizar varias acciones, como: 

- **hacer llamadas**
- **enviar mensajes de texto**
- **tomar fotos** 

Sin embargo, cada una de estas acciones se realiza de manera única y específica para el teléfono móvil en sí.

## 1.1. **Ejemplo basico de `Polimorfismo`**

**Un objeto puede tener múltiples métodos o funciones asociadas a él, pero cada uno de estos métodos se comporta de manera única y específica para la clase a la que pertenece el objeto**. Por ejemplo, si tienes un objeto de la **clase `Coche`** y otro objeto de la **clase `Avión`**, ambos objetos **pueden tener un método `volar`**, pero **el método `volar` se comportará de manera diferente para cada uno de ellos**, ya que un coche no puede volar, mientras que un avión sí lo puede hacer.

```python

class Coche:
    def volar(self):
        print("Un coche no puede volar")

class Avion:
    def volar(self):
        print("Un avión puede volar")

# Crear objetos de las clases Coche y Avión
coche = Coche()
avion = Avion()

# Llamar al método volar de cada objeto
coche.volar() # Un coche no puede volar
avion.volar() # Un avión puede volar

```
- En el ejemplo anterior, **el método `volar` aunque tiene el mismo nombre, se comporta de manera diferente para cada clase**. Esto es un ejemplo de polimorfismo en Python.

## 1.2. **Método que llama a un `método polimorfico`**

Si se definiera otro método en cualquiera de las dos clases como `conducir`, en este caso dentro de la clase `Avion`, **tendria el mismo efecto pero es necesario primero declarar el objeto que apunta a la clase `Avion` y luego llamar al método `conducir`** para pasar como argumento al objeto que apunta a la clase `Coche` cuando se quiere llamar al método `conducir` de la clase `Avion`

```python

class Coche:
  
    def volar(self):
        print("Un coche no puede volar")

class Avion:

    def volar(self):
        print("Un avión puede volar")
    def conducir(self, vehiculo):
        self.vehiculo = vehiculo
        vehiculo.volar()

# Crear objetos de las clases Coche y Avión
avion = Avion()
avion.conducir(avion) # Un avión puede volar

# Llamar al método conducir de la clase Avión
coche = Coche()
avion.conducir(coche)
```

- En el ejemplo anterior, **se define un método `conducir` en la clase `Avion` que recibe un objeto `vehiculo` y llama al método `volar` del objeto `vehiculo`.** Luego, se crea un objeto de la clase `Coche` y otro de la clase `Avion`, y se llama al método `conducir` de la clase `Avion` con cada uno de los objetos como argumento. Como resultado, **el método `volar` se comportará de manera diferente para cada objeto, lo que es un ejemplo de polimorfismo en Python.**

## 1.3. **Método `isinstance()` en el polimorfismo**

El método `isinstance()` en Python se utiliza para verificar si un objeto es una instancia de una clase o de una clase derivada de ella. Este método devuelve `True` si el objeto es una instancia de la clase especificada, de lo contrario, devuelve `False`.

Por ejemplo, si se desea verificar si un objeto `coche` es una instancia de la clase `Coche`, puedes hacerlo de la siguiente manera:
  
```python
class Coche:
  def volar(self):
      print("Un coche no puede volar")

class Avion:
    def volar(self):
        print("Un avión puede volar")
        
# Crear objetos de las clases Coche y Avión
coche = Coche()
avion = Avion()

# Llamar al método volar de cada objeto
coche.volar() # Un coche no puede volar
avion.volar() # Un avión puede volar

# Verificar si un objeto es una instancia de una clase
print(isinstance(coche, Coche)) # True
print(isinstance(avion, Avion)) # True
print(isinstance(coche, Avion)) # False

```

- En el ejemplo anterior, **se verifica si el objeto `coche` es una instancia de la clase `Coche` y si el objeto `avion` es una instancia de la clase `Avion`.** Ambas verificaciones devolverán `True` ya que `coche` es una instancia de la clase `Coche` y `avion` es una instancia de la clase `Avion`, de lo contrario, devolverá `False`.

> [!NOTE]
>
> Este metodo `isinstance()` es muy útil en el polimorfismo, ya que **permite verificar si un objeto es una instancia de una clase o de una clase derivada de ella.** Sin embargo solo es utilizado para casos extremos, ya que **es una mala practica que los métodos de una clase hagan tantas validaciones de este tipo.**
>

## 1.4. **Ejemplo avanzado de `Polimorfismo`**

En este ejemplo, primero se construye una **`superclase`  (clase padre)** que realizará una primera evaluación de la idoneidad de una cuenta de correo electrónico. Luego, se crean dos clases hijas específicas para una determinada extensión **(sufijo)** en la que se basara el polimorfismo.

```python

class CorreoElectronico:
    def __init__(self, cuenta):
        if not cuenta.endswith(self.sufijo):
            raise ValueError("La cuenta de correo electrónico no es válida")
        self.cuenta = cuenta
      
class CorreoGmail(CorreoElectronico):
    sufijo = "@gmail.com" 
    def send_email(self):
        if not cuenta.count("@") == 1:
            raise ValueError("La cuenta de correo electrónico no es válida")
        print("Enviando correo electrónico a", self.cuenta)

class CorreoHotmail(CorreoElectronico):
    sufijo = "@hotmail.com"
    def send_email(self):
        if not cuenta.count("@") == 1:
            raise ValueError("La cuenta de correo electrónico no es válida")
        print("Enviando correo electrónico a", self.cuenta)

# Crear objetos de las clases CorreoGmail y CorreoHotmail
correo_gmail = CorreoGmail("pepe@gmail.com")
correo_hotmail = CorreoHotmail("pepe2@hotmail.com")

# Llamar al método send_email de cada objeto
correo_gmail.send_email() # Enviando correo electrónico a
correo_hotmail.send_email() # Enviando correo electrónico a

```

- En el ejemplo anterior, **se define una clase `CorreoElectronico` que realiza una primera evaluación de la idoneidad (*veracidad de la cuenta*) de una cuenta de correo electrónico. Luego, se crean dos clases hijas específicas para una determinada extensión (sufijo) en la que se basará el polimorfismo.** Ambas clases hijas tienen un método `send_email` que envía un correo electrónico a la cuenta de correo electrónico especificada. Al crear objetos de las clases `CorreoGmail` y `CorreoHotmail` y llamar al método `send_email` de cada objeto, **el método se comportará de manera diferente para cada objeto, lo que es un ejemplo de polimorfismo en Python.**



