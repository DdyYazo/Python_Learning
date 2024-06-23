from os import system

system('clear')


from ClassFigure_HM import FiguraGeometrica 
from ClassColor_HM import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def calcular_area (self):
        return self.ancho * self.alto
