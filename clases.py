# CLASES

# Una clase es una plantilla común para la creación de objetos.
# Los objetos son los elementos diferentes entre si pero comparten la misma clase.
# Las clases (plantillas) no se inicializan, los objetos o tambien llamados ejemplar de clase si.

# (instancia / ejemplar de clase / objeto) Significan lo mismo.

# EJ: Una clase puede ser humano, mientras que algunas instancias pueden ser hombre y mujer.
# En la practica clases y instancias se trabajan como lo mismo (class) pero este concepto de clases y instancias 
# nos permitirán modelar mejor los conceptos (Mediante herencia) y así trabajar más modularizado. 

# OBS: Las clases siempre deben estar encapsuladas, esto quiere decir que solo la clase debe saber como realiza sus tareas y
# poseer metodos para la comunicación de resultados finales, sin exponer la forma en que trabaja y sin generar dependencia de
# metodos de otras clases.

# CREAR UNA CLASE
class Auto ():
    # CONSTRUCTOR
    def __init__(self):
        # En python no existen las palabras reservadas public, protected y private para encapsular, se utiliza un subrayado.
        # "_" para protected y "__" para private, por defecto siempre es public.
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self._enmarcha = False

# Self es el equivalente a this, en otros lenguajes se pasa el contexto por defecto, 
# en python hay que especificarlo como parametro por obligación.
    def prender(self, arrancamos):
        self._enmarcha = arrancamos
        chequeo = self.__chequeo_interno()
        if self._enmarcha and chequeo:
            return "El auto ahora está en marcha."
        elif self._enmarcha and chequeo == False:
            return "Hay un problema con el vehiculo, no ha podido arrancar"
        else:
            return "El auto ahora está detenido."
    
    def informacion(self):
       # OPERADOR TERNARIO
       enmarcha = "En marcha" if self._enmarcha else "Detenido"
       print("Acho chasis:", self.__anchoChasis, "Largo chasis:", self.__largoChasis,"Ruedas:", self.__ruedas, "Estado:", enmarcha)

    # El metodo de encapsulación es equivalente para propiedades y metodos
    def __chequeo_interno(self):
        return True
    
# Instanciar una clase
miAuto = Auto()
# Acceder a las propiedades / metodos
print(miAuto.prender(True))
miAuto.informacion()
