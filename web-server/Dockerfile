FROM python:3.10

WORKDIR /app
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# En este caso para el caso del servidor web se va a usar uvicorn que es un servidor web asincrono para python y se establece en el puerto 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]