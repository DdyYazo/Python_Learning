import psycopg2

try:
    conn = psycopg2.connect(
        user='postgres',
        password='password_assigment',
        root='127.0.0.0',
        port='5432',
        database='test_db'
    )
    print("Conexion exitosa a la base de datos")
except psycopg2.Error as error:
    print("Ocurrio un error con la conexión a la base de datos", error)
    
    conn.close()