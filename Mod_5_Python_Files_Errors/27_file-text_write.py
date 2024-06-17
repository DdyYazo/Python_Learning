from os import system

system("clear")

""" Para escribir en un archivo de texto, se debe abrir el archivo en modo escritura, si el archivo no existe, se creará, si existe, se sobreescribirá """

""" En este primer caso se utilizaria el permiso "r+" para que no se sobreescriba el archivo y le de permisos de lectura y escritura"""
with open("./Mod_5_Python_Files_Errors/text.txt","r+",) as file: # En este caso se le asignan al archivo permisos de lectura y escritura para que no se sobreescriba el archivo
    for line in file:
        print(line)
    file.write("Hola, este es un archivo de texto\n")  # se utiliza el método write() para escribir en el archivo



""" En el segundo caso se utilizaria el permiso "w+" para que se sobreescriba el archivo y le de permisos de lectura y escritura"""
with open("./Mod_5_Python_Files_Errors/text.txt","w+",) as file: # En este caso se le asignan al archivo permisos de lectura y escritura para que se sobreescriba el archivo
    for line in file:
        print(line)
    file.write("Hola, este es un archivo de texto\n")
    file.write("Hola, esta es una segunda prueba\n")
    file.write("Hola, este es una tercera prueba \n")