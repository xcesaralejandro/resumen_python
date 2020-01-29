#Ciclos de iteraciones disponibles en python

# 1 - FOR

# Recorrer lista de elementos
somethings = ['something 1','something 2','something 3']
for something in somethings:
    print(something) 
# Ejecutar ciclo con un valor predeterminado
hasta = 5
for i in range(hasta):
    print("Elemento " + str(i))
# Ejecutar ciclo en un rango predeterminado
desde = 5
hasta = 10
for i in range(desde, hasta):
    print("Elemento " + str(i))
# Ejecutar ciclo con un rango predeterminado contando en más de uno por iteración
desde = 10
hasta = 20 
incremento = 2
for i in range(desde, hasta, incremento):
    print("Elemento " + str(i))




# 2 - WHILE

# Sentencia while standard
count = 0
while count < 2:
    count+=1
    print("Contador ciclo while: " + str(count))




# 3 - FUJOS DE ITERACIÓN (continue, pass, else, break)

#CONTINUE: Salta a la siguiente iteración sin ejecutar el codigo que sigue a continuación en la iteracción actual
for letra in "¿hola como estás?":
    if letra == " ":
        continue 
    print (letra, end = "")
print("")
#BREAK: Interrumpe la continuidad del ciclo sin ejecutar más iteraciones
for letra in "¿hola como estás?":
    if letra == " ":
        break 
    print (letra, end = "")
print("")
# ELSE
# OBS: Se ejecuta luego de recorrer el ciclo.
for i in range(2):
    print(f"Ciclo con else, iteración {i}")
else: # Puede ser util instanciar variables que no se hayan cumplido en las iteraciones o cuando se itera en listas vacias.
    print("Este else se ejecuta luego del ciclo")
# PASS: Devuelve null en cuanto se lee el bucle, puede ser util para implementar cosas más tarde
# OBS: while infitino, el pass permite seguir la ejecución al retornar null
while True: 
    pass #permite seguir con la ejecución manteniendo el ciclo
class MiClass:
    pass #permite seguir con la ejecución manteniendo la declaración de la clase 




# 4 - OTROS

# Concatenar variables dentro de texto
edad = 24
print(f"Hola, mi edad es : {edad}")