from os import system

system('clear')

from abc import ABC, abstractmethod

""" Primera clase padre """
class FiguraGeometrica(ABC): # Transformar en clase Abstracta
    
    def __init__(self, ancho, alto):
        if self._valueValidator(ancho):
            self._ancho = ancho
        else: 
            self._ancho = 0
            print(f'Valor invalido: {ancho}')
        if self._valueValidator(alto):
            self._alto = alto
        else: 
            self._alto = 0
            print(f'Valor invalido: {ancho}')

    @property
    def ancho (self):
        return self._ancho
    
    @ancho.setter
    def ancho (self, ancho):
        if (self._valueValidator(ancho)):
            self._ancho = ancho
        else:
            print(f'El valor erroneo del ancho: {ancho}')

    @property
    def alto(self):
        return self._alto
    
    @alto.setter
    def alto(self, alto):
        if (self._valueValidator(alto)):
            self._alto = alto
        else:
            print(f'El valor erroneo del alto: {alto}')
    
    
    @abstractmethod
    def calcular_area(self):
        pass
    
    def __str__(self):
        return f'Figura geometrica: [Ancho: {self._ancho}, Alto: {self._alto}]'

    def _valueValidator (self, value): # Metodo privado o encapsulado para validar valores
        return True if 0 < value < 10 else False
