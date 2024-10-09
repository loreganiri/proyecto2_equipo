
while True:
    print("Escribe el título de la película que vas a registrar")
    agregar_pelicula = input()
    with open ("Catalogo.txt", 'a') as archivo:
      archivo.write(agregar_pelicula)
      archivo.write("\n")
     # print(agregar_pelicula)
      print("¿Deseas agregar otra película? SI/NO")
      otra = input()
    
    if otra.lower()in ["sí"]:
      import AgregarPeli
      from AgregarPeli import *
           
    elif otra.lower() in ["no"]:
       print("¡Ok! ¡Gracias, adiosito!")
       break
    else:
       print("Opción inválida. Por favor escribe SI o NO")
       break