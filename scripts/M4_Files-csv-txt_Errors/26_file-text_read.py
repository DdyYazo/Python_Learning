from os import system

system("clear")

""" En python es posible leer un archivo de texto, para ello se utiliza la función open() y el método read() """


file = open("./Mod_5_Python_Files_Errors/text.txt","r",)  # se crea una variable llamada file, y open abre el archivo con la ruta especificada, el segundo argumento es el modo de apertura, en este caso 'r' para lectura
print(file.read()) # se utiliza el método read() para leer el contenido del archivo 

print(file.readline())  # se utiliza el método readline() linea por linea de mi archivo de texto
file.close()  # se cierra el archivo con el método close() 

""" Pero para el caso de archivos muy grandes, se puede utilizar un ciclo for para recorrer el archivo linea por linea """
for line in open("./Mod_5_Python_Files_Errors/text.txt", "r"):
    print(line) 
    
""" A pesar de que el for recorre el archivo linea por linea, es necesario cerrar el archivo con el método close() entonces para no tener que estar cerrando el archivo manualmente, se puede utilizar el método with, que se encarga de cerrar el archivo automáticamente """
with open("./Mod_5_Python_Files_Errors/text.txt") as file:
    for line in file:
        print(line)