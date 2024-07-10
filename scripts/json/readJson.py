from os import system

system('clear')


import json
import urllib.request

# Debido a cambios en la libreria ahora se deben pasar algunos cabeceros html

url = 'http://globalmentoring.com.mx/api/personas.json'
headers = { 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36' }

peticion = urllib.request.Request(url, data=None, headers=headers)

url = urllib.request.urlopen(peticion)
body = url.read()
print(body)
print()

# Procesamos la respuesta json
json_response = json.loads(body.decode("utf-8"))
print(json_response)
print()

# Imprimimos sólo los nombres de las personas
# json se convierte a listas y diccionarios de python
print('Nombres de las personas en el archivo json: \n')
for persona in json_response['personas']:
    print(f'Persona: {persona["nombre"]}, {persona["edad"]}')


# Accedemos al total de personas de archivo
print(f'Total de personas: {json_response["total"]}')

# Accedemos al mensaje del archivo
print(f'Mensaje: {json_response["mensaje"]}')

""" Guardar el archivo json en un archivo local """