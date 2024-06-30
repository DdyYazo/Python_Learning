# PRIMERA PAGINA PARA RESUMEN DE COMO USAR MODULOS

""" 1. Para este ejemplo se define una función que puede ser reutilizada en otros programas. 
La función get_population() retorna dos listas, una con las llaves y otra con los valores que se van a emplear en el diccionario de comprensión. """
def get_population():

    keys = ["col", "arg"]
    values = ["col", "arg"]
    return keys, values

""" 2. Al igual que las funciones las variables definidas en un módulo pueden ser reutilizadas en otros programas."""
A = 'Hola'

"""  
> [!TIP] 
> 
> Una buena practica para nombrar archivos que se consideran modulos es nombrandolos como utils.py, helpers.py, etc. lo que permitira que otros programadores sepan que son modulos que contienen funciones que pueden ser reutilizadas en otros programas.

> [!IMPORTANT] 
> 
> Ademas normalmente los archivos que  tienen utilidades solo manejan funciones para que no se mezclen con las variables y clases de otros archivos.
 """
""" 1.2 Otro ejemplo de una función de una población basado en un pais llamada population_by_country() que utiliza una lambda function para filtrar los paises de la lista de diccionarios data y retorna el pais y su población """	
def population_by_country(data, country):
    result = list(filter(lambda item: item['Country'] == country, data))
    return result