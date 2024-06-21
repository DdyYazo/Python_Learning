from os import system

system('clear')

class Persona:
    def __init__(self, nombre, apellido, edad):
        self.__nombre = nombre 
        self.__apellido = apellido
        self.__edad = edad

    @property
    def user(self):
        print('Llamando método get nombre')
        return self.__nombre, self.__edad, self.__apellido
    
    @user.setter
    def user(self, user_info):
        self.__nombre, self.__edad, self.__apellido = user_info


    def mostrarDetalle(self):
        print(f'Persona: Hola {self.__nombre} {self.__apellido}, tu edad es: {self.__edad}')

    def __del__(self):
        print(f'Objeto {self.__nombre} y {self.__apellido} eliminado')

if __name__ == '__main__':
    persona1 = Persona("Juan", "Perez", 30)
    print(persona1.user)

    persona1.user = ('Jaime', 22, 'Lopez')  
    persona1.mostrarDetalle()
    
    print(__name__)