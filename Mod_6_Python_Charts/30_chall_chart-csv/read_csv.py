import csv

def read_csv(path):
    """
    Lee un archivo CSV y devuelve su contenido como una lista de diccionarios.

    Args:
        path (str): La ruta al archivo CSV.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa una fila en el archivo CSV.
              Las claves de los diccionarios son los nombres de las columnas del archivo CSV, y los valores
              son los valores correspondientes en cada fila.
    """
    # Código para leer el archivo CSV y devolver su contenido
def read_csv(path):
    """
    Reads a CSV file and returns its contents as a list of dictionaries.

    Args:
        path (str): The path to the CSV file.

    Returns:
        list: A list of dictionaries, where each dictionary represents a row in the CSV file.
              The keys of the dictionaries are the column names from the CSV file, and the values
              are the corresponding values in each row.

    """
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
        return data

if __name__ == '__main__':
  data = read_csv('./30_chall_chart-csv/data.csv')
  print(data[0])