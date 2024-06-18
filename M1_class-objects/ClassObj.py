class Persona:
    def __init__(self, nombre, apellido, edad): # Se definen los atributos (parametros) de la clase
        self.nombre = nombre # Se inicializa el atributo nombre
        self.apellido = apellido
        self.edad = edad

persona1 = Persona("Juan", "Perez", 30) # Se crea un objeto de la clase Persona pasado los argumentos
print(f'Objeto Persona 1 :{persona1.nombre} {persona1.apellido} {persona1.edad}') # Se acceden a los atributos del objeto  

persona2 = Persona("Karla", "Gomez", 25)
print(f'Objeto Persona 2 :{persona2.nombre} {persona2.apellido} {persona2.edad}')  
