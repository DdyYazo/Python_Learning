from os import system
import utils
import read_csv
import charts
import pandas as pd

system("clear")


def run():
    # Analisis y visualizacion de datos con csv mediante read_csv y matplotlib
    '''
    data = list(filter(lambda item: item["Continent"] == "South America", data))
    
    countries = list(map(lambda x: x['Country/Territory'], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))

    '''
    # Analisis y visualizacion de datos mediante la libreia pandas y matplotlib
    df = pd.read_csv('data.csv')
    df = df[df["Continent"] == "Africa"]# En esta caso se usa el filtro para obtener los paises de Sudamerica
    
    countries = df["Country/Territory"].values
    percentages = df["World Population Percentage"].values
    
    charts.generate_pie_chart(countries, percentages)
    
    data = read_csv.read_csv('data.csv')
    country = input("Type Country => ")
    print(country)

    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == "__main__":
    run()
