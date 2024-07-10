
<div align="center">

# **Manejo y procesamiento de documentos `JSON` en Python** 

<p align="center">
  <img src="https://i.postimg.cc/wjjDKP8X/image-4.png" alt="Aquí va el texto del enlace">
</p>
<p align="center">
<strong>Diferencias entre `List` vs `Tuples` vs `Sets`</strong>
</p>

</div>

# **Tabla de contenido**
- [**Manejo y procesamiento de documentos `JSON` en Python**](#manejo-y-procesamiento-de-documentos-json-en-python)
- [**Tabla de contenido**](#tabla-de-contenido)
- [1. **¿Qué es `JSON`?**](#1-qué-es-json)
- [2. **¿En que se usa el formato `JSON`?**](#2-en-que-se-usa-el-formato-json)
- [3. **¿Cómo se ve un archivo `JSON`?**](#3-cómo-se-ve-un-archivo-json)
  - [3.1. ***Visores online de archivos `JSON`***](#31-visores-online-de-archivos-json)
- [4. **Manejo de archivos `JSON` en Python**](#4-manejo-de-archivos-json-en-python)
  - [4.1. ***Lectura de archivos `JSON` mediante el método `load()`***](#41-lectura-de-archivos-json-mediante-el-método-load)
    - [4.1.1. **Usando la libreria `urllib` para leer un archivo `JSON` proveniente de una URL**](#411-usando-la-libreria-urllib-para-leer-un-archivo-json-proveniente-de-una-url)
    - [4.1.2. **Filtrar información de un archivo `JSON` a traves de un ciclo `for`**](#412-filtrar-información-de-un-archivo-json-a-traves-de-un-ciclo-for)
  - [4.2. ***Escritura de archivos `JSON` mediante el método `dump()`***](#42-escritura-de-archivos-json-mediante-el-método-dump)


# 1. **¿Qué es `JSON`?**

Los archivos `JSON` (***JavaScript Object Notation***) **son un formato de intercambio de datos ligero que es fácil de leer y escribir para los seres humanos y fácil de analizar y generar para las máquinas.** 

- Se basa en **un subconjunto del Lenguaje de Programación JavaScript**, 
  
  - **Standard ECMA-262 3ª Edición - Diciembre 1999. `JSON` es un formato de texto que es completamente independiente del lenguaje** pero utiliza convenciones que son familiares para los programadores de la familia de lenguajes C, incluidos `C`, `C++`, `C#`, `Java`, `JavaScript`, `Perl`, `Python` y muchos otros. Estas propiedades hacen que `JSON` sea un lenguaje ideal para el intercambio de datos.

# 2. **¿En que se usa el formato `JSON`?**

<img align="right" src="https://i.postimg.cc/7LDzh126/Screenshot-2024-07-08-172557.png" alt="Aquí va el texto del enlace" style="width:250px;"/>

- `JSON` por lo general **se utiliza para el intercambio de datos dentro del campo del `web services` o `APIs` (*Application Programming Interfaces*).**

# 3. **¿Cómo se ve un archivo `JSON`?**

- **En un caso real para la estructura de un archivo `JSON` se suele representar en un `Array` de `Objects` o un `Object` de `Arrays`, como por ejemplo la siguiente estructura básica:**

```json
{
  "personas": [
    {
      "nombre": "Juan Perez",
      "edad": "28"
    },
    {
      "nombre": "Karla Gomez",
      "edad": "32"
    },
    {
      "nombre": "Carlos Lara",
      "edad": "35"
    },
    {
      "nombre": "María Esparza",
      "edad": "22"
    },
    {
      "nombre": "Pedro Santos",
      "edad": "40"
    }
  ],
  "total": 5,
  "mensaje": "exitoso"
}
```

- **En este caso, el archivo `JSON` contiene un `Object` con tres `keys` (`personas`, `total` y `mensaje`), donde `personas` es un `Array` de `Objects` que contiene la información de cada persona.**

## 3.1. ***Visores online de archivos `JSON`***

<div align="center">

| | |
|:-------------------------:|:-------------------------:|
| [![](https://i.postimg.cc/44jt9H7z/imagen-2024-07-08-180344750.png)](https://jsonviewer.stack.hu/#http://globalmentoring.com.mx/api/personas.json) | [![Aquí va el texto del enlace](https://i.postimg.cc/CKfpd2WC/imagen-2024-07-08-180609100.png)](https://jsoneditoronline.org/#left=local.vemate&right=local.wiruhi) |


</div>

# 4. **Manejo de archivos `JSON` en Python**

- **Para el manejo de archivos `JSON` en Python se puede utilizar la librería `json` que viene por defecto en la instalación de Python.**

```python
import json
```

## 4.1. ***Lectura de archivos `JSON` mediante el método `load()`***

- **Para leer un archivo `JSON` en Python se puede utilizar el método `load()` de la librería `json` que permite cargar el contenido de un archivo `JSON` en un objeto de tipo `dict`.**

### 4.1.1. **Usando la libreria `urllib` para leer un archivo `JSON` proveniente de una URL**

En muchos casos es necesario leer información en formato `JSON` desde una URL, para ello se puede utilizar la librería `urllib` o `requests` para leer el contenido de la URL y luego cargarlo en un objeto `dict` con la librería `json`.

```python	
import urllib.request
import json

url = "http://globalmentoring.com.mx/api/personas.json"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
req = urllib.request.Request(url, data=None, headers=headers)

# Obtener el contenido de la URL
url = urllib.request.urlopen(req)
body = url.read()
print(body)

# Parsear el contenido que se obtiene en formato binario a un formato JSON

json_data = json.loads(body.decode("utf-8"))
print(json_data)
```

- En el código anterior se obtiene el contenido de la URL teniendo en cuenta los siguientes pasos:

  1. Se declara una variable `url` que almacena la URL de donde se va a obtener el archivo `JSON`.

  2. Se declara una variable `headers` la cual es necesario en la libreria `urllib` para traer los encabezados de la URL que se va a leer.
  
  3. Se declara una variable `req` que es la petición que se va a realizar a la URL, en este caso se utiliza la función `Request` de la librería `urllib` que recibe como parámetros la URL, los datos que se van a enviar y los encabezados.
  
  4. Se obtiene el contenido de la URL con la función `urlopen()` de la librería `urllib` que recibe como parámetro la petición `req`.
  
  5. Se lee el contenido de la URL con la función `read()` que retorna el contenido de la URL en formato binario.
  
  6. Posterioemente se parsea el contenido que se obtiene en formato binario a un formato `JSON` con la función `loads()` de la librería `json` que recibe como parámetro el contenido de la URL en formato binario y se decodifica a formato `utf-8`.

### 4.1.2. **Filtrar información de un archivo `JSON` a traves de un ciclo `for`**

- **Para filtrar información de un archivo `JSON` se puede recorrer los `keys` del objeto `dict` que se obtiene al cargar el archivo `JSON` y luego acceder a los valores de cada `key`.** En este caso para obtener los nombres de las personas se puede acceder a la `key` `personas` y luego al `array` de `personas` para obtener el `nombre` de cada persona y su `edad`.

```python
# Resto de codigo del ejemplo anterior

json_data = json.loads(body.decode("utf-8"))

print('Nombres de las personas:', '\n' center(50, '-'))
for persona in json_data['personas']:
    print(f'Persona: {persona["nombre"]}, {persona['edad']}')

```

- En el código anterior se recorre el objeto `dict` que se obtiene al cargar el archivo `JSON` y se accede a la `key` `personas` para obtener la información de cada persona, en este obteniendo del `array` de `personas` la `key` `nombre` y `edad` de cada persona.

Tambien se puede acceder a la `key` `total` y `mensaje` para obtener el total de personas y un mensaje de exito.

```python

# Resto de codigo del ejemplo anterior
print(f'Total de personas: {json_data["total"]}')
print(f'Mensaje extraido: {json_data["mensaje"]}')
  
```

## 4.2. ***Escritura de archivos `JSON` mediante el método `dump()`***

- **Para escribir un archivo `JSON` en Python se puede utilizar el método `dump()` de la librería `json` que permite guardar un objeto de tipo `dict` en un archivo `JSON`.** Pero es importante tener en cuenta que el archivo `JSON` se debe guardar en formato `utf-8` para que pueda ser leído correctamente.

```python
# Resto de codigo del ejemplo anterior
url = urllib.request.urlopen(req)
body = url.read()

# Cambiar el formato binario a formato JSON para poder escribirlo en un archivo
json_data = json.loads(body.decode("utf-8"))

# Escribir el contenido en un archivo JSON (si no existe lo crea)
with open('personas.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)

print('Archivo JSON creado exitosamente')  

```

- En el código anterior se obtiene el contenido de la URL y se parsea el contenido que se obtiene en formato binario a un formato `JSON` para poder escribirlo en un archivo `JSON` con la función `dump()` de la librería `json` que recibe como parámetros el contenido `JSON`, el archivo donde se va a guardar, el formato `utf-8`, `ensure_ascii=False` para que no se escape los caracteres especiales y `indent=4` para que el archivo `JSON` tenga una identación de 4 espacios.
