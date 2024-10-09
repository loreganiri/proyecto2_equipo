
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
       print("¡Ok! ¡Gracias, adiosito!")
       break
    else:
       print("Opción inválida. Por favor escribe SI o NO")
       break