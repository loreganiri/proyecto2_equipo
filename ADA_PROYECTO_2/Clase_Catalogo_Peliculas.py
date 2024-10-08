# Crear una clase catálogo que gestione los diferentes catálogos de películas
import AgregarPeli

class CatalogoPeliculas():                                 # El nombre de el catálogo de películas
    def __init__(self, nombre_catalogo, ruta_catalogo):     # La ruta del archivo donde se va a guardar el catálogo
        self.nombre_catalogo = nombre_catalogo
        self.ruta_catalogo   = ruta_catalogo

    def agregar_pelicula(self, pelicula):  # Escribir películas en el archivo
         with open(self.ruta_catalogo, 'a') as archivo:
            archivo.write(f"{pelicula}\n")                    
         return 'La película se agregó en el catálogo'
        #resultado = AgregarPeli.agregar_pelicula(self.ruta_catalogo, pelicula)
        #return resultado

# Ejemplo de uso
catalogo = CatalogoPeliculas("Mi Catálogo", "Catalogo.txt")
print(catalogo.agregar_pelicula('Nueva película'))


