from os import system

system('clear')
""" Clase padre """
class Persona: # Se utilizaria (object) para que la clase sea nueva y no herede de ninguna otra clase pero no es necesario
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def datos(self):
        return self.__nombre, self.__edad

    @datos.setter
    def datos(self, datos):
        self.__nombre, self.__edad = datos
        
    def __str__(self):
        return f'Persona: [Nombre: {self.__nombre}, Edad: {self.__edad}]'
    
    def mostrar(self):
        print(f'Nombre: {self.__nombre}')
        print(f'Edad: {self.__edad}')

""" Clase hija """
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.__sueldo = sueldo
        
    @property
    def datos(self):
        return super().datos + (self.__sueldo,)
    
    @datos.setter
    def datos(self, datos):
        nombre, edad, sueldo = datos  # Desempaquetado de la tupla
        super(Empleado, self.__class__).datos.fset(self, (nombre, edad))  # Llama al setter de la clase padre para nombre y edad
        self.__sueldo = sueldo  # Establece el sueldo directamente
    
    def __str__(self):
        return f'Empleado: [Salario: {self.__sueldo}, {super().__str__()}'
    
    def mostrar(self):
        super().mostrar()
        print(f'Sueldo: {self.__sueldo}')


if __name__ == '__main__':	
    Empleado1 = Empleado('juan', 32, 2000)
    Empleado1.mostrar()
    Empleado1.datos = ('Pedro', 25, 1500)
    Empleado1.mostrar()