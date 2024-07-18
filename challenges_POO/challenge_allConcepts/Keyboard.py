from os import system

system('clear')
from InputDevice import InputDevice

class Keyboard(InputDevice):
    
    keyboardCounter = 0
    
    @classmethod
    def _keyboardCounter(cls):
        cls.keyboardCounter += 1
        return cls.keyboardCounter
    
    def __init__(self, inputType, brand):
        super().__init__(inputType, brand)
        self.__idKeyboard = Keyboard._keyboardCounter()
    
    def __str__(self) :
        return f'Id: {self.__idKeyboard}, {InputDevice.__str__(self)}'

if __name__ == '__main__':
    Keyboard1 = Keyboard('USB','Redragon')
    print(Keyboard1)
    Keyboard2 = Keyboard('Blutooth','MarcaPro')
    print(Keyboard2)