
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
- [1. **Instalación del módulo de `PostgreSQL` en Python**](#1-instalación-del-módulo-de-postgresql-en-python)
- [2. **Conexión a la base de datos**](#2-conexión-a-la-base-de-datos)
- [3. **Manejando PostgreSQL desde Python mediante la librería `psycopg2`**](#3-manejando-postgresql-desde-python-mediante-la-librería-psycopg2)
  - [3.1. ***Primera query a la base de datos: métodos `cursor()`, `execute()` y `fetchall()`***](#31-primera-query-a-la-base-de-datos-métodos-cursor-execute-y-fetchall)
  - [3.2. ***Uso de `with` y `psycopg2` para manejar la conexión a la base de datos y el objeto `cursor()`***](#32-uso-de-with-y-psycopg2-para-manejar-la-conexión-a-la-base-de-datos-y-el-objeto-cursor)
  - [3.2. ***Uso de la función `fetchone()` para obtener un solo registro de la consulta***](#32-uso-de-la-función-fetchone-para-obtener-un-solo-registro-de-la-consulta)
  - [3.3. ***Los `placeholders` más comunes en las consultas SQL***](#33-los-placeholders-más-comunes-en-las-consultas-sql)


# 1. **Instalación del módulo de `PostgreSQL` en Python**

Para poder trabajar con `PostgreSQL` desde `Python`, es necesario instalar el módulo `psycopg2`. Para ello, se debe ejecutar el siguiente comando en la terminal:

```bash
pip install psycopg2
```

# 2. **Conexión a la base de datos**

Una buena practica para establecer la conexión a una base de datos de `PostgreSQL` o cualquier otro **RDBMS** desde `Python` es **estableciendola dentro de un `try` y `except`para capturar el error en caso que la conexión no se pueda establecer.** 

A continuación se muestra un ejemplo de cómo se puede establecer la conexión a una base de datos `PostgreSQL`:

```python
import psycopg2

try:
    connection = psycopg2.connect(
        user="postgres",
        password="password",
        host="127.0.0.0",	
        port="5432",
        database="database_name"
    )
    print("Conexión exitosa", "\n")
    print(connection)
except psycopg2.Error as e:
    print("Error al conectar a la base de datos", e)
    connection.close()
```

- En el código anterior, se establece la conexión a la base de datos `PostgreSQL` dentro de un bloque `try` y `except`. Dentro del bloque `try`, se declara una variable `connection` que almacena la conexión a la base de datos, teniendo en cuenta los siguientes parámetros:
    - **`user`:** Nombre de usuario de la base de datos, que por defecto es `postgres`.
    
    - **`password`:** Contraseña del usuario de la base de datos.
    
    - **`host`:** Dirección IP del servidor de la base de datos, que por defecto es `
    
    - **`port`:** Puerto de conexión a la base de datos, que por defecto es `5432`.
    
    - **`database`:** Nombre de la base de datos a la que se desea conectar.

Posteriormente en el bloque `except`, se captura el error en caso que la conexión no se pueda establecer, mostrando un mensaje de error y cerrando la conexión a la base de datos con el método `close()`.

# 3. **Manejando PostgreSQL desde Python mediante la librería `psycopg2`**

## 3.1. ***Primera query a la base de datos: métodos `cursor()`, `execute()` y `fetchall()`***

Para realizar una consulta a la base de datos, se puede hacer uso del método `cursor()` de la conexión a la base de datos, el cual retorna un objeto de tipo `cursor` que permite ejecutar consultas a la base de datos a traves del método `execute()`. 
- Ademas, para obtener los resultados de la consulta, se puede hacer uso del método `fetchall()` del objeto `cursor`.

```python

# Codigo de conexión a la base de datos

cursor = connection.cursor()
sentence = "SELECT * FROM table_name"
cursor.execute(sentence)
registros = cursor.fetchall()

cursor.close()
connection.close()
```

- En el código anterior, s**e declara una variable `cursor` que almacena el objeto de tipo `cursor`** que permite ejecutar consultas a la base de datos.

- Posteriormente, **se declara una variable `sentence` que almacena la consulta** que se desea realizar a la base de datos. 

- Luego, **se ejecuta la consulta a través del método `execute()` del objeto `cursor`,** pasando como argumento la variable `sentence`. 

- Finalmente, **se almacenan los resultados de la consulta en la variable `registros` a través del método `fetchall()`** del objeto `cursor`.

- Por último, **se cierra el objeto `cursor` y la conexión a la base de datos** con los métodos `close()`.

## 3.2. ***Uso de `with` y `psycopg2` para manejar la conexión a la base de datos y el objeto `cursor()`***

Una buena práctica para manejar la conexión a la base de datos y el objeto `cursor` **es hacer uso de la sentencia `with` de `Python`, la cual permite manejar la conexión a la base de datos y el objeto `cursor` de forma automática, cerrando la conexión y el objeto `cursor` al finalizar el bloque de código**. Al igual que el caso anterior en caso de error manejarlo con `try` y `except`.

```python

# Codigo anterior de la conexión a la base de datos
try: 
    with conn:
        with conn.cursor() as curs:
            sentence = 'SELECT * FROM persona'
            curs.execute(sentence)
            registro = curs.fetchall()
            print(registro)
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
```

- En el código anterior, se hace uso de la sentencia `with` para manejar la conexión a la base de datos y el objeto `cursor` de forma automática. Además, se hace uso de la sentencia `try`, `except` y `finally` para capturar los errores en caso que la conexión no se pueda establecer.

> [!IMPORTANT]
>
> No obstante **es importante tener en cuenta que la conexión a la base de datos se debe cerrar manualmente, en este caso dentro del bloque `finally`**

## 3.2. ***Uso de la función `fetchone()` para obtener un solo registro de la consulta***

En caso que se desee obtener un solo registro de la consulta, se puede hacer uso de la función `fetchone()` del objeto `cursor`.

```python

# Codigo anterior de la conexión a la base de datos

try: 
    with conn:
        with conn.cursor() as curs:
            sentence = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = input("Ingrese el id de la persona: "  )
            curs.execute(sentence, (id_persona,))
            registro = curs.fetchone()
            print(registro)
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
```

- En el código anterior, se hace uso de la función `fetchone()` para obtener un solo registro de la consulta. Para ello:
  
  - En la variable `sentence` se declara la consulta que se desea realizar a la base de datos, pasando como argumento el id de la persona a través de placeholders `%s`.
  
  - Se declara una variable `id_persona` que almacena el id de la persona solicitado al usuario mediante la función `input()`.
  
  - Luego, considerando que el registro se imprime en un tupla, en el objeto cursor **se ejecuta la consulta a través del método `execute()`, pasando como argumento la variable `sentence` y el id de la persona como una tupla `(id_persona,)`**.
  
  - Finalmente, se almacena el resultado de la consulta en la variable `registro` a través de la función `fetchone()` del objeto `cursor`.

## 3.3. ***Los `placeholders` más comunes en las consultas SQL***

<div align="center">

| Placeholder | Tipo de valor | Ejemplos de uso en Python |
|-------------|--------------|---------|
| `%s` | Para valores de tipo `string` | `cursor.execute("SELECT * FROM persona WHERE nombre = %s", ("Juan",))` |
| `%d` | Para valores de tipo `int` | `cursor.execute("SELECT * FROM persona WHERE id_persona = %d", (1,))` |
| `%f` | Para valores de tipo `float` | `cursor.execute("SELECT * FROM persona WHERE salario = %f", (1000.0,))` |
| `%b` | Para valores de tipo `bytes` | `cursor.execute("SELECT * FROM persona WHERE foto = %b", (b'foto',))` |
| `%r` | Para valores de tipo `raw` | `cursor.execute("SELECT * FROM persona WHERE foto = %r", (b'foto',))` |
| `%y` | Para valores de tipo `date` | `cursor.execute("SELECT * FROM persona WHERE fecha_nacimiento = %y", (date(1990, 1, 1),))` |
| `%t` | Para valores de tipo `time` | `cursor.execute("SELECT * FROM persona WHERE hora_nacimiento = %t", (time(12, 0, 0),))` |
| `%a` | Para valores de tipo `array` | `cursor.execute("SELECT * FROM persona WHERE hobbies = %a", (['futbol', 'natacion'],))` |
| `%j` | Para valores de tipo `json` | `cursor.execute("SELECT * FROM persona WHERE datos = %j", ({"nombre": "Juan", "edad": 30},))` |
| `%p` | Para valores de tipo `path` | `cursor.execute("SELECT * FROM persona WHERE foto = %p", (Path("foto.jpg"),))` |

</div>


