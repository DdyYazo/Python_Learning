class Persona:
    Contador_personas = 0
    
    @classmethod
    def _incremento_de_personas(cls):
        cls.Contador_personas += 1
        return cls.Contador_personas
    
    def __init__(self, nombre, edad):
        self.id_persona = Persona._incremento_de_personas()
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return f'Persona [{self.id_persona} {self.nombre} {self.edad}]'

persona1 = Persona('Juan', 28)
persona2 = Persona('Maria', 30)
persona3 = Persona('Jose', 18)
print(persona1)
print(persona2)
print(persona3)