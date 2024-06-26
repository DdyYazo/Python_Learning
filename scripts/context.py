from os import system

system('clear')


class MiClase ():
    variable_clase = 'Variable de clase'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

    @staticmethod
    def metodo_estatico():
        print(MiClase.variable_clase)

    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)

MiClase.metodo_clase()
MiObjeto1 = MiClase('Valor de la Variable de instancia')
MiObjeto1.metodo_clase()
MiObjeto1.metodo_instancia()



