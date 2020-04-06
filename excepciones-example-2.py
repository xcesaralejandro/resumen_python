# EXCEPCIONES

# Controlar multiples excepciones
def divide_with_specific_exception():
    try:
        number1 = float(input("Numero 1:"))
        number2 = float(input("Numero 2:"))
        print("La división es: " + str(number1/number2))
    except ZeroDivisionError:
        print("No puedes dividir por 0")
    except ValueError:
        print("El valor ingresado no es valido")
    print("Calculo finalizado.")




# Controlar cualquier excepción
def divide_with_general_exception():
    try:
        number1 = float(input("Numero 1:"))
        number2 = float(input("Numero 2:"))
        print("La división es: " + str(number1/number2))
    except:
        print("Ha ocurrido un error.")
    print("Calculo finalizado.")




# CONTROL DE EXCEPCIONES -> FINALLY
# Esta sentencia sirve para ejecutar codigo SIEMPRE, haya ocurrido la excepción o no.
# En caso de que haya un error (excepción no controlada) ejecutará primero el finally
# y luego lanzará el error de la excepción.
def divide_with_finally():
    try:
        number1 = float(input("Numero 1:"))
        number2 = float(input("Numero 2:"))
        print("La división es: " + str(number1/number2))
    except:
        print("Ha ocurrido un error.")
    finally:
        print("Calculo finalizado.")




# LANZAR EXCEPCIONES
def evaluarEdad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")

    if edad < 20:
        return "Muy joven"
    elif edad < 40:
        return "Joven"
    elif edad < 65:
        return "Adulto"
    elif edad < 100:
        return "Anciano"

try:
    print(evaluarEdad(-10))
# Podemos obtener y mostrar la descripción de la excepción de la siguiente forma
except ValueError as ErrorEdad:
    print(ErrorEdad)