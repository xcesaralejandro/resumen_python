import re


# Busqueda
message = "22-01-20 08:26 - César Alejandro M: ¡Hola regex! esto es un formato para aprender regex."
expresion = "¡Hola"
busqueda_simple = re.search(expresion, message)
print(busqueda_simple)

# Obtener la posición donde comienza la coincidencia   
print(busqueda_simple.start())

# Obtener la posición donde acaba la coincidencia   
print(busqueda_simple.end())

# Obtener una tupla con el inicio y fin de la coincidencia
print(busqueda_simple.span())

# Buscar todas las coincidencias
expresion = "regex"
print(re.findall(expresion, message))

# ANCLAS
nombres = ['Ana Goméz', 'María Martín', 'Sandra López', 'Santiago Martín']


# STRING COMIENZA POR...
# "^" Este caracter seguido de una palabra buscará los strings que comiencen con dicha palabra.
# EJ: '^Sandra', quiere decir que el string debe comenzar coincidiendo con 'Sandra'
print('\n\nComienza con Sandra:')
for nombre in nombres:
    if re.findall('^Sandra', nombre):
        print(nombre)




# STRING FINALIZA POR...
# "$" Una palabra seguida de este caracter buscará los strings que finalicen con la palabra.
# EJ: 'Martín$', quiere decir que el string debe finalizar coincidiendo con 'Martín'
print('\nFinaliza con Martín:')
for nombre in nombres:
    if re.findall('Martín$', nombre):
        print(nombre)




# CLASE DE CARACTERES
# Son patrones de busqueda dentro un texto y se ponen dentro de []
# OBS: No importa el orden de los caracteres dentro de los corchetes, solo buscará si está o no.
dominios = ["http://www.google.cl","http://www.facebook.com", "http://www.españa.es"]
print('\nClase de caracteres, buscar por ñ:')
for dominio in dominios:
    # En este caso no buscará la palabra 'ña', si no que traerá los strings que tengan una ñ y una a 
    # sin importar si la 'a' está antes o despues de la 'ñ' y viceversa
    if re.findall('[ña]', dominio):
        print(dominio)

# El siguiente ejemplo nos ayudará a entender mejor la utilidad. Otro ejemplo practico puede ser para 
# buscar coincidencias en palabras que llevan acentos y no se sabe si están con ellos [aá]. 
perfiles = ["Adulto", "Joven", "niños", "niñas"]
for perfil in perfiles:
    if re.findall('niñ[oa]s', perfil):
        print(perfil)




# RANGOS
# Se ubican dentro de [] y están separados por el caracter "-", aplica tanto para letras 
# del abecedario como para numeros
nombres = ['Ana', 'Pamela', 'Pedro', 'María', 'Rosa', 'Sandra', 'Celia']
print("\nRangos:")
print("\nMostrar nombres que contienen algún caracter desde 'o' hasta 't', incluyendo 'o' o 't'")
for nombre in nombres:
    # Mostrará los nombres que contengan una o-p-q-r-s-t
    if re.findall('[o-t]', nombre):
        print(nombre)

sucursales = ['stgo1', 'stgo2', 'stgo3', 'ccp1', 'ccp2', 'vm1', 'stgo4', 'ccpA','stgoA','stgoF']
print("\nSucursales en un rango de 1 a 3 (Inclusive)")
for sucursal in sucursales:
    if re.findall('[1-3]$', sucursal):
        print(sucursal)




# RANGO NEGADO
# Un rango negado devolverá todos valores que no coinciden con el rango a buscar, para negar 
# el rango se debe anteponer ^
print("\nSucursales en un rango negado de '1' a '3' (Inclusive)")
for sucursal in sucursales:
    if re.findall('[^1-3]$', sucursal):
        print(sucursal)


# MULTIPLE RANGO
# Tambien se pueden combinar rangos de la siguiente forma [1-3A-C]
# Esto se trauce en [123ABC], Lo cual buscará la coincidencia de cualquiera de esos caracteres
print("\nSucursales stgo de '1' a '3' y de 'A' a 'C' (Inclusive)")
for sucursal in sucursales:
    if re.findall('stgo[1-3A-C]$', sucursal):
        print(sucursal)


# MATCH function
# La función match buscará las coincidencias desde el comienzo, recibe 3 parametros donde el tercero
# es opcional y puede ser alguna recla como re.IGNORECASE

names = ["Sandra Lopéz", "César Mora", "Hector Lopéz", "sandra figueroa"]
print("\nFunción MATCH con ignore case para la palabra sandra.")
for name in names:
    if re.match('Sandra', name, re.IGNORECASE):
        print("(SI) - ", name)
    else:
        print("(NO) - ", name)




# SEARCH function
# La función search buscará las coincidencias sin importar la ubicación dentro del string
names = ["Sandra Lopéz Rodriguez", "César Mora Cid", "Hector Galez Lopéz"]
print("\nFunción SEARCH para la palabra Lopéz.")
for name in names:
    if re.search('Lopéz', name, re.IGNORECASE):
        print("(SI) - ", name)
    else:
        print("(NO) - ", name)



# COMODINES DE CARACTER

# El "." nos permitirá reemplazar un caracter en particular (Excepto un salto de linea)
names = ["Lara", "hector", "Jara", "sandra"]
print("\nUtilizando el comodín .ara")
for name in names:
    if re.match('.ara', name, re.IGNORECASE):
        print(name)


# "\d" quiere decir que el caracter es un numero cualquiera
codes = ["a8561", "254621", "FAE42", "C-005-12QWE"]
print("\nUtilizando el comodín numerico")
for code in codes:
    if re.match("\d", code):
        print(code)




# CHEAT SHEET DE REGEX
# https://gist.github.com/vitorbritto/9ff58ef998100b8f19a0









