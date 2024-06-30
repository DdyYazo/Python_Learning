from os import system

system('clear')

from Producto import Producto

class Orden:
    
    Contador_ordenes = 0
    
    @classmethod
    def _incrementar_contador(cls):
        cls.Contador_ordenes += 1
        return cls.Contador_ordenes
    
    def __init__(self, productos):
        self._id_orden = Orden._incrementar_contador()
        self._productos = list(productos)
        
    @property
    def productos(self):
        return self._productos
    
    @productos.setter
    def productos(self, productos):
        self._productos = productos
    
    def agregar_producto (self, producto):
        self._productos.append(producto)
    
    def calcular_total(self):
        total = 0 
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ''
        for producto in self._productos:
            productos_str += producto.__str__() + ' | '
        return f'Orden: {self._id_orden} \n Productos: {productos_str} \n Total: {self.calcular_total()}'
