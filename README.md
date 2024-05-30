# python-pip-environment
Esta es una recopilación de las utilidades y comandos implementados para pip y entornos virtuales de python


# 1. Comandos Iniciales para la instalación de paquetes y entornos para Python

## Instalación en Windows con WSL
1.  Instalación de gestor de paquetes de dependencias
```sh
sudo apt install-get -y python3-pip
```

2. Verificar Instalación del gestor
```sh
pip3 -V
```

3. Dependencias en entorno profesional
```sh
sudo apt-get install -y build-essential libssl-dev libffi-dev python3-dev
```

## Flujo de trabajo en python

### [main.py](game/main.py): Game Project
**Para correr el juego debes seguir las siguientes instrucciones en la terminal:**

```sh
cd game
python3 main.py
```

# 2. PIP y Entornos Virtuales

## 2.1. ¿Que es pip?

PIP es el gestor de paquetes de python, es posible buscar librerías en la pagina [pypi.org](https://pypi.org).

- Ver la versión de pip `pip3 -v`. 
- Instalación de paquetes `pip3 install <libreria>`.
- Listar las librerías que se tienen en el entorno de python global `pip3 list`.
- Listar todas las librerías de python instaladas por el usuario `pip3 freeze`.


## 2.2. ¿Que es un entorno o ambiente virtual?
Los entornos virtuales en Python son una herramienta muy útil que permite mantener separadas las dependencias requeridas por diferentes proyectos. En esencia, un entorno virtual es un directorio que contiene una instalación de Python de una versión particular, además de unos cuantos paquetes adicionales.

### Ejemplo de un `venv` "Virtual Environment"
Imagina que estás trabajando en dos proyectos de Python: `ProyectoA` y `ProyectoB`. **`ProyectoA` requiere la versión 1.0** de una librería llamada `LibreriaX`, **pero `ProyectoB` necesita la versión 2.0** de la misma librería. Si instalas todo en el mismo entorno de Python (el entorno global), no podrías satisfacer las dependencias de ambos proyectos al mismo tiempo.

<p align="center">
  <img src="https://i.postimg.cc/dVpGvSp9/imagen-2024-03-18-145755787.png" alt="Aquí va el texto del enlace">
</p>

Aquí es donde los entornos virtuales son útiles. **Puedes crear un entorno virtual para cada proyecto y luego instalar las versiones específicas de las librerías que cada proyecto necesita.** 

<p align="center">
  <img src="https://i.postimg.cc/xCymvjCs/imagen-2024-03-18-145826469.png" alt="Aquí va el texto del enlace">
</p>

### Caracteristicas de los `venv`
- Permiten utilizar varios sistemas operativos en un mismo equipo físico

- Permiten instalar y utilizar diferentes aplicaciones y tecnologías de manera segura, sin tener que hacer cambios permanentes en el sistema operativo principal

- Pueden ser fácilmente movidos o copiados, lo que significa que pueden ser utilizados en diferentes equipos o compartidos con otros usuarios

- También pueden ser fácilmente respaldados y restaurados en caso de que se produzca un problema, lo que puede ayudar a prevenir la pérdida de datos o el tiempo de inactividad

- Ofrecen una forma conveniente y segura de utilizar diferentes aplicaciones y tecnologías en un mismo equipo


## 2.3. Creando un `venv` "*Entorno Virtual*"
Coamandos a implementar para saber el curso del entorno virtual
1. Verificar donde esta `python` y `pip`
```sh
which python3
```
```sh
which pip3
```

2. Si estas en linux o wsl debes instalar el paquete para poder instalar los **venv**
```sh
sudo apt install -y python3-venv
```

3. Poner cada proyecto en su propio ambiente, pero antes se debe entrar en cada carpeta donde se desea crear el ambiente.
```sh
cd <NameFile> 
python3 -m venv <name_env>
```

4. Activar el ambiente
```sh
source <name_env>/bin/activate
```

5. Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
```sh
pip3 install matplotlib==3.5.0
```
> [!IMPORTANT]
>
> Luego de haber realizado la instalación de las diferentes librerias y modulos en sus versiones correspondientes dentro del entorno, **se requerira seleccionar un interprete de python compatible con las versiones**, _en el caso que se desarrolle dentro del entorno de VSCode este lo solicitara automaticamente para solucionar los errores_.

6. Verificar las instalaciones
```sh
pip3 freeze
```

7. Salir del ambiente virtual
```sh
deactivate
```

## 2.4. Requirements.txt 
>[!IMPORTANT]
> 
> **Archivo que gestiona todas las dependencias y en que versiones se necesitan.**

1. Generar el archivo con el siguiente comando
```sh
pip3 freeze > requirements.txt
```
> [!NOTE]
>
> Antes de ejecutar este comando es importante tener en cuenta que **las librerias deseadas ya deben estar instaladas y verificadas con el comando `pip3 freeze` el entorno.**

2.  Revisar lo que hay dentro del archivo
```sh
cat requirements.txt
```

3. Instalar las dependencias necesarias para contribuir más rápido en proyectos

```sh
pip3 install -r requirements.txt
```

## 2.5. Add Project
**Con base en lo anterior, añadir el proyecto en un nuevo ambiente clonando el repositorio**
```sh
# Clona el repositorio de GitHub a tu máquina local
git clone

# Cambia al directorio del proyecto
cd app

# Crea un entorno virtual de Python
python3 -m venv env

# Activa el entorno virtual
source env/bin/activate

# Instala las dependencias del proyecto
pip3 install -r requirements.txt

# Ejecuta el programa principal
python3 main.py
```

## 2.6. Solicitudes HTTP con Requests

La librería `requests` en Python **es una biblioteca para hacer solicitudes HTTP.** Es una de las bibliotecas más populares en Python para hacer solicitudes HTTP debido a su simplicidad y facilidad de uso.

- **Con requests, puedes enviar solicitudes HTTP de todos los tipos, como `GET`, `POST`, `PUT`, `DELETE` y más.** 

- También puedes manejar detalles como parámetros de consulta, encabezados HTTP, formularios, archivos multipartes y sesiones.

### Instalación de la libreria `requests` en un `venv` de Python

Luego de haber creado un `venv` tomando de base las indicaciones antes  mencionadas, basta con digitar el siguiente comando:

```sh
pip3 install requests
```

> [!TIP]
> 
> Al instalarse se sigue el mismo procedimiento para almacenar las librerias en el `requeriments.txt` del directorio y poder hacer solicitudes HTTP

### Solicitudes POST a una API fake con `requests`

- En el siguiente ejemplo se realiza una solicitud GET a una API de productos **[Platzi Fake Store API](https://fakeapi.platzi.com)** para traer los sets de datos en formato de diccionario para luego pasarlo a formato JSON

```python
import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Se establece la conexión con la API usando el metodo GET
    print(r.status_code) # Se imprime el estado de la conexión
    print(r.text) # Se imprime el contenido de la conexión
    print(type(r.text)) # Se imprime el tipo de dato de la conexión
    categories = r.json() # Se convierte el contenido de la conexión a un objeto JSON
    for category in categories:
        print(category['name']) # Se imprime el nombre de cada categoría
```
> [!TIP]
>
> **Es buena practica declarar la URL de la URl de la que se hace la solicitud en una variable o incluso se pueden guardar en un unico archivo e importarlo cuando se requiera establecer una solicitud**

```python
import requests

api_url_categories = 'https://api.escuelajs.co/api/v1/categories'

def get_categories():
      r = requests.get(api_url_categories) # Se establece la requests.get(api_url_categories)
      print(f'Status code: {r.status_code}')
      print(f'Text: {r.text}')
      print(f'type: {type(r.text)}')
```


## 2.7. Uso de la libreria `pandas` en Python

La librería `pandas` en Python es una biblioteca de código abierto que proporciona estructuras de datos de alto rendimiento y fáciles de usar, así como herramientas de análisis de datos.

- Es fundamental para la manipulación y el análisis de datos en Python, y es una de las bibliotecas más utilizadas en ciencia de datos y análisis de datos.

### Aplicaciones y usos de la libreria `pandas` en Python

- **Manipulación de datos**: puedes cambiar la forma de los datos, pivotarlos, dividirlos, etc.

- **Limpieza de datos**: puedes tratar con datos faltantes, filtrar datos, etc.

- **Análisis de datos**: puedes agrupar datos, calcular estadísticas descriptivas, etc.

### Instalación de la libreria `pandas` en un `venv` de Python

Para llevar a cabo la instalación de la librería `pandas` en un `venv` de Python, se debe ejecutar el siguiente comando:

```sh
pip3 install pandas
```
> [!TIP]
> 
> Al instalarse se sigue el mismo procedimiento para almacenar las librerias en el `requeriments.txt` 

### Ejemplos de uso de la libreria `pandas` en Python

1. Crear un DataFrame (la estructura de datos principal de pandas) a partir de un diccionario de Python

```python
import pandas as pd
data = {
    'name': ['John', 'Anna', 'Peter', 'Linda'],
    'age': [25, 36, 29, 42],
    'city': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)
print(df)
```

2. Calcular estadísticas descriptivas

```python
import pandas as pd

df = pd.read_csv('data.csv')
filtered_df = df[df['age'] > 30]
print(filtered_df.describe())
```

> [!NOTE]
>
> **La biblioteca es muy poderosa y flexible, y puede manejar una amplia variedad de tareas de manipulación y análisis de datos**.
>


## 2.8. Uso de la libreria `FastAPI` en Python

La librería `FastAPI` es un Framework web moderno y rápido para la creación de API web con Python 3.6+. Utiliza la mejor OpenAPI y JSON Schema para la validación de datos y la documentación automática.

- **Es fácil de usar y aprender**, y proporciona una gran cantidad de características y funcionalidades útiles para la creación de API web.

### Aplicaiones y usos de la libreria `FastAPI` en Python

- **Creación de API web**: Permite crear API web rápidas y modernas con Python.

- **Documentación automática**: FastAPI genera automáticamente documentación interactiva para una API web.

- **Validación de datos**: FastAPI valida automáticamente los datos de entrada y salida de una API web.

- **Seguridad**: FastAPI proporciona características de seguridad integradas para proteger una API web.

- **Escalabilidad**: FastAPI es altamente escalable y puede manejar una gran cantidad de tráfico.

- **Compatibilidad con otros marcos**: FastAPI es compatible con otros marcos y bibliotecas de Python entre las cuales están `Starlette`, `Pydantic`, `SQLAlchemy`, `OAuth2`, `JWT`, entre otros.

### Instalación de la libreria `FastAPI` en un `venv` de Python

Para llevar a cabo la instalación de la librería `FastAPI` en un `venv` de Python, se debe ejecutar el siguiente comando:

```sh
pip3 install fastapi
```
- Ademas de instalar `FastAPI`, también se debe instalar `uvicorn`, un servidor ASGI de alto rendimiento para Python, con el siguiente comando:

```sh
pip3 install "uvicorn[standard]"
```

> [!TIP]
>
> Al instalarse se sigue el mismo procedimiento para almacenar las librerias en el `requeriments.txt`

### Ejemplos de uso de la libreria `FastAPI` en Python

1. Crear una API web simple con FastAPI

```python
from fastapi import FastAPI

def create_app():
    app = FastAPI()

    @app.get('/')
    def read_root():
        return {'message': 'Hello, World!'}

    return app
if __name__ == '__main__':
    app = create_app()
```

> [!IMPORTANT]
>
> Al tratarse de una API web, se debe ejecutar el servidor de desarrollo de FastAPI con el siguiente comando:

```sh
uvicorn main:app --reload
```
> **de esta manera se podra visualizar la API en el navegador web**. Ademas **el parametro `--reload` permite que el servidor se reinicie automáticamente cuando se realicen cambios en el código**.

2. Crear una API web que muestre una estructura HTML

```python
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

def create_app():
    app = FastAPI()

    @app.get('/response', response_class=HTMLResponse)
    def get_response():
        return """
        '<h1>Hello, World!</h1>'
    """
    return app
if __name__ == '__main__':
    app = create_app()
```

> [!NOTE]
> Esta biblioteca es bastante practica para la creación de API web, ya que permite **crear API web rápidas y modernas con Python, además de proporcionar una gran cantidad de características y funcionalidades útiles para la creación de API web.**