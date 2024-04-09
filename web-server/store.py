import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories') # Se establece la conexión con la API usando el metodo GET
    print(r.status_code) # Se imprime el estado de la conexión
    print(r.text) # Se imprime el contenido de la conexión
    print(type(r.text)) # Se imprime el tipo de dato de la conexión
    categories = r.json() # Se convierte el contenido de la conexión a un objeto JSON
    for category in categories:
        print(category['name']) # Se imprime el nombre de cada categoría