
<div align="center">

# **Manejo de archivos `txt` y `csv` en Python**

<p align="center">
  <img src="https://i.postimg.cc/RZdGKK9R/image-3.png" alt="Aquí va el texto del enlace">
</p>
<p align="center">
<strong>Diferencias entre `List` vs `Tuples` vs `Sets`</strong>
</p>

</div>

# **Tabla de contenido**
- [**Manejo de archivos `txt` y `csv` en Python**](#manejo-de-archivos-txt-y-csv-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **Manipulación de archivos `txt`**](#1-manipulación-de-archivos-txt)
  - [1.1. ***Modos de apertura de archivos***](#11-modos-de-apertura-de-archivos)
  - [1.2. ***Escribir `w` en archivos de texto (`.txt`)***](#12-escribir-w-en-archivos-de-texto-txt)
    - [1.2.1. **Manejando el juego de caracteres en archivos `txt` mediante el argumento `encoding`**](#121-manejando-el-juego-de-caracteres-en-archivos-txt-mediante-el-argumento-encoding)
  - [1.3. ***Leer `r` archivos de texto (`.txt`)***](#13-leer-r-archivos-de-texto-txt)
    - [1.3.1. **Recorrer el contenido de un archivo de texto con un bucle `for`**](#131-recorrer-el-contenido-de-un-archivo-de-texto-con-un-bucle-for)
  - [1.4. ***Anexar `a` contenido a un archivo `txt`***](#14-anexar-a-contenido-a-un-archivo-txt)
  - [1.5. ***Manejo de archivos con `(with)`***](#15-manejo-de-archivos-con-with)
    - [1.5.1. **Recorrer el contnendo del archivo con bucle `for` dentro del `with`**](#151-recorrer-el-contnendo-del-archivo-con-bucle-for-dentro-del-with)
  - [1.6. ***Usando el `Context Manager` para abrir archivos mediante el bloque `with`***](#16-usando-el-context-manager-para-abrir-archivos-mediante-el-bloque-with)
    - [1.6.1. **Métodos magicos de `Context Manager`**](#161-métodos-magicos-de-context-manager)
  - [read\_csv.py: Manipulación de archivos `csv` en Python](#read_csvpy-manipulación-de-archivos-csv-en-python)
    - [Archivos CSV](#archivos-csv)
- [Módulo 6: Graficas en Python](#módulo-6-graficas-en-python)
  - [charts.py: Generar gráficos utilizando matplotlib en Python](#chartspy-generar-gráficos-utilizando-matplotlib-en-python)
    - [1. Matplotlib](#1-matplotlib)
    - [2. Seaborn](#2-seaborn)
    - [3. Plotly](#3-plotly)


# 1. **Manipulación de archivos `txt`** 

Para leer un archivo de texto en Python, se puede utilizar la función `open()`. 

Esta función toma dos argumentos: 

1. **El nombre del archivo** o ruta del archivo existente

2. El **modo en el que se abre el archivo**:

## 1.1. ***Modos de apertura de archivos***

<div align="center">

| Modo | Descripción |
|------|-------------|
| **read: `'r'`** | Abre el archivo en modo de lectura. Este es el valor por defecto si no se especifica ningún modo. |
| **write: `'w'`** | Abre el archivo en modo de escritura. Crea un nuevo archivo si no existe o trunca el archivo si ya existe. |
| **append: `'a'`** | Abre el archivo en modo de adición. Crea un nuevo archivo si no existe. Si el archivo ya existe, los datos se añaden al final del archivo sin borrar el contenido existente. |
| **create: `'x'`** | Crea un nuevo archivo y lo abre para escritura. Si el archivo ya existe, la operación fallará. |
| `'r+'` | Abre el archivo para lectura y escritura. El archivo debe existir. |
| `'w+'` | Abre el archivo para lectura y escritura. Crea un nuevo archivo si no existe o trunca el archivo si ya existe. |
| `'a+'` | Abre el archivo para lectura y adición. Crea un nuevo archivo si no existe. Si el archivo ya existe, los datos se añaden al final del archivo sin borrar el contenido existente. |

</div>

> [!TIP]
>
> Una buena practica es capturar todo el codigo dentro de un bloque `try-except` para manejar excepciones que puedan surgir al abrir o leer un archivo.

> [!IMPORTANT]
> 
> Por otro lado, es importante recordar que **`'w'` y `'w+'` borrarán el contenido existente del archivo al abrirlo.** *Si quieres añadir contenido a un archivo existente sin borrar el contenido actual, debes usar `'a'` o `'a+'`*.

Adicionalmente tambien **se puede especificar si el tipo de archivo que se va a leer o escribir es de texto o binario**, para ello se puede especificar el argumento `t` para archivos de texto y `b` para archivos binarios.

<div align="center">

| Modo | Descripción | Uso | Resultado |
|------|-------------|-----|-----------|
| `'t'` | Abre el archivo en modo de texto. Este es el valor por defecto si no se especifica ningún modo. | Archivos de texto | `open('archivo.txt', 'rt')` |
| `'b'` | Abre el archivo en modo binario. | imagenes, videos, etc. | `open('archivo.jpg', 'rb')` |

</div>

## 1.2. ***Escribir `w` en archivos de texto (`.txt`)***

Para escribir en un archivo de texto se puede de la siguiente manera:

1. Abrir el archivo utilizando la **función `open()` indicando el nombre del archivo y el modo de apertura en este caso `'w'`** para escritura.

2. Luego, se puede **escribir en el archivo utilizando el método `write()`.**

> [!NOTE]
> 
> **En dado caso que este archivo no exista, se creará en la ruta especificada o de lo contrario se lanzará una excepción que se puede manejar con un bloque `try-except`.**

```python
try:
    file = open('prueba.txt', 'w')
    file.write("Hola, este es un archivo de texto\n")
    file.write("Este es un archivo de texto en Python")
except Exception as e:
    print(e)
finally:
    file.close()
```

- En el código anterior, se abre el archivo `prueba.txt` en modo de escritura `'w'` y se escribe en el archivo utilizando el método `write()`.

> [!IMPORTANT]
>
> Siempre que se abra un archivo, es importante cerrarlo después de usarlo para liberar los recursos del sistema. **Esto se puede hacer utilizando el método `close()`** al final del código.

### 1.2.1. **Manejando el juego de caracteres en archivos `txt` mediante el argumento `encoding`**

Cuando se desea escribir en un archivo de texto en Python, usando caracteres especiales o **caracteres no ASCII**, es importante especificar el juego de caracteres que se utilizará. **Esto se puede hacer especificando el argumento `encoding` al abrir el archivo.**

```python
try:
    file = open('prueba.txt', 'w', encoding='utf-8')
    file.write("Hola, este es un archivo de texto\n")
    file.write("Este es un archivo de texto en Python en español")
except Exception as e:
    print(e)
finally:
    file.close()
```

- En el código anterior, se abre el archivo `prueba.txt` en modo de escritura `'w'` y se especifica el juego de caracteres `utf-8` utilizando el argumento `encoding`. Luego, se escribe en el archivo utilizando el método `write()`. Lo que permite escribir caracteres especiales o no ASCII en el archivo.


## 1.3. ***Leer `r` archivos de texto (`.txt`)***

Para leer un archivo de texto se puede de la siguiente manera:

1. Abrir el archivo utilizando la **función `open()` indicando el nombre del archivo y el modo de apertura en este caso `'r'`** para lectura. 

2. Luego, se puede **leer el contenido del archivo utilizando el método `read()`,` readline()` o `readlines()`.** 

```python
file = open('prueba.txt', 'r', encoding='utf-8')

""" Leer algunos caracteres del archivo usando el método read() """
contenido = file.read(5)
print(contenido) # Hola,

""" Leer lineas completas del archivo usando el método readline() """
contenido = file.readline()
print(contenido) # Hola, este es un archivo de texto

""" Leer todas las lineas del archivo usando el método readlines() """
contenido = file.readlines()
print(contenido) # ['Hola, este es un archivo de texto\n', 'Este es un archivo de texto en Python en español']

file.close() # Cierra el archivo
```

- En el código anterior, se abre el archivo `prueba.txt` en modo de lectura `'r'` y se puede leer el contenido del archivo utilizando los métodos **`read()`**, **`readline()`** o **`readlines()`**. 
  
  - Cabe destacar que el método `readlines()` lee todas las líneas del archivo y las devuelve como una `lista` de cadenas de texto.	Si se desea leer solo una línea, **se puede utilizar el método `readline()` indicando la posición de la línea que se desea leer.**

```python
file = open('prueba.txt', 'r', encoding='utf-8')
print(file.readlines()[1]) # Este es un archivo de texto en Python en español
file.close() # Cierra el archivo
```

### 1.3.1. **Recorrer el contenido de un archivo de texto con un bucle `for`**

Los métodos anteriormente mencionados son útiles para leer el contenido de un archivo de texto pequeño. Sin embargo, **si el archivo es demasiado grande para leerlo en memoria de una sola vez, se puede recorrer el contenido del archivo con un bucle `for`.**

```python
file = open('prueba.txt', 'r', encoding='utf-8')

for line in file:
    print(line)

file.close() # Cierra el archivo
```

## 1.4. ***Anexar `a` contenido a un archivo `txt`***

Para añadir contenido a un archivo de texto existente, se puede abrir el archivo en modo de adición `'a'` y escribir en el archivo utilizando el método `write()`. **Tambien se puede generar una copia del archivo original y añadir contenido a la copia.**

```python
file = open('prueba.txt', 'r', encoding='utf-8')
file2 = open('copia_prueba.txt', 'a', encoding='utf-8')
file2.write(file.read())
file2.write("\nLinea añadida al archivo")
file2.close() # Cierra el archivo
file.close() # Cierra el archivo
```

- En el código anterior, se abre el archivo `prueba.txt` en modo de lectura `'r'` y se abre el archivo `copia_prueba.txt` en modo de adición `'a'`. Luego, se lee el contenido del archivo `prueba.txt` y se escribe en el archivo `copia_prueba.txt`. Finalmente, se añade una línea al archivo `copia_prueba.txt` y se cierran ambos archivos.

## 1.5. ***Manejo de archivos con `(with)`***

**Es una buena práctica** manejar archivos utilizando la declaración `with`, **ya que se encarga de cerrar el archivo automáticamente después de usarlo**, incluso si se lanza una excepción.

```python
with open('mi_archivo.txt', 'r' encoding='utf-8') as archivo:
    contenido = archivo.read()
    print(contenido)
```

- En el código anterior, se abre el archivo `mi_archivo.txt` en modo de lectura `'r'` utilizando la declaración `with` asignando el alias `archivo`. Luego, se lee el contenido del archivo utilizando el método `read()` y se imprime en la consola. **Después de que el bloque `with` se complete, el archivo se cerrará automáticamente.**


### 1.5.1. **Recorrer el contnendo del archivo con bucle `for` dentro del `with`**

Al igual que se puede recorrer el contenido de un archivo con un bucle `for` fuera de un bloque `with`, **también se puede hacer dentro del bloque `with`.** Asi como se muestra en el siguiente ejemplo:

```python
# Abre el archivo en modo de letura ('r+')
with open('mi_archivo.txt','r+') as file:
    for line in file:
        print(line)
# Escribe la cadena de texto  en el archivo 
    file.write("Hola, este es un archivo de texto\n") 
```

## 1.6. ***Usando el `Context Manager` para abrir archivos mediante el bloque `with`***

El `Context Manager` es una forma de trabajar con recursos que necesitan ser limpiados o liberados después de su uso. **En Python, se puede utilizar la declaración `with` para trabajar con archivos, sockets, bases de datos, etc.**

### 1.6.1. **Métodos magicos de `Context Manager`**

Estos métodos se definen en una clase para permitir que la clase actúe como un `Context Manager`. Los métodos mágicos más comunes son `__enter__` y `__exit__`.

- **`__enter__`**: Este método se llama al entrar en el bloque `with`. Se puede utilizar para inicializar recursos o realizar tareas de configuración.

- **`__exit__`**: Este método se llama al salir del bloque `with`. Se puede utilizar para limpiar recursos o realizar tareas de limpieza.

```python
""" Clase que actua como un Context Manager """
class ManejoArchivos:
    def __init__(self, file):
        self.file = file

    def __enter__(self):
      print("Abriendo el archivo" center(50, '-'))
      self.file = open(self.file, 'r' encoding='utf-8')   
      return self.file

    def __exit__(self, exc_type, exc_value, exc_traceback):
      print("Cerrando el archivo" center(50, '-'))
      if self.file:
        self.file.close()

""" Importa la clase ManejoArchivos """
with ManejoArchivos('mi_archivo.txt') as file:
    print(file.read())
```

- En el código anterior, se define una clase `ManejoArchivos` que actúa como un `Context Manager`. La clase tiene dos métodos mágicos `__enter__` y `__exit__`. El método `__enter__` abre el archivo y el método `__exit__` cierra el archivo, confirmando que el archivo este cerrado mediante una condición `if`. Finalmente, se utiliza la declaración `with` para abrir el archivo `mi_archivo.txt` utilizando la clase `ManejoArchivos` y se imprime el contenido del archivo.

> [!IMPORTANT]
>
> Dentro de los parametros del método `__exit__` **es importante indicar el `exc_type`, `exc_value` y `exc_traceback` que se utilizan para manejar excepciones que puedan surgir al abrir o cerrar un archivo.**


## [read_csv.py](./Mod_5_Python_Files_Errors/28_app_read-csv/read_csv.py): Manipulación de archivos `csv` en Python

Python proporciona varias bibliotecas para trabajar con archivos CSV y Excel, como csv y pandas. Aquí te proporciono un ejemplo de cómo puedes manipular estos archivos y la importancia de cada declaración.

### Archivos CSV
Para trabajar con archivos CSV, puedes usar la biblioteca incorporada csv.

- **Ejemlo**
```python
import csv

def run(path):
    with open(path, "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            print(country_dict)

# Si este archivo se está ejecutando como el principal, llama a la función run con la ruta al archivo CSV
if __name__ == "__main__":
    run('./app_read-csv/data.csv')
```
- **Explicación del codigo**
  - `import csv`: Esta línea importa la biblioteca csv de Python, que proporciona funcionalidades para leer y escribir archivos CSV.

  - `def run(path)`: Esta línea define una función llamada run que toma un argumento path. path es la ruta al archivo CSV que quieres leer.
 
  - `with open(path, "r") as csvfile`: Esta línea abre el archivo CSV en modo de lectura. with asegura que el archivo se cierre correctamente después de usarlo.
  
  - `reader = csv.reader(csvfile, delimiter=',')`: Esta línea crea un objeto reader que puede iterar sobre las líneas del archivo CSV. El argumento delimiter=',' especifica que las columnas del CSV están separadas por comas.
  
  - `header = next(reader)`: Esta línea obtiene la primera línea del CSV, que generalmente contiene los encabezados de las columnas.
  
  - `for row in reader`: Esta línea comienza un bucle que itera sobre cada línea restante del CSV.
  
  - `iterable = zip(header, row)`: Esta línea combina los encabezados y los valores de la fila actual en un objeto iterable de pares.
  
  - `country_dict = {key: value for key, value in iterable}`: Esta línea crea un diccionario donde las claves son los encabezados y los valores son los valores de la fila actual.
  
  - `print(country_dict)`: Esta línea imprime el diccionario.

> [!NOTE]
>
> La biblioteca de `csv` *proporciona muchas más funcionalidades para manipular archivos CSV, como escribir datos, filtrar datos, realizar cálculos, etc.*

> [!IMPORTANT]
> ### Fuente para consultar datasets csv
>
> La siguiente fuente se utiliza en su mayoria para tomar datasets compartidos por la comunidad
> <p align="center">
> <a href="https://www.kaggle.com/datasets/iamsouravbanerjee/world-population-dataset">
> <img src="https://i.postimg.cc/8cKYYN3j/imagen-2024-03-11-155704440.png" alt="Aquí va el texto del enlace">
> </a>
> </p>



# Módulo 6: Graficas en Python

## [charts.py](./Mod_6_Python_Charts/29_app_chart_matplotlib/charts.py): Generar gráficos utilizando matplotlib en Python

Python ofrece varias bibliotecas para la visualización de datos, entre las que se incluyen **Matplotlib**, **Seaborn** y **Plotly**.

### 1. Matplotlib 

Es una de las bibliotecas más utilizadas para la creación de gráficos estáticos, animados e interactivos en Python. Matplotlib es altamente personalizable y puede ser usado para crear una amplia variedad de gráficos.

```python
    import matplotlib.pyplot as plt

    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    plt.plot(x, y)
    plt.show()
```
- **Descripción**
  -  En este ejemplo, `import matplotlib.pyplot as plt` importa el módulo `pyplot` de Matplotlib, que proporciona una interfaz para crear gráficos. `plt.plot(x, y)` crea un gráfico de líneas y `plt.show()` muestra el gráfico.

### 2. Seaborn 

Es una biblioteca de visualización de datos basada en Matplotlib que proporciona una interfaz de alto nivel para crear gráficos estadísticos atractivos.

```python
    import seaborn as sns

    tips = sns.load_dataset("tips")
    sns.boxplot(x="day", y="total_bill", data=tips)
```
- **Descripción**
  -  En este ejemplo, `import seaborn as sns` importa la biblioteca Seaborn. `sns.load_dataset("tips")` carga un conjunto de datos incorporado en Seaborn llamado **"tips"**. `sns.boxplot(x="day", y="total_bill", data=tips)` crea un boxplot de la columna **"total_bill"** agrupada por **"day"**.

### 3. Plotly 

Es una biblioteca que permite crear gráficos interactivos.

```python
    import plotly.express as px

    df = px.data.iris()
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
    fig.show()
```
- **Descripción**
  -  En este ejemplo, `import plotly.express as px` importa el módulo `express` de Plotly, que proporciona una interfaz para crear gráficos. `px.data.iris()` carga un conjunto de datos incorporado en Plotly llamado **"iris"**. `px.scatter(df, x="sepal_width", y="sepal_length", color="species")` crea un gráfico de dispersión de las columnas **"sepal_width"** y **"sepal_length"**, coloreado por **"species"**. fig`.show()` muestra el gráfico.



