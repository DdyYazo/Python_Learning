from ClassCuadrado_HM import Cuadrado

cuadrado1 = Cuadrado(12, 'verde')
print(f'Cálculo área del Cuadrado: {cuadrado1.calcular_area()}')


# MRO - Method Resolution Order
print(Cuadrado.mro())