# Crear una clase catálogo que gestione los diferentes catálogos de películas
import AgregarPeli                                          # Importa el módulo AgregarPeli
import Mostrar_pelis_existentes                             # Importa el módulo Mostrar_pelis_existentes 

class CatalogoPeliculas():                                 # El nombre de el catálogo de películas
    def __init__(self, nombre_catalogo, ruta_catalogo):    # La ruta del archivo donde se va a guardar el catálogo
        self.nombre_catalogo = nombre_catalogo
        self.ruta_catalogo   = ruta_catalogo

# Método para agregar películas.

    def agregar_pelicula(self, pelicula):                   # Escribir películas en el archivo
         with open(self.ruta_catalogo, 'a') as archivo:
            archivo.write(f"{pelicula}\n")                    
         return 'La película se agregó en el catálogo\n' 
    
# Método para leer y mostrar las películas.

    def listar_pelicula(self):
       with open(self.ruta_catalogo, 'r') as archivo:
            peliculas = archivo.read()
            return f'Las películas existentes en el catálogo son:\n{self.listar_peliculas()   }'




# Ejemplo de uso
catalogo = CatalogoPeliculas("Mi Catálogo", "Catalogo.txt")
print(catalogo.agregar_pelicula('Registro de película nueva'))
print(catalogo.listar_pelicula())

