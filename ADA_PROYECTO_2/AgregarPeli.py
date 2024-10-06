

while True:
    print("Escribe el nombre de la pelicula a registrar")
    Nombre_Peli = input()
    with open ("Catalogo.txt", 'a') as archivo:
      archivo.write(Nombre_Peli)
      archivo.write("\n")
      print(Nombre_Peli)
      print("¿Deseas agregar otra pelicula? SI/NO")
      otra = input()
    
    if otra.lower()in ["si"]:
      import AgregarPeli
      from AgregarPeli import *
           
    elif otra.lower() in ["no"]:
       print("Ok, gracias, adiosito!")
       break
    else:
       print("Opcion invalida, por favor escribe SI ó NO")
       break