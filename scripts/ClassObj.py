from os import system

system('clear')
class Persona:
    """ 
    Pasar una tupla de valores de tipo variable y un diccionario de valores de tipo variable a la clase Persona y mostrar los valores en pantalla
    
    """
    
    def __init__(self, nombre, apellido, edad, *args, **kwargs): # Se utiliza *args para pasar una tupla de valores de tipo variable y **kwargs para pasar un diccionario de valores de tipo variable 
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad
        self.args = args
        self.kwargs = kwargs
        
    def mostrarDetalle(self):
        print(f'Persona: Hola {self.nombre} {self.apellido}, tu edad es: {self.edad} y tambien tienes los siguientes valores de una tupla: {self.args} y un diccionario: {self.kwargs}')

persona1 = Persona("Juan", "Perez", 30, 1, 2, 3, 4, 5, ciudad = "Bogota", pais = "Colombia")
persona1.mostrarDetalle()

