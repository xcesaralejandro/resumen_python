# Los diccionarios son el equivalente a un array clave:valor en otros lenguajes

# 1 - CREAR DICCIONARIO

# Crear diccionario vacia
mydictionary = {}
# Crear diccionario con elementos iniciales
mydictionary = {'name' : 'César', 'lastname':'mora', 'age': 24}




# 2 - ACCEDER A ELEMENTOS

# Acceder a un elemento mediante su clave
mydictionary['name']




# 3 - AGREGAR ELEMENTOS

# Añadir un nuevo elemento
# Obs: si la clave ya existe, sobrescribe el valor
mydictionary['gender'] = 'm'




# 4 - ELIMINAR ELEMENTOS

# Eliminar un elemento del diccionario mediante su clave
del mydictionary['gender']




# 5 - OTROS

# Obtener solo las claves de un diccionario 
mydictionary.keys()
# Obtener solo los valores de un diccionario 
mydictionary.values()
# Obtener el tamaño del diccionario 
len(mydictionary)
# Comprobar el tipo de la variable
type(mydictionary)