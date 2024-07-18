from os import system


system('clear')
from Monitor import Monitor
from Keyboard import Keyboard
from Mouse import Mouse

class Computer:
    
    computersCounter = 0
    
    @classmethod
    def _computersCounter(cls):
        cls.computersCounter += 1
        return cls.computersCounter
    
    def __init__(self, name, monitor, keyboard, mouse):
        self.__idComputer = Computer._computersCounter()
        self._name = name
        self._monitor = monitor
        self._keyboard = keyboard
        self._mouse = mouse

    """ @property
    def name (self):
        return self._name
    
    @name.setter
    def name (self, entrada):
        self._name = entrada
    
    @property
    def monitor (self):
        return self._monitor
    
    @monitor.setter
    def monitor (self, monitor):
        self._monitor = monitor """

    # def agregar_mouse ():
    def __str__(self) :
        return f'''
        {self._name}: {self.__idComputer} \n
            Monitor: {self._monitor} 
            keyboard: {self._keyboard} 
            mouse: {self._mouse} 
        '''


if __name__ == '__main__':
    monitor1 = Monitor('Asus','24 pulgadas')
    keyboard1 = Keyboard('USB','Redragon')
    mouse1 = Mouse('Blutooth','Logitech')
    Computer1 = Computer('Lenovo', monitor1, keyboard1, mouse1)
    print(Computer1)
    
    monitor2 = Monitor('HP','12 pulgadas')
    keyboard2 = Keyboard('Blutooth','weibo')
    mouse2 = Mouse('USB','iconic')
    Computer2 = Computer('McBook',monitor2, keyboard2, mouse2)
    print(Computer2)