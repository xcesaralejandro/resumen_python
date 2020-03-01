# ARCHIVOS EXTERNOS
# Para trabajar con archivos externos requeriremos la libreria IO
from io import open

# Modos soportados

# (r) read -> Solo leer
# (w) write -> Escribir (Sobrescribe la información anterior)
# (a) append -> Agregar información a un archivo existente y con información anterior
# (r+) read & write -> Lectura y escritura

# Escribir 
archivo = open("archivo_creado_con_python.txt","w")
frase = "Mi texto deste python :) \n jejejeje :)"
archivo.write(frase)
archivo.close()


# Leer
archivo = open("archivo_creado_con_python.txt","r")
# OBS: Otro medoto util puede ser .readlines() y guarda las lineas como una lista.
#      Del mismo modo existe writelines para escribir un documento desde una lista.
texto_archivo = archivo.read()
archivo.close()
print(texto_archivo)

# Puntero (En palabras simples es como la posición del cursor)
archivo = open("archivo_creado_con_python.txt","r")
# OBS: Cuando leemos el puntero comienza en el inicio hasta el final, si volvemos a leer por segunda vez
#      no mostrará nada, ya que el puntero se encontrará en el final y no habrá nada para obtener.
#      si pasamos el parametro opcional de limite de lectura la primera vez, la segunda vez que leamos
#      seguirá desde el punto anterior, no desde el principio. 
texto_archivo = archivo.read()
# Posicionar el puntero
archivo.seek(0)
# read recibe un parametro opcional que corresponde a la cantidad de caracteres a leer desde el punto actual.
texto_archivo = archivo.read(12)
archivo.close()
print(texto_archivo)



input()
