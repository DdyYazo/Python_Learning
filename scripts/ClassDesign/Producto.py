from os import system

system('clear')

class Producto:
    
    Contador_productos = 0
    
    @classmethod
    def _incrementar_contador(cls):
        cls.Contador_productos += 1
        return cls.Contador_productos
    
    def __init__(self, nombre, precio):
       self._id_producto = Producto._incrementar_contador()
       self._nombre = nombre
       self._precio = precio

    @property
    def id_producto(self):
        return self._id_producto
    
    @id_producto.setter
    def id_producto(self, id_orden):
        self._id_producto = id_orden
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio
    
    def __str__(self):
        return f'[Id Producto: {self._id_producto}, Nombre: {self._nombre}, Precio: {self._precio}]'

