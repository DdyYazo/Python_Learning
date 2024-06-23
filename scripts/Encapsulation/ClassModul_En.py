from os import system

system('clear')


from scripts.Encapsulation.ClassEncapsul import Persona as ce


print('Creación de objeto de prueba '.center(50,'-'),'\n')
persona1 = ce("Juan", "Perez", 30)
persona1.mostrarDetalle()
print()

print('Eliminación de objetos '.center(50,'-'),'\n')
del persona1