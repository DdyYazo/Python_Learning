from os import system

system('clear')

class CorreoElectronico:
    def __init__(self, cuenta):
        if not cuenta.endswith(self.sufijo):
            raise ValueError("La cuenta de correo electrónico no es válida")
        self.cuenta = cuenta
      
class CorreoGmail(CorreoElectronico):
    sufijo = "@gmail.com" 
    def send_email(self):
        if not self.cuenta.count("@") == 1:
            raise ValueError("La cuenta de correo electrónico no es válida")
        print("Enviando correo electrónico a", self.cuenta)

class CorreoHotmail(CorreoElectronico):
    sufijo = "@hotmail.com"
    def send_email(self):
        if not self.cuenta.count("@") == 1:
            raise ValueError("La cuenta de correo electrónico no es válida")
        print("Enviando correo electrónico a", self.cuenta)

# Crear objetos de las clases CorreoGmail y CorreoHotmail
correo_gmail = CorreoGmail("pepe@gmail.com")
correo_hotmail = CorreoHotmail("p@pe2@hotmail.com")


# Llamar al método send_email de cada objeto
correo_gmail.send_email() # Enviando correo electrónico a
correo_hotmail.send_email() # Enviando correo electrónico a
