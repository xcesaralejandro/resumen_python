# DECORADORES

# Los decoradores son funciones que a su vez añaden funcionalidades a otras funciones
# Los decoradores están formados de 3 funciones (A, B, C). Donde A recibe como parametro
# a B para devolver C.
# Un decorador devuelve una función.

# Obs: La función decorador no requiere de algún nombre en particular
def presentacion(some_function):
    # La función interior tampoco requiere de un nombre particular 
    def process():
        print("Hola, yo soy...")
        some_function()
        print("y es un gusto conocerte.")
    return process

# Para decorar una función hay que agregar "@" seguido del nombre de la función, la función
# se sigue llamando con su nombre original.
@presentacion
def nombre1():
    print("César")

def nombre2():
    print("Fernanda")

# Función decorada
nombre1()
print("\n")
# Función sin decorar
nombre2()



# PASAR PARAMETROS AL DECORADOR
def add_operation_info(function):
    # * equivale a un numero indeterminado de parametros
    # ** equivale a un numero indeterminado de parametros, pero clave - valor
    # OBS: Tambien se pueden especificar los parametros
    def internal_function(*args, **kwargs):
        print("------------------------------------")
        print("La operación ha dado como resultado:")
        function(*args, **kwargs)
        print("------------------------------------")
    return internal_function

@add_operation_info
def suma(num1, num2):
    print(num1+num2)

@add_operation_info
def potencia(base, exponente):
    print(pow(base, exponente))

suma(5,5)
print("\n")
potencia(base=5, exponente=3)