<div align="center">

# Python: Pip y entornos virtuales

<p align="center">
  <img src="https://i.postimg.cc/Pf9qsRBx/imagen-2024-06-15-124325203.png" width="450">
</p>

<p><strong>Esta es una recopilación de las utilidades y comandos implementados para pip y entornos virtuales de python</strong></p>

</div>

# Tabla de contenido

- [Python: Pip y entornos virtuales](#python-pip-y-entornos-virtuales)
- [Tabla de contenido](#tabla-de-contenido)
- [1. Comandos Iniciales para la instalación de paquetes y entornos para Python](#1-comandos-iniciales-para-la-instalación-de-paquetes-y-entornos-para-python)
  - [Instalación en Windows con WSL](#instalación-en-windows-con-wsl)
  - [Flujo de trabajo en python](#flujo-de-trabajo-en-python)
    - [main.py: Game Project](#mainpy-game-project)
- [2. PIP y Entornos Virtuales](#2-pip-y-entornos-virtuales)
  - [2.1. `¿Que es pip?`](#21-que-es-pip)
  - [2.2. `¿Que es un entorno o ambiente virtual?`](#22-que-es-un-entorno-o-ambiente-virtual)
    - [Ejemplo de un `venv` "Virtual Environment"](#ejemplo-de-un-venv-virtual-environment)
    - [Caracteristicas de los `venv`](#caracteristicas-de-los-venv)
  - [2.3. `Creando un venv "*Entorno Virtual*"`](#23-creando-un-venv-entorno-virtual)
  - [2.4. `Requirements.txt `](#24-requirementstxt-)
  - [2.5. `Add Project`](#25-add-project)
  - [2.6. `Solicitudes HTTP con Requests`](#26-solicitudes-http-con-requests)
    - [Instalación de la libreria `requests` en un `venv` de Python](#instalación-de-la-libreria-requests-en-un-venv-de-python)
    - [Solicitudes POST a una API fake con `requests`](#solicitudes-post-a-una-api-fake-con-requests)
  - [2.7. `Uso de la libreria "pandas" en Python`](#27-uso-de-la-libreria-pandas-en-python)
    - [Aplicaciones y usos de la libreria `pandas` en Python](#aplicaciones-y-usos-de-la-libreria-pandas-en-python)
    - [Instalación de la libreria `pandas` en un `venv` de Python](#instalación-de-la-libreria-pandas-en-un-venv-de-python)
    - [Ejemplos de uso de la libreria `pandas` en Python](#ejemplos-de-uso-de-la-libreria-pandas-en-python)
  - [2.8. `Uso de la libreria "FastAPI" en Python`](#28-uso-de-la-libreria-fastapi-en-python)
    - [Aplicaiones y usos de la libreria `FastAPI` en Python](#aplicaiones-y-usos-de-la-libreria-fastapi-en-python)
    - [Instalación de la libreria `FastAPI` en un `venv` de Python](#instalación-de-la-libreria-fastapi-en-un-venv-de-python)
    - [Ejemplos de uso de la libreria `FastAPI` en Python](#ejemplos-de-uso-de-la-libreria-fastapi-en-python)
- [3. Python en contenedores de Docker](#3-python-en-contenedores-de-docker)
  - [3.1. `¿Qué es Docker?`](#31-qué-es-docker)
    - [De que manera se aislan los diferentes scrips de python en contenedores Docker](#de-que-manera-se-aislan-los-diferentes-scrips-de-python-en-contenedores-docker)
  - [3.2. `Instalación de Docker en Windows Subsystem for Linux (WSL)`](#32-instalación-de-docker-en-windows-subsystem-for-linux-wsl)
  - [3.3 `Dockerización de scripts de Python`](#33-dockerización-de-scripts-de-python)
      - [1. Crear un archivo `Dockerfile` en el directorio del proyecto](#1-crear-un-archivo-dockerfile-en-el-directorio-del-proyecto)
      - [2. Crear el archivo `docker-compose.yml` en el directorio del proyecto](#2-crear-el-archivo-docker-composeyml-en-el-directorio-del-proyecto)
      - [3. Poner en marcha el contenedor](#3-poner-en-marcha-el-contenedor)
  - [3.5. `Dockerización de una API web con FastAPI`](#35-dockerización-de-una-api-web-con-fastapi)

--- 

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
--- 

# 2. PIP y Entornos Virtuales

## 2.1. `¿Que es pip?`

PIP es el gestor de paquetes de python, es posible buscar librerías en la pagina [pypi.org](https://pypi.org).

- Ver la versión de pip `pip3 -v`. 
- Instalación de paquetes `pip3 install <libreria>`.
- Listar las librerías que se tienen en el entorno de python global `pip3 list`.
- Listar todas las librerías de python instaladas por el usuario `pip3 freeze`.


## 2.2. `¿Que es un entorno o ambiente virtual?`
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


## 2.3. `Creando un venv "*Entorno Virtual*"`
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

## 2.4. `Requirements.txt `
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

## 2.5. `Add Project`
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

## 2.6. `Solicitudes HTTP con Requests`

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


## 2.7. `Uso de la libreria "pandas" en Python`

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


## 2.8. `Uso de la libreria "FastAPI" en Python`

La librería **[FastAPI](https://fastapi.tiangolo.com/#installation)** es un Framework web moderno y rápido para la creación de API web con Python 3.6+. Utiliza la mejor OpenAPI y JSON Schema para la validación de datos y la documentación automática.

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

2. Crear una API web que muestre una estructura HTML usando el modulo **[HTMLResponse](https://fastapi.tiangolo.com/advanced/custom-response/#html-response)** de FastAPI

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

--- 

# 3. Python en contenedores de Docker

## 3.1. `¿Qué es Docker?`

Docker es una plataforma de código abierto que permite a los desarrolladores empaquetar, enviar y ejecutar aplicaciones en contenedores. Los contenedores son entornos ligeros y portátiles que contienen todo lo necesario para ejecutar una aplicación, incluidas las bibliotecas, las dependencias y el código.

- **Docker es una herramienta muy útil para los desarrolladores**, ya que les permite crear entornos de desarrollo consistentes y reproducibles, y les permite ejecutar aplicaciones en cualquier lugar, desde su máquina local hasta la nube.


### De que manera se aislan los diferentes scrips de python en contenedores Docker

<p align="center">
  <img src="https://i.postimg.cc/RCpb7xm2/imagen-2024-05-30-171619676.png" alt="Aquí va el texto del enlace">
</p>

- **Cada contenedor de Docker es una instancia aislada de una imagen de Docker**. Una imagen de Docker es un paquete que contiene todo lo necesario para ejecutar una aplicación, incluidas las bibliotecas, las dependencias y el código.

- **Cada contenedor de Docker se ejecuta en un entorno aislado y seguro**, lo que significa que no puede acceder a los recursos de otros contenedores o del sistema operativo subyacente.

<p align="center">
  <img src="https://i.postimg.cc/Vk4dZgNr/imagen-2024-05-30-183302276.png" alt="Aquí va el texto del enlace">
</p>

## 3.2. `Instalación de Docker en Windows Subsystem for Linux (WSL)`

Para instalar Docker en Windows Subsystem for Linux (WSL), **se pueden seguir los pasos del siguiente video**.

<p align="center">
    <a href="https://youtu.be/ZO4KWQfUBBc">
        <img src="https://i.postimg.cc/bYbfwvk3/imagen-2024-05-30-181020635.png" alt="Imagen" width="400">
    </a>
</p>

**Ademas es importante tener en cuenta los siguientes recursos:**

1. Instalador desde la página de **[Docker for Windows](https://docs.docker.com/desktop/install/windows-install/)**.

2. Consultar la **[documentación oficial de Docker](https://docs.docker.com/desktop/wsl/)** para algunas configuraciones para WSL.

## 3.3 `Dockerización de scripts de Python`

> [!IMPORTANT]
>
> Antes de comenzar con la dockerización de los scripts de Python, es importante tener en cuenta que **se debe tener instalado y corriendo Docker en la máquina local** y ademas que los archivos que se desean dockerizar cumplan con la version de compatibilidad de Python. 

Para llevar a cabo la dockerización de los scripts de Python, se deben seguir los siguientes pasos:

#### 1. Crear un archivo `Dockerfile` en el directorio del proyecto

Dicho archivo contendrá las instrucciones necesarias para construir la imagen del contenedor. A continuación se muestra un ejemplo de un archivo `Dockerfile` para un script de Python

```Dockerfile

FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt /app/requeriments.txt 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
CMD bash -c "while true; do sleep 1; done"
``` 

***Explicación del codigo de configuración del archivo `Dockerfile`***

- **Primera linea:** Selecciona la imagen base de Python 3.9 en su versión slim.

- **Segunda linea:** Especifica el directorio de trabajo en el contenedor.

- **Tercera linea:** Copia el archivo `requirements.txt` del proyecto al contenedor y asi mismo se especifica la carpeta de destino.

- **Cuarta linea:** Instala las dependencias del proyecto en el contenedor y ademas se omite el cache para evitar problemas de compatibilidad, por otro lado, tambien se actializando las dependencias.

- **Quinta linea:** Copia todos los archivos del proyecto al contenedor.

- **Sexta linea:** Ejecuta un comando bash para mantener el contenedor en ejecución.

> [!TIP]
>
> Una buena practica al momento de copiar los archivos del proyecto que se desean dockerizar es **copiar las dependencias `requirements.txt` al contenedor, especificando al lado izquierdo la carpeta local y al lado derecho la carpeta del contenedor**.
>
> - Tambien es importante **especificar la ejecución del contenedor mediante el comando `CMD` para mantenerlo en ejecución, siendo clave para que el archivo `docecfile` funcione correctamente.**

#### 2. Crear el archivo `docker-compose.yml` en el directorio del proyecto

El archivo `docker-compose.yml` contendrá las instrucciones necesarias para construir y ejecutar el contenedor. A continuación se muestra un ejemplo de un archivo `docker-compose.yml` para un script de Python.

```yml
services: 
 app-csv: 
  build: 
   context: . 
   dockerfile: Dockerfile 
```

***Explicación del codigo de configuración del archivo `docker-compose.yml`***

   - **Primera linea:** Se especifica el servicio que se desea dockerizar.

  - **Segunda linea:** Se especifica el nombre del servicio.

  - **Tercera linea:** Se lleva a cabo la construcción de la imagen o servicio. 

  - **Cuarta linea:** Se especifica el contexto del proyecto desde se esta ejecutando el archivo `Dockerfile`. En este caso el directorio actual.

  - **Quinta linea:** Se especifica el archivo `Dockerfile` que se desea utilizar, es importante indicar la linea de codigo `CMD` para mantener el contenedor en ejecución.

#### 3. Poner en marcha el contenedor

Para poner en marcha el contenedor, se deben seguir los siguientes pasos:

1. **Construir la imagen del contenedor** con el siguiente comando:

```sh
docker-compose build
```

2. **Iniciar o levantar el contenedor** con el siguiente comando:

```sh
docker-compose up -d
# la bandera -d permite que el contenedor se ejecute en segundo plano
```

3. **Verificar que el contenedor se encuentra en ejecución** con el siguiente comando:

```sh
docker-compose ps
```
> [!NOTE]
>
> Es importante verificar que el `STATUS` **indique que el contenedor se encuentra en ejecución.**

4. Luego de haber ejecutado los comandos anteriores, **se puede acceder o ejecutar el contenedor** con el siguiente comando:

```sh
docker-compose exec app-csv bash
```

 - Para salir del contenedor se debe ejecutar el comando `exit`.

> [!IMPORTANT]
>
> Si por algun motivo se identifico una incongruencia en el contenedor, se debe volver a construir la imagen del contenedor con el comando `docker-compose build` y luego detener el contenedor que esta en ejecución con el comando `docker-compose down`. Para luego posteriormente volver a levantar el contenedor con el comando `docker-compose up -d`.

5. Para **detener el contenedor**, se debe ejecutar el siguiente comando:

```sh
docker-compose down
```

> [!TIP]
> 
> ## 3.4. `Automatización de vinculos a los archivos con Docker`
> 
> Cada vez que se realiza un cambio en alguno de los archivos del proyecto y se desea actualizar el contenedor, se debe volver a construir la imagen del contenedor con el comando `docker-compose build` y luego detener el contenedor que esta en ejecución con el comando `docker-compose down`. Para luego posteriormente volver a levantar el contenedor con el comando `docker-compose up -d`. **ESTO RESULTA SER UNA TAREA TEDIOSA Y REPETITIVA**
> 
> Por lo tanto para hacerlo mas eficiente se puede automatizar el proceso de vinculación de los archivos del proyecto con el contenedor de Docker mediante una configuración en el archivo `docker-compose.yml`, agregando una linea de mapeo de volumen para vincular los archivos del proyecto con el contenedor, de esta manera cada vez que se realice un cambio en los archivos del proyecto, el contenedor se actualizara automáticamente.

```yml
# resto de codigo
   dockerfile: <archivo Docker> 
  volumes: 
   - .:/app #esta linea mapea la carpeta actual con la carpeta /app del contenedor para que cada cambio que se haga en la carpeta actual se refleje en el contenedor
```

## 3.5. `Dockerización de una API web con FastAPI`

Al igual que el caso de los scripts de Python, **se puede dockerizar una API web creada con FastAPI** siguiendo los mismos pasos mencionados anteriormente, con la excepción de que puede cambiar la version de Python y las dependencias del proyecto. En este caso la unica linea que se alteraria en el archivo `Dockerfile` estaria relacionada con el servidor `uvicorn` que se encarga de ejecutar la API web y asi mismo indicando el puerto de ejecución.

```Dockerfile
# -- Resto de codigo
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

- En este caso para el caso del servidor web **se va a usar `uvicorn` que es un servidor web asincrono para python y se establece en el puerto 80.**

Y asi mismo, en el caso del archivo `docker-compose.yml` se debe especificar el puerto de ejecución de la API web y el nombre de la imagen con respecto al proyecto, que en este caso es `web-server`.

```yml
services: 
 web-server: 
# -- Resto de codigo
  ports: 
   - "80:80"
```
