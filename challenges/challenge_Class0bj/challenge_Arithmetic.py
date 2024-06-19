from os import system

system('clear')

class Aritmetica:
    """ 
    Clase Aritmetica para realizar las operaciones de sumar, restar, multiplicar, dividir, potencia, raiz, modulo y division entera
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        result = self.operandoA + self.operandoB
        print(f'La suma de {self.operandoA} y {self.operandoB} es {result}')
    
    def restar(self):
        result = self.operandoA - self.operandoB
        print(f'La resta de {self.operandoA} y {self.operandoB} es {result}')
        
    def multiplicar(self):
        result = self.operandoA * self.operandoB
        print(f'La multiplicacion de {self.operandoA} y {self.operandoB} es {result}')
        
    def dividir(self):
        try :
            result = self.operandoA / self.operandoB
            print(f'La division de {self.operandoA} y {self.operandoB} es {result:.2f}')
            if result == 0:
                raise ZeroDivisionError
        except ZeroDivisionError:
            print(f'La división entre {self.operandoA} y {self.operandoB} es invalida por que no se puede dividir por cero')
        
    def potencia(self):
        result = self.operandoA ** self.operandoB
        print(f'La potencia de {self.operandoA} elevado a {self.operandoB} es {result}')

    def raiz(self):
        result = self.operandoA ** (1/self.operandoB)
        print(f'La raiz de {self.operandoA} es {result}')
    
    def modulo(self):
        result = self.operandoA % self.operandoB
        print(f'El modulo de {self.operandoA} y {self.operandoB} es {result}')
    
    def division_entera(self):
        result = self.operandoA // self.operandoB
        print(f'La division entera de {self.operandoA} y {self.operandoB} es {result}')
    
val1 = Aritmetica(20, 3)
val1.sumar()
val1.restar()
val1.multiplicar()
val1.dividir()
val1.potencia()
val1.raiz()
val1.modulo()
val1.division_entera()
    