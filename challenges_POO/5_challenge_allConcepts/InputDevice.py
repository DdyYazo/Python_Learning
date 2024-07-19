from os import system

system('clear')
class InputDevice:
    
    def __init__(self, inputType, brand):
        self._inputType = inputType
        self._brand = brand

    @property
    def inputType (self):
        return self._inputType
    
    @inputType.setter
    def inputType (self, entrada):
        self._inputType = entrada
    
    @property
    def brand (self):
        return self._brand
    
    @brand.setter
    def brand (self, brand):
        self._brand = brand
    
    def __str__(self) :
        return f'brand: {self._brand}, Tipo de Entrada: {self._inputType}'