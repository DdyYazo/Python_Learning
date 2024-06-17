""" En los conjuntos tambien se pueden hacer operaciones de creacion, modificacion y eliminacion de elementos """

# Saber el tamaño de un conjunto
setPrub = {1, 2, 3, 4, 5, 6, 7, 8, 'loco'}
size = len(setPrub) # En este caso se crea una variable para almacenar el tamaño del conjunto
print(size) # Al imprimirlo se puede ver que el tamaño del conjunto es de 9 elementos

# Preguntar por un elemento en un conjunto
print(1 in setPrub) # Al imprimirlo se puede ver que el elemento 1 si esta en el conjunto
print(10 in setPrub) # Al imprimirlo se puede ver que el elemento 10 no esta en el conjunto

# Agregar un elemento a un conjunto
setPrub.add('bebe') # En este caso se agrega el elemento bebe al conjunto
print(setPrub) # Al imprimirlo se puede ver que el elemento bebe se agrego al conjunto
setPrub.add('bebe') # En este caso se agrega el elemento bebe al conjunto
print(setPrub) # Al imprimirlo se puede ver que no se agrego el elemento bebe al conjunto porque ya existe

""" Update: Agregar varios elementos a un conjunto"""
setPrub.update({'hola', 'eche', 1}) # En este caso se agregan los elementos hola, eche y 1 al conjunto
print(setPrub) # Al imprimirlo se puede ver que los elementos hola, eche y 1 se agregaron al conjunto pero el 1 no se agrego porque ya existe


"""1.  Delete: Eliminar elementos de un conjunto mediante remove o discard """

setPrub.remove('eche') # En este caso se elimina el elemento eche del conjunto
print(setPrub) # Al imprimirlo se puede ver que el elemento eche se elimino del conjunto

# Remover un elemento que no existe en un conjunto
""" setPrub.remove('eche') # En este caso se elimina el elemento eche del conjunto
print(setPrub) # Al imprimirlo se puede ver que mandara un error porque el elemento eche no existe en el conjunto
 """
# 2. Para el caso anterior se puede usar discard
setPrub.discard('eche') # En este caso se elimina el elemento eche del conjunto
print(setPrub) # Al imprimirlo se puede ver que no mandara un error porque el elemento eche no existe en el conjunto por ello es mas recomendable usar discard

# 3. Limpiar un conjunto
setPrub.clear() # En este caso se limpia el conjunto
print(len(setPrub)) # Al imprimirlo se puede ver que el conjunto se vacio

