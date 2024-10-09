# Crear una clase catálogo que gestione los diferentes catálogos de películas
# Este archivo tiene la lógica del menú, estoy mandando llamar los módulos que programó Lore

import AgregarPeli
import Mostrar_pelis_existentes

class CatalogoPeliculas:
    def __init__(self, nombre_catalogo, ruta_catalogo):
        self.nombre_catalogo = nombre_catalogo
        self.ruta_catalogo = ruta_catalogo

    def agregar_pelicula(self, titulo, director=None, genero=None, año=None):
        return AgregarPeli.agregar_pelicula(self.ruta_catalogo, titulo, director, genero, año)
    
    def listar_peliculas(self):
        return Mostrar_pelis_existentes.listar_peliculas(self.ruta_catalogo)

    def buscar_pelicula(self, titulo):
        return Mostrar_pelis_existentes.buscar_pelicula(self.ruta_catalogo, titulo)

    def eliminar_pelicula(self, titulo):
        return Mostrar_pelis_existentes.eliminar_pelicula(self.ruta_catalogo, titulo)

# Ejemplo de uso
catalogo = CatalogoPeliculas("Mi Catálogo", "Catalogo.csv")
print(catalogo.agregar_pelicula('Registro de película nueva', 'Director Ejemplo', 'Género Ejemplo', 2024))
print(catalogo.listar_peliculas())
print(catalogo.buscar_pelicula('Registro de película nueva'))
print(catalogo.eliminar_pelicula('Registro de película nueva'))
print(catalogo.listar_peliculas())
