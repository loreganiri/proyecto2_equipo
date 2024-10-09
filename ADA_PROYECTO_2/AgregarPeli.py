
while True:
    print("Escribe el título de la película que vas a registrar: ")
    agregar_pelicula = input()

    with open ("Catalogo.txt", 'a') as archivo:
      archivo.write(agregar_pelicula + "\n")        # Para tener menos líneas solo agregué el +

      print(f'Película {agregar_pelicula} fue registrada.')

      print("¿Deseas agregar otra película? SI/NO")

      otra = input().strip().lower()                # .strip elimina espacios en blanco
    
    if otra in ['si', 'sí']:                        # consideré que el usuario puede no escribir el acento
      #import AgregarPeli
      #from AgregarPeli import *                     # No es necesario importar acá el módulo
           continue
    elif otra in ["no"]:
       print(f'¿Quieres ver la lista de películas? SI/NO\n')
       ver = input().strip().lower()                 # Elimina espacios y pone la entrada en minúsculas
       if ver in['si', 'sí']: 
          with open("Catalogo.txt", 'r') as archivo:
                peliculas = archivo.read()
                print(f'Las películas existentes en el catálogo son:\n{peliculas}')        
       break
    
    else:
       print("Opción inválida. Por favor escribe SI/NO")
       break