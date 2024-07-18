from os import system

system('clear')

"""
Definir una clase padre llamada Vehiculo y dos clases hijas llamadas Coche y Bicicleta,
las cuales heredan de la clase Padre Vehiculo.
La clase padre debe tener los siguientes atributos y métodos

Vehiculo (Clase Padre):
-Atributos (color, ruedas)
-Métodos ( __init__() y __str__ )

Coche  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( velocidad (km/hr) )
-Métodos ( __init__() y __str__() )

Bicicleta  (Clase Hija de Vehículo) (Además de los atributos y métodos heradados de Vehículo):
-Atributos ( tipo (urbana/montaña/etc )
-Métodos ( __init__() y __str__() )
"""

class Vehiculo:

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return f'Mi vehículo tiene: [Color: {self.color}, Ruedas: {self.ruedas}]'

class Coche(Vehiculo):

    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return f'Mi coche tiene: [Color: {self.color}, Ruedas: {self.ruedas}, Velocidad: {self.velocidad} km/hr]'

class Bicicleta(Vehiculo):

    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return f'Mi bicicleta tiene: [Color: {self.color}, Ruedas: {self.ruedas}, Tipo: {self.tipo}]'

# Creación de objeto de prueba
Vehiculo1 = Vehiculo('Rojo', 4)
print(Vehiculo1)
print()
Vehiculo2 = Coche('Azul', 4, 120)
print(Vehiculo2)
print()
Vehiculo3 = Bicicleta('Verde', 2, 'Montaña')
print(Vehiculo3)
print