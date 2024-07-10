import urllib.request
import json

url = "http://globalmentoring.com.mx/api/personas.json"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
peticion = urllib.request.Request(url, data=None, headers=headers)

url = urllib.request.urlopen(peticion)
body = url.read()

json_data = json.loads(body.decode("utf-8"))

with open('./scripts/json/prueba.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
 
print('Archivo JSON creado exitosamente')