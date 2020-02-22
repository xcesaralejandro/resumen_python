# GENERADORES
# Los generadores son funciones que retornan un elemento iterable.
# (Es como si devolvieran una pila, por la forma en que se leen los elementos).

# Cuando se almacena un valor permanece pausado hasta que se solicita el siguiente,
# a esto se le conoce como "suspensión de estado"

# Ventajas sobre una función normal:
# - Más eficiente que las funciones tradicionales
# - Muy utiles para listas de valores infinitos


# Traditional function


def traditional_function(quantity):
    number = 1
    numbers = []
    while number <= quantity:
        numbers.append(number * 2)
        number += 1
    return numbers
print("Traditional function will return:")
print(traditional_function(10))


# YIELD - Generator function
# OBS: se utiliza la palabra reservada yield y esta no detiene la ejecución del codigo.


def generator_function(quantity):
    number = 1
    while number <= quantity:
        yield number * 2 #Esto es como si tuviera una lista e hiciera un append del valor
        number += 1


# Understanding generators


generated = generator_function(10)
print("Generator function will return")
print(next(generated)) #Para obtener un valor se debe utilizar next o realizar una iteración
print("Some code here...")
print(next(generated)) #Acá podemos apreciar que continua del valor anterior, no desde el comienzo.
print("Some code here...")
print(next(generated))

# Tambien podemos recorrer los elementos, si anteriormente se utilizó next, continuará desde ahí
print("Use iterations to cycle through numbers")
for generated_number in generated:
    print(generated_number)

# YIELD FROM
# El YIELD FROM busca evitar un doble ciclo para agregar sub-elementos
#El * antes del argumento quiere decir que recibirá un numero indeterminado de argumentos en formato de tupla
def devuelve_ciudades(*cities): 
    for city in cities:
        yield from city
cities = devuelve_ciudades(["Concepción", "Chillan"], ["Pucon","Tomé"])
print("Results of YIELD FROM")
print(next(cities))
print(next(cities))
print(next(cities))
print(next(cities))
