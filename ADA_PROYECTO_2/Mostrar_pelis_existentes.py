
archivo = open('Catalogo.txt', 'r')
with open ("Catalogo.txt", 'r') as archivo:
   print("Leyendo el archivo linea por linea con readline(): ")
   linea = archivo.readline()
   while linea:
       print(linea.strip())
       linea = archivo.readline()
   print("-" * 40)