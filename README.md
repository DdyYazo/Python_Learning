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

## ¿Que es pip?

PIP es el gestor de paquetes de python, es posible buscar librerías en la pagina [pypi.org](https://pypi.org).

- Ver la versión de pip `pip3 -v`. 
- Instalación de paquetes `pip3 install <libreria>`.
- Listar las librerías que se tienen en el entorno de python global `pip3 list`.
- Listar todas las librerías de python instaladas por el usuario `pip3 freeze`.


## ¿Que es un entorno o ambiente virtual?
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

## Creando un `venv` "*Entorno Virtual*"
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

5. Salir del ambiente virtual
```sh
deactivate
```

6. Podemos instalar las librerias necesarias en el ambiente virtual como por ejemplo
```sh
pip3 install matplotlib==3.5.0
```

7. Verificar las instalaciones
```sh
pip3 freeze
```

## Requirements.txt 
>[!IMPORTANT]
> 
> **Archivo que gestiona todas las dependencias y en que versiones se necesitan.**

1. Generar el archivo con el siguiente comando
```sh
pip3 freeze > requirements.txt
```

2. Revisar lo que hay dentro del archivo
```sh
cat requirements.txt
```

3. Instalar las dependencias necesarias para contribuir más rápido en proyectos

```sh
pip3 install -r requirements.txt
```

## Add Project
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
