""" El archivo __init__.py es necesario para que Python trate el directorio como un paquete. (Aplica mayormente para versiones anteriores a la 3.3 de Python)"""

print("Se inicio el paquete 22_packages")
URL = "https://www.google.com" 

# Cada vez que se importe el paquete, se ejecutará el código que se encuentre en el archivo __init__.py

# Se pueden importar los modulos directamente en este archivo, para que se puedan acceder a ellos desde el paquete
from mi_paquete_22.mod_1 import func_1, func_2

# o simplemente se puede importar con el .
from .mod_2 import func_3, func_4
