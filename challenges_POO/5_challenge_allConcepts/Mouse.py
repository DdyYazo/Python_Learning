from os import system

system('clear')
from InputDevice import InputDevice

class Mouse(InputDevice):
    
    mouseCounter = 0
    
    @classmethod
    def _mouseCounter(cls):
        cls.mouseCounter += 1
        return cls.mouseCounter
    
    def __init__(self, inputType, brand):
        super().__init__(inputType, brand)
        self.__idMouse = Mouse._mouseCounter() 

    def __str__(self) :
        return f'Id: {self.__idMouse}, {InputDevice.__str__(self)}'


if __name__ == '__main__':
    mouse1 = Mouse('USB','MarcaX')
    print(mouse1)