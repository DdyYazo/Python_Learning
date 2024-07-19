from os import system

system('clear')
class Monitor():
    
    monitorCounter = 0
    
    @classmethod
    def _monitorCounter(cls):
        cls.monitorCounter += 1
        return cls.monitorCounter
    
    def __init__(self, marca, tamaño):
        self.__idMonitor = Monitor._monitorCounter()
        self._marca = marca
        self._tamaño = tamaño
    
    @property
    def marca (self):
        return self._marca
    
    @marca.setter
    def marca (self, marca):
        self._marca = marca
        
    @property
    def tamaño (self):
        return self._tamaño
    
    @tamaño.setter
    def tamaño (self, entrada):
        self._tamaño = entrada
    

    def __str__(self) :
        return f'Id: {self.__idMonitor}, Marca: {self._marca}, Tamaño: {self._tamaño}'


if __name__ == '__main__':
    monitor1 = Monitor('MarcaX', '12 pulgadas')
    print(monitor1)