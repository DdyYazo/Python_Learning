from os import system
import utils
import read_csv
import charts
system("clear")
def run():
    """
    Función principal que ejecuta el programa.
    Lee los datos de un archivo CSV y solicita al usuario el nombre de un país.
    Luego, obtiene la población de ese país y genera un gráfico de barras.
    """
    data = read_csv.read_csv('data.csv')
    country = input('Ingrese el nombre del país => ')
  
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)

if __name__ == '__main__':
  run()