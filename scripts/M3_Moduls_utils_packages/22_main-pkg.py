from os import system

system("clear")

""" from mi_paquete.mod_1 import func_1, func_2
from mi_paquete.mod_2 import func_3, func_4 """

""" print(func_1())
print(func_2())
print(func_3())
print(func_4()) """

import mi_paquete_22
print(mi_paquete_22.URL)
print(mi_paquete_22.mod_1.func_1()) # En este ejemplo de namespace package, se puede acceder a los modulos de la siguiente manera mi_paquete.mod_1.func_1() o mi_paquete.mod_2.func_3() sin necesidad de importarlos directamente. pero cabe aclarar que no se pueden invocar directamente sin antes haberlos importado en mi_paquete/__init__.py
