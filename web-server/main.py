import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


# Definición de la consulta get utilizando la libreria fastapi
@app.get("/")  # especifica la ruta de acceso desde la web
def get_root():
    return {"message": "Hello World", "status": "Im stay in a API"}


@app.get("/contact", response_class=HTMLResponse)
def get_contact():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Contact</h1>
            <p>Send an email to email address <a href="mailto:example@example.com">example@example.com</a></p>
        </body>
    </html>
"""

"""  ---------------- secuence point ----------------"""
# Definición de la consulta get utilizando la libreria requests
def run():
    store.get_categories()

# entry point para el uso de la libreria requests
if __name__ == "__main__":
    run()
