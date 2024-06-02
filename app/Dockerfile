# Especificar desde que version de python se va a trabajar para la imagen 
FROM python:3.9


# Ahora se especifica la carpeta del espacio de trabajo
WORKDIR /app

# Una buena practica es copiar las dependencias de python a la carpeta de trabajo el lado izquierdo es la carpeta local y el lado derecho es la carpeta de trabajo o del contenedor
COPY requirements.txt /app/requirements.txt

# Ahora se dejan instaladas las dependencias y ademas se omite la cache para que no se guarde en el contenedor y tambien se actualizan las dependencias

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Ahora se copian los archivos de la aplicacion a la carpeta de trabajo, el punto es para copiar todo el contenido de la carpeta actual

COPY . /app

# Ahora se especifica el comando que se va a ejecutar cuando se inicie el contenedor para que no se cierre

CMD bash -c "while true; do sleep 1; done"