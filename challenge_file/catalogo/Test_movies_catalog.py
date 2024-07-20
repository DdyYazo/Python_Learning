from domain.Movies import Movie as mov
from service_cat.MovieCatalog import MovieCatalog as movc

opc = None
while opc != 4:
    try:
        print('Opciones que puedes elegir \n'.center(50,'-'))
        print('1. Agregar pelicula')
        print('2. Listar pelicula')
        print('3. Eliminar pelicula')
        print('4. Salir \n')
        opc = int(input('Selecciona una opción (1-4):'))  # Corrección aquí: asignar a opc en lugar de select
        
        print('')
        if opc == 1:
            name_movie = input("Ingresa el nombre de la pelicula: ")
            pelicula = mov(name_movie)
            movc.add_movie(pelicula)
        elif opc == 2:
            movc.movie_list()
        elif opc == 3:
            movc.delete_movie()
        """ elif opc == 4:
            print('Se finalizo el programa')
        else:
            print('Opción inválida, por favor intenta de nuevo.') """
    except Exception as e:
        print(f'Error opción invalida {e}')
        opc = None
else:
    print('Se finalizo el programa')