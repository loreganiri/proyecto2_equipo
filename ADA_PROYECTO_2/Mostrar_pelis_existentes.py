# Abril el archivo 'Catalogo.txt' en modo lectura archivo = open('Catalogo.txt', 'r')
with open ("Catalogo.txt", 'r') as archivo:
      sentencia = archivo.readline()                  # Leer la primera línea del archivo

      while sentencia:                                # Continua leyendo y procesando líneas hasta el final del archivo
       print(linea.strip())                           # Imprime la línea sin espacios en blanco al principio o al final
       sentencia = archivo.readline()                 # Lee la siguiente línea de archivo
  
print("¿Deseas agregar otra película?")               # Preguntar al usuario si desea agregar otra película
otra = input()

if otra.lower()in ["si","sí"]:                         # Verifica la respuesta del usuario
#      import AgregarPeli                               No es necesario mandarlo llamar dos veces
      from AgregarPeli import *                        # Importa el módulo y su contenido
else: 
#      otra.lower() in ["no"]                           La condición no es necesaria
      print("¡Ok! ¡Gracias, adiosito!")                 # Imprime mensaje de despedida
      