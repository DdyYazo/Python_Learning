from os import system

system('clear')


class Order:
    
    orderCounter = 0
    
    @classmethod
    def _ordenCounter(cls):
        cls.orderCounter += 1
        return cls.orderCounter
    
    def __init__(self, computers):
        self.__idOrder = Order._ordenCounter()
        self._computers = computers
        

    def addcomputers (self, computer):
        self._computers.append(computer)
        

    def __str__(self):
        computers_str = ""
        for computer in self._computers:
            computers_str += computer.__str__().replace('\n', '\n      ') + "\n"

        return f'''
            Orden: {self.__idOrder} \n
            Computadoras: 
            {computers_str}
        '''