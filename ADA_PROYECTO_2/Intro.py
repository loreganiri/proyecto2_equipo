import os   

print("Hola Bienvenido a Pelimovie")
print("Escoge que deseas hacer (typea el numero)")
print("1.- Agregar pelicula")
print("2.- Listar peliculas")
print("3.- Eliminar catalogo de peliculas")
print("4.- Salir")

while True:
   print("Dame un numero entre 1 y 4: ")
   choose=int(input())
   if choose not in range(1,5):
       print("Opcion invalida, intenta de nuevo")
   else:
        if choose == 1:
            from pathlib import Path
            print("Escogio la 1")   
            try:
                with open('Catalogo.txt') as f:     
                    print("El archivo existe")
                    import AgregarPeli
                    from AgregarPeli import *  

            except FileNotFoundError:
                print("El archivo aun no existe")
                import Catalogo_no_existe
                from Catalogo_no_existe import *
            
        elif choose == 2:
            try: 
               with open('Catalogo.txt') as f:      
                print("Mostrar peliculas existentes en el catalogo")
                import Mostrar_pelis_existentes
                from Mostrar_pelis_existentes import * 
            except FileNotFoundError:
                print("El archivo no existe, por favor registra una pelicula primero.")  
        elif choose == 3:
                print("Eliminacion del Catalogo en proceso")
                import os
                file = 'Catalogo.txt'
                if os.path.exists(file): 
                    os.remove(file)
                    print("Este archivo fue eliminado con exito")
                else:
                    print("No se encontro tal archivo")
        else:
            if choose ==4:
                print("Muchas gracias por visitarnos! Adios!")
                exit()

                
        

   










# Aqui checaremos si el catalogo existe, sino para crear uno nuevo
#if os.path.exists('catalogo.txt'):
#   print('The file exists')
#else:
#   print('The file does not exist')

