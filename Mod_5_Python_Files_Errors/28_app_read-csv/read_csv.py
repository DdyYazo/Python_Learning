from os import system

system("clear")

""" Para manipular archivos csv en Python se puede utilizar la librería csv que ya viene incluida en Python """
import csv
""" def run(path): # Se define la función run() que recibe como parámetro la variable path, path es la ruta del archivo data.csv, path significa ruta
    with open(path, "r") as csvfile: # Se abre el archivo data.csv en modo lectura
        reader = csv.reader(csvfile, delimiter=',') # Se utiliza el método reader() para leer el archivo
        header = next(reader)
        for row in reader: # Se itera sobre cada fila del archivo
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            print(country_dict)

if __name__ == "__main__":
    run('./app_read-csv/data.csv') # Se llama la función run() para que se pueda ejecutar en otros archivos
 """


""" Al ejecutarse el codigo anterior la información del csv no se verá de manera amigable para el usuario, para elo se puede mostrar en forma de diccionario usando diccionary comprehension """
def run(path): # Se define la función run() que recibe como parámetro la variable path, path es la ruta del archivo data.csv, path significa ruta
    with open(path, "r") as csvfile: # Se abre el archivo data.csv en modo lectura
        reader = csv.reader(csvfile, delimiter=',') # Se utiliza el método DictReader() para leer el archivo
        header = next(reader) # Se utiliza el método next() para obtener la cabecera del archivo
        data = []
        for row in reader: # Se itera sobre cada fila del archivo
            iterable = zip(header, row) # Se utiliza el método zip() para unir la cabecera con cada fila del archivo
            country_dict = {key: value for key, value in iterable} # Se crea un diccionario con comprensión de diccionario
            data.append(country_dict) # Se agrega el diccionario a la lista data
        return data
            
if __name__ == "__main__":
    data = run('./28_app_read-csv/data.csv') # Se llama la función run() para que se pueda ejecutar en otros archivos
    print(data[1]) # Se imprime la variable data para que se pueda ver la información del archivo csv en forma de diccionario