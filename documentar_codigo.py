# DOCUMENTACIÓN

def helloWorld():
    # Los comentarios entre triple comillas ubicados dentro de la función
    # permitirán ser luego consultados mediante helpers.
    # este comentario no será visible para tiempos de ejecución.
    """
        Esta función realiza lo siguiente:
        1) Decir hello world
    """
    print("Hello World")


helloWorld()
# Consultar documentación de una función

# Alternativa 1
print(helloWorld.__doc__)
# Alternativa 2
help(helloWorld)




# FUNCIÓN DENTRO DE UNA CLASE

class Person:
    """ Esta es la clase persona."""
    def sayHello():
        """Esta función de la clase Person dice Hello"""
        print("Hello")

    def sayBye():
        """Esta función de la clase Person dice Bye"""
        print("Bye")

# Consultar la documentación de una función particular
help(Person.sayHello)

# Consultar la documentación de toda la clase
help(Person)