import os

os.system('clear')

class MovieCatalog:

    file_route = './challenge_file/catalogo/movies.txt' 

    @classmethod
    def add_movie (cls, movie):
        with open(cls.file_route, 'a+', encoding='utf8') as file:
            file.write(f'{movie.name}\n')

    @classmethod
    def movie_list (cls):
        with open(cls.file_route, 'r', encoding='utf8') as file_list:
            print(f'Catalogo de peliculas:'.center(50,'-'))
            print(file_list.read())

    @classmethod
    def delete_movie(cls):
        os.remove(f'Archivo {cls.file_route} eliminado')
