# Las condicionales en python no llevan corchetes pero se entiende como parte de la condicional
# la identación hacia la derecha.
# Para salir de la condicional simplemente hay que romper la identación
# Los operadores logicos validos acá son: and, or, in
# La sentencia switch no existe

# EXAMPLE 1
# IF
oranges = 1
print("You've " + str(oranges) + " Orange(s)")
if oranges > 0:
    print("You can make orange juicy")




# EXAMPLE 2
# IF - ELSE
songs = 0
print("You've " + str(songs) + " Song(s)")
if songs > 0:
    print("You can play music")
else:
    print("Yo can't play music")
print("This line is out of the conditional")




# EXAMPLE 3
# IF - ELIF -ELSE
hour = 13
print("Current time: " + str(hour) + " Hours")
if hour >= 0 and hour < 6 :
    print("Early morning")
elif hour >= 6 and hour < 12:
    print("Morning")
elif hour >= 12 and hour < 18:
    print("Late")
elif hour >= 18 and hour < 24:
    print("Night")
else:
    print("Current time error")




# EXAMPLE 4
# Concatenación de operadores de validación
# Obs: las validaciones se leen de izquierda a derecha y si no se cumple, ignora el resto de la condición
age = -7
print("Your age is: " + str(age) + " Years")

if 0 < age < 120:
    print("Valid age")
else:
    print("Incorrect age")
    



# EXAMPLE 5
# Uso del operador logico IN
# Obs: Si se trabaja con strings, es case sensitive
coupon = '25%OFF'
available_cupons = ('25%OFF','15%OFF', '5%OFF','DELIVERYFREE')
if('25%OFF' in available_cupons):
    print("Your coupon is valid")
else:
    print("Coupon not found")

