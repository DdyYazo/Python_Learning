
<div align="center">

# **Manejo de SQL desde Python**

<p align="center">
  <img src="https://i.postimg.cc/j2vCZxjG/image-5.png" alt="Aquí va el texto del enlace">
</p>
<p align="center">
<strong>Diferencias entre `List` vs `Tuples` vs `Sets`</strong>
</p>

</div>

# **Tabla de contenido**
- [**Manejo de SQL desde Python**](#manejo-de-sql-desde-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1.](#1)
  - [26\_file-text\_read.py: Leer archivos de texto (`.txt`) en Python](#26_file-text_readpy-leer-archivos-de-texto-txt-en-python)
    - [1. Manejo de archivos mediante la función `open()`](#1-manejo-de-archivos-mediante-la-función-open)
      - [Puntos a tener en cuenta del codigo anterior](#puntos-a-tener-en-cuenta-del-codigo-anterior)


# 1. 

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


