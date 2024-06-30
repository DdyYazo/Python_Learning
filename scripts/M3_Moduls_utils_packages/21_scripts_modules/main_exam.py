""" 1. Para este ejemplo se desea importar la variable data del módulo script.py  """
from moduleScript_2 import data

""" print(f"La Data List de data=> {data}")  
# Para este caso el modulo moduleScript_2.py no solo importa la variable data sino que también importa las funciones population_by_country() y get_population() del módulo utils.py, lo que en realidad solo se busca importar la variable data del módulo moduleScript_2.py
 """
 
""" 2. Solucionar este problema embebiendo el comportamiento del modulo moduleScript_2.py en una función que se pueda importar en otro modulo."""
from moduleScript_2 import run # Se importa la función run() del módulo moduleScript_2.py
run() # En este caso luego de haber embebido todo el comportamiento del modulo moduleScript_2.py en una función, se puede ejecutar la función run() para obtener las funciones de los modulos importados



### IMPORTANDO EL EJEMPLO BASE PARA EL USO DE SCRIPTS EN PYTHON

import moduleScript_2
moduleScript_2.hello() # En este caso cuando se ejecute el archivo moduleScript_2.py el output será: module.py se ha importado como un módulo

