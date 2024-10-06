
archivo = open('Catalogo.txt', 'r')
with open ("Catalogo.txt", 'r') as archivo:
   linea = archivo.readline()
   while linea:
       print(linea.strip())
       linea = archivo.readline()
  

print("¿Deseas agregar otra pelicula?")
otra = input()
if otra.lower()in ["si"]:
      import AgregarPeli
      from AgregarPeli import *
else: 
      otra.lower() in ["no"]
      print("Ok, gracias, adiosito!")
      