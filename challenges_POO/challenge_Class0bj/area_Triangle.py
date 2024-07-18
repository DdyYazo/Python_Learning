from os import system

system('clear')
class Area ():
    """
    Calcular el area de un triangulo teniendo en cuenta la base y la altura siguiendo la operación matematica area = 0.5 * base * altura en resultado decimal
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return 0.5 * self.base * self.altura
    
base = int(input("Digite la base del triangulo: "))
altura = int(input("Digite la altura del triangulo: "))
resultado = Area(base, altura)
print(f'El area del triangulo con base {base} y altura {altura} es {resultado.calcularArea()}')