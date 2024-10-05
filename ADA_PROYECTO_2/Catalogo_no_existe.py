

with open ("Catalogo.txt", 'w') as archivo:
   while True:
    print("Escribe el nombre de la pelicula a registrar")
    Nombre_Peli = input()
    archivo.write(Nombre_Peli)
    print(Nombre_Peli)
    print("¿Deseas agregar otra pelicula? SI/NO")
    otra = input()
    
    if otra.lower()in ["si"]:
        archivo = open('Catalogo.txt', 'a')
        with open ("Catalogo.txt", 'a') as archivo:
           print("Nombre de la pelicula que deseas agregar: ")
           Nombre_Peli = input()
           archivo.write(Nombre_Peli)
        
           
    elif otra.lower() in ["no"]:
       print("Ok, gracias, adiosito!")
       break
    else:
       print("Opcion invalida, por favor escribe SI ó NO")
       

