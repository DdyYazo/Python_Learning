from os import system

# import csv
system("clear")


""" Esta función lee un archivo CSV y devuelve su contenido como una lista de diccionarios. """
""" def get_argentina_data(path):
    with open(path, "r") as file:
        reader = csv.DictReader(file)

        # Filtrar la fila del país de Argentina y seleccionar solo las columnas de los años
        for row in reader:
            if 'Country/Territory' in row and row["Country/Territory"] == "Argentina":
                data = {labels: values for labels, values in row.items() if 'Population' in labels}
                break
    return data

if __name__ == "__main__":
    data = get_argentina_data('./30_chall_chart-csv/data.csv')
    print(data)  # Output: {'Population (2020)': '45195', 'Population (2019)': '44939', 'Population (2018)': '44689', 'Population (2017)': '44494', 'Population (2016)': '44271', 'Population (2015)': '44045', 'Population (2014)': '43847', 'Population (2013)': '43660', 'Population (2012)': '43417', 'Population (2011)': '43132', 'Population (2010)': '42871', 'Population (2009)': '42626', 'Population (2008)': '42377', 'Population (2007)': '42115', 'Population (2006)': '41841', 'Population (2005)': '41553', 'Population (2004)': '41262', 'Population (2003)': '40969', 'Population (2002)': '40678', 'Population (2001)': '40382', 'Population (2000)': '40038'}
 """
 
def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
    result = list(filter(lambda item: item['Country/Territory'] == country, data))
    return result

""" Esta función recibe una lista de diccionarios y un país, y devuelve el diccionario correspondiente a ese país."""
""" def population_by_country(data, country):
    result = next((item for item in data if item.get('Country/Territory') == country), None)
    return result """