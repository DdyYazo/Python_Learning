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
