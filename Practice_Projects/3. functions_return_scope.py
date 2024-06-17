import random
import os

os.system("clear")


""" Completar la función message_creator para que retorne un mensaje distinto dependiendo del artículo de tecnología que reciba como entrada.

La función message_creator recibirá como entrada un string que indica el artículo de tecnología. Luego, deberás evaluar el valor de este string y retornar un mensaje distinto dependiendo del valor que reciba. 
La implementacion debe responder al siguiente comportamiento:

Si recibes una computadora, debes retornar el mensaje: "Con mi computadora puedo programar usando Python".
Si recibes un celular, debes retornar el mensaje: "En mi celular puedo aprender usando la app de Platzi".
Si recibes un cable, debes retornar el mensaje: "¡Hay un cable en mi bota!".
Y si no recibes ninguno de estos valores, debes retornar el mensaje: "Artículo no encontrado". """


def message_creator(text):
    if text == "computadora":
        return "Con mi computadora puedo programar usando Python"
    elif text == "celular":
        return "En mi celular puedo aprender usando la app de Platzi"
    elif text == "cable":
        return "¡Hay un cable en mi bota!"
    else:
        return "Artículo no encontrado"

""" 
text = "computadora"
response = message_creator(text)
print(response) """


# Solución del reto usando comprehension lists
def message_creator(text):
    return [
        f"Con mi {text} puedo programar usando Python"
        if text == "computadora"
        else f"En mi {text} puedo aprender usando la app de Platzi"
        if text == "celular"
        else f"¡Hay un {text} en mi bota!"
        if text == "cable"
        else "Artículo no encontrado"
    ]
# Ejecución del reto
text = "computadora"
response = message_creator(text)
print(response)

# Solución del reto usando case switch
def message_creator(text):
    switcher = {
        "computadora": "Con mi computadora puedo programar usando Python",
        "celular": "En mi celular puedo aprender usando la app de Platzi",
        "cable": "¡Hay un cable en mi bota!",
    }
    return switcher.get(text, "Artículo no encontrado")
# Ejecución del reto
text = "oso"
response = message_creator(text)
print(response)

# Solución del reto utilizando interacción con el usuario
def message_creator(text):
    switcher = {
        "computadora": "Con mi computadora puedo programar usando Python",
        "celular": "En mi celular puedo aprender usando la app de Platzi",
        "cable": "¡Hay un cable en mi bota!",
    }
    return switcher.get(text, "Artículo no encontrado")
text = input("Ingresa un artículo de tecnología: ")
response = message_creator(text)
print(response)
