from os import system

system("clear")

## Iteradores
# Un iterador en pyton es un objeto que representa un flujo de datos. Un objeto es un iterador si implementa el método __iter__ y __next__.

## Ejemplo con ciclo for
for i in range(1, 11):
    print(i)

## Un punto importante en un iterador, es entender el range, el cual  es un iterador que genera una secuencia de números.

## En este caso se recorre cada elemento del iterador de forma manual, haciendo uso de la función next.

my_iter = iter(range(1, 11)) # iter es una función que convierte un objeto iterable en un iterador.
print(my_iter)
print(next(my_iter)) # next es una función que obtiene el siguiente elemento del iterador, iterando manualmente el operador.

## Los iterables son importantes mayormente cuando se quieren leer archivos grandes, ya que no se pueden cargar en memoria y requieran ser leidos de manera secuencial o manualmente, sin embargo, al hacerlo de forma manual, va a haber un límite de memoria que se puede leer, generando un error o excepción.

### Caso donde se generaria una excepción
""" my_iter = iter(range(1, 4))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter)) """ # Se genera una excepción StopIteration, ya que se ha llegado al final del iterador.

## Ejemplo de iteradores con el metodo __iter__ y __next__
class MyNumbers:
    """Una clase que representa un iterador para números del 1 al 20."""
    
    def __iter__(self):
        self.a = 1 # self.a es un atributo de la clase MyNumbers
        return self 
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration # Se genera una excepción StopIteration, ya que se ha llegado al final del iterador.
my_class = MyNumbers()
my_iter = iter(my_class)

