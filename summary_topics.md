# Python_Compre_Funct_Err-Hand


Este repositorio es una excelente fuente de información para cualquier persona que quiera aprender o revisar estos conceptos de Python.

# Tabla de Contenido
- [Python\_Compre\_Funct\_Err-Hand](#python_compre_funct_err-hand)
- [Tabla de Contenido](#tabla-de-contenido)
- [Módulo 5: Manipulación de archivos y errores en Python](#módulo-5-manipulación-de-archivos-y-errores-en-python)
  - [26\_file-text\_read.py: Leer archivos de texto (`.txt`) en Python](#26_file-text_readpy-leer-archivos-de-texto-txt-en-python)
    - [1. Manejo de archivos mediante la función `open()`](#1-manejo-de-archivos-mediante-la-función-open)
      - [Puntos a tener en cuenta del codigo anterior](#puntos-a-tener-en-cuenta-del-codigo-anterior)
  - [27\_file-text\_write.py: Escribir en archivos de texto (`.txt`) en Python](#27_file-text_writepy-escribir-en-archivos-de-texto-txt-en-python)
    - [Modos de apertura de archivos](#modos-de-apertura-de-archivos)
  - [read\_csv.py: Manipulación de archivos `csv` en Python](#read_csvpy-manipulación-de-archivos-csv-en-python)
    - [Archivos CSV](#archivos-csv)
- [Módulo 6: Graficas en Python](#módulo-6-graficas-en-python)
  - [charts.py: Generar gráficos utilizando matplotlib en Python](#chartspy-generar-gráficos-utilizando-matplotlib-en-python)
    - [1. Matplotlib](#1-matplotlib)
    - [2. Seaborn](#2-seaborn)
    - [3. Plotly](#3-plotly)


# Módulo 5: Manipulación de archivos y errores en Python

## [26_file-text_read.py](Mod_5_Python_Files_Errors/26_file-text_read.py): Leer archivos de texto (`.txt`) en Python

### 1. Manejo de archivos mediante la función `open()`
Para leer un archivo de texto, primero debes abrir el archivo utilizando la función `open()`. Luego, puedes leer el contenido del archivo utilizando el método `read()`,` readline()` o `readlines()`.

```python
# Abre el archivo en modo de lectura ('r')
archivo = open('mi_archivo.txt', 'r')

# Lee todo el contenido del archivo
contenido = archivo.read()

# Imprime el contenido
print(contenido)

# Cierra el archivo
archivo.close() 
```

#### Puntos a tener en cuenta del codigo anterior
- `open('mi_archivo.txt', 'r')`: Esta línea abre el archivo mi_archivo.txt en modo de lectura `('r')`. **Si el archivo no existe, se lanzará una excepción.**
- `archivo.close()`: Esta línea cierra el archivo. **Es importante cerrar los archivos después de usarlos para liberar recursos del sistema.**

> [!IMPORTANT]
> 
> ### Manejo de archivos con `(with)`
> 
> **Es una buena práctica** manejar archivos utilizando la declaración `with`, **ya que se encarga de cerrar el archivo automáticamente después de usarlo**, incluso si se lanza una excepción.
> ```python
> with open('mi_archivo.txt', 'r') as archivo:
>    contenido = archivo.read()
>    print(contenido)
> ```


> [!TIP]
> 
> #### Recorrer el contnendo del archivo con bucle `for` dentro del `with`
> 
> Este es un método comúnmente utilizado para leer archivos de texto en Python, especialmente cuando los archivos son demasiado grandes para ser leídos en memoria de una sola vez.
> ```python
> # Abre el archivo en modo de lectura ('r') 
> with open('mi_archivo.txt', 'r') as archivo:
>    # Recorre cada línea del archivo
>    for linea in archivo:
>        # Imprime la línea
>        print(linea)
> ```
> En este código, se recorre cada línea del archivo una por una.


## [27_file-text_write.py](Mod_5_Python_Files_Errors/27_file-text_write.py): Escribir en archivos de texto (`.txt`) en Python

En Python, puedes escribir en archivos de texto utilizando la función incorporada `open()`. Esta función toma dos argumentos: el nombre del archivo y el modo en el que se abre el archivo. Los modos más comunes son `'r'` **para lectura**, `'w'` **para escritura**, `'a'` **para añadir**, y `'r+'`, `'w+'` **para lectura y escritura**.


- **Ejemplo**
	- Para escribir en un archivo de texto, primero debes abrir el archivo en modo de escritura `('w')` o en modo de adición `('a')`. Luego, puedes escribir en el archivo utilizando el método `write()`.

```python
# Abre el archivo en modo de letura ('r+')
with open('mi_archivo.txt','r+',) as file:
    for line in file:
        print(line)
# Escribe la cadena de texto  en el archivo 
    file.write("Hola, este es un archivo de texto\n") 
```

### Modos de apertura de archivos

- `'r'`: Abre el archivo en modo de lectura. Este es el valor por defecto si no se especifica ningún modo.
- `'w'`: Abre el archivo en modo de escritura. Crea un nuevo archivo si no existe o trunca el archivo si ya existe.
- `'a'`: Abre el archivo en modo de adición. Crea un nuevo archivo si no existe. Si el archivo ya existe, los datos se añaden al final del archivo sin borrar el contenido existente.
- `'r+'`: Abre el archivo para lectura y escritura. El archivo debe existir.
- `'w+'`: Abre el archivo para lectura y escritura. Crea un nuevo archivo si no existe o trunca el archivo si ya existe.
> [!NOTE]
> 
> Es importante recordar que **`'w'` y `'w+'` borrarán el contenido existente del archivo al abrirlo.** *Si quieres añadir contenido a un archivo existente sin borrar el contenido actual, debes usar `'a'` o `'a+'`*.


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



