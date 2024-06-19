from os import system

system('clear')
class Cubo:
    """ 
    Calcular el volumen de un cubo teniendo en cuenta el ancho, largo y profundo siguiendo la operación matematica volumen = ancho * largo * profundo 

    """
    
    def __init__(self, ancho, alto, profundo):
        self.ancho = ancho
        self.alto = alto
        self.profundo = profundo
        
    def calcularVolumen(self):
        return self.ancho * self.alto * self.profundo

ancho = int(input("Digite el ancho del cubo: "))
alto = int(input("Digite el largo del cubo: "))
profundo = int(input("Digite el profundo del cubo: "))
resultado = Cubo(ancho, alto, profundo)
print(f'El volumen del cubo con ancho {ancho}, largo {alto} y profundo {profundo} es {resultado.calcularVolumen()}m3')