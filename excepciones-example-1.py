# EXCEPCIONES

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplica(a,b):
    return a * b

def divide (a,b):
# CONTROL DE EXCEPCIÓN 
    try:
        return a / b
    # El nombre de la excepción aparace en el seguimiento de pila cuando se lanza el error.
    except ZeroDivisionError :
        print("No se puede dividir por cero, gato.")
        return "No se ha realizado la operación"

other = "s"
while (other.lower() == "s"):
    # CONTROL DE EXCEPCIÓN
    # El while infitino combinado con el try-except permitirán pedir los numeros de nuevo
    # cuando se lance una excepción.
    while True:
        try:
            a_number = int(input("Numero 1:"))
            operation = input("Operación: [suma,resta,multiplica,divide]")
            b_number = int(input("Numero 2:"))
            break
        #El nombre de la excepción aparace en el seguimiento de pila cuando se lanza el error.
        except ValueError:
            print("Los valores ingresados son incorrectos, intentalo de nuevo")

    print("RESULTADO:")
    if(operation.lower() == "suma"):
        print(suma(a_number,b_number))
    elif (operation.lower() == "resta"):
        print(resta(a_number,b_number))
    elif (operation.lower() == "multiplica"):
        print(multiplica(a_number,b_number))
    elif (operation.lower() == "divide"):
        print(divide(a_number,b_number))
    else:
        print("operation not found. ")
    print("Some code here...")
    other = input("¿Desea realizar otra operación? (s/n)")