from Cuadrado import Cuadrado
from Rectangulo import Rectangulo


print('Creación de objeto Cuadrado'.center(50,'-'))
Cuadrado1 = Cuadrado(5, 'azul')
Cuadrado1.ancho = 9
Cuadrado1.alto = -1
print(f'El área del Cuadrado es: {Cuadrado1.calcular_area()}\n')
print(Cuadrado1)
print('\n')
# print(f'{Cuadrado.mro()} \n')


print('Creación de objeto Rectangulo'.center(50,'-'))
Rectangulo1 = Rectangulo(9, 8, 'lila')
print(f'El área del Rectangulo es: {Rectangulo1.calcular_area()}\n')
print(Rectangulo1)
print('\n')
# print(f'{Rectangulo.mro()} \n')