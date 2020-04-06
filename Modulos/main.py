# IMPORTAR MODULOS

# Considerar que el metodo de importación está directamente relacionado con la velocidad de ejecución.
# Si una libreria es extremadamente extensa y solo utilizarás dos funciones, es mejor importar solo
# lo que se va a utilizar.

# OBS: Para importar un modulo debe estar en el mismo nivel que el fichero que lo llama, no se puede usar ruta relativa o absoluta.
#      Si no encuentra el modulo, lo irá a buscar al syspath (ruta de instalación de python).
#      Para tener el modulo donde se te antoje, se debe hacer un paquete.

# Importar y usar el nombre del modulo por defecto 
# import funciones_matematicas

# Importar y usar el nombre del modulo con un alias
# import funciones_matematicas as calculadora 

# Importar una función en particular
# OBS: Al importar la función se puede utilizar directamente como sumar(a,b), sin usar el nombre del modulo.
# from funciones_matematicas import sumar

# Importar todo sin necesidad de usar el nombre del modulo
from funciones_matematicas import * 

sumar(1,2)
restar(8,2)