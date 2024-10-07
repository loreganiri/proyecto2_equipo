# Esta clase se encargará de representar una película con sus atributos, como el nombre.

class Pelicula:
    tipo = 'Cine'
    
    def __init__(self, __titulo, anio, genero, __director):
        self.__titulo   = __titulo                               # Atributo de instancia
        self.anio       = anio
        self.genero     = genero
        self.__director = __director

# Método para mostrar información
    def mostrar_info(self):
        print(f'Nombre de la película: {self.__titulo}, el género es {self.genero}.')
        print(f'El director fue {self.__director} en el año {self.anio}')  # Imprime la información

    # Getter con @property
    @property
    def titulo(self):
        return self.__titulo
# El decorador @property convierte el método titulo en un getter,
#  permitiendo acceder al atributo __titulo de manera controlada.
    @property
    def director(self):
    
    # Setter con @nombre.setter
    @titulo.setter
    def titulo(self, nuevo_titulo):
        if isinstance(nuevo_titulo, str):
            self.__titulo = nuevo_titulo
        else:
            raise ValueError('El nombre debe ser una cadena de texto')
# El decorador @titulo.setter define un setter para el atributo __titulo,
#  permitiendo modificar su valor solo si nuevo_titulo es una cadena de texto.
#  Si no lo es, se lanza un ValueError.
    
# Uso de la propiedad
pelicula = Pelicula('Matriz', 1999, 'Ciencia Ficción', 'Lana Wachowski')
print(pelicula.titulo)  # Llama al getter sin usar paréntesis
pelicula.titulo = 'Matrix'  # Llama al setter como una asignación directa
print(pelicula.titulo)  # Accede nuevamente al atributo usando getter}

pelicula = Pelicula('Una familia normal', 2023, 'Drama', 'Per Hanefjord'))

mostrar_info.pelicula
