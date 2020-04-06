# Las tuplas son listas inmutables desde su instancia, el equivalente a las
# constantes en otros lenguajes. Permite obtener una porción de lista pero 
# la entrega como una nueva tupla.

# ¿Ventajas sobre las listas?
# Más rapidas, permiten formatear strings y a diferencia de una lista, 
# puede ser utilizada como claves de diccionario.




# 1 - CREAR TUPLAS

# Crear tupla vacia
mytupla = ()
# Crear tupla con elementos iniciales
mytuple = ('item 1', 'item 2', 'item 3')
# Tupla unitaria
# Obs: Si no se agrega una coma luego del primer elemento, no lo considera una tupla, lo considera el tipo del
#     primer elemento
test = ('item 1',)
# Empaquetado de tupla (Es lo mismo que crear)
# Obs: se puede crear una tupla sin parentesis pero no se recomienda, si se pasa como argumento en funciones
#      puede ser algo confuso
mytuple = 'item 1', 'item 2', 'item 3'
# Desempaquetar una tupla (Pasar a variables el contenido de una tupla manteniendo el orden de izq a der)
item1, item2, item3 = mytuple




# 2 - ACCEDER A ELEMENTOS

# Acceder a un elemento por su indice
mytuple[1]

# 3 - PORCIONES DE TUPLAS

# Desde el primer indice hasta uno especifico
mytuple[:2]
# Desde un indice especifico hasta el ultimo
mytuple[2:]
# Una porción especifica mediante indices
mytuple[1:2]
# Toda la tupla
mytuple[:] 




# 4 - COMPROBACIONES

'item 1' in mytuple




# 5 - OTROS

# Comprobar el tipo de la variable
type(mytuple)
# Transformar tupla a lista
mylist = list(mytuple)
# Contar repeticiones de un elemento especifico dentro de la tupla
element = 'not found'
mytuple.count(element)
# Obtener la cantidad de elementos dentro de una tupla
len(mytuple)