from os import system

system('clear')
""" Primera clase padre """
class FiguraGeometrica:
    
    def __init__(self, ancho, alto):
        self.__ancho = ancho
        self.__alto = alto

    @property
    def ancho (self):
        return self.__ancho
    
    @ancho.setter
    def FiguraGeo (self, value):
        self.__ancho = value

    @property
    def alto(self):
        return self.__alto
    
    @alto.setter
    def alto(self, value):
        self.__alto = value
