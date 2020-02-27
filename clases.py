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


# PRINCIPIO DE SUSTITUCIÓN
# El principio de sustitución quiere decir "es siempre un/a" es decir, dada la clase empleado que hereda
# de persona, un empleado es siempre una persona, pero una persona no necesariamente es un empleado
# ya que podria estar en otra situación. Este concepto nos ayudará a determinar y asegurarnos que la herencia
# implementada es realmente correcta, ya que si la clase "padre" es siempre el "hijo", entonces 
# el diseño de clases estaria incorrecto. 

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

print("\n")

class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo 
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True
    
    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print("\n Marca:", self.marca, "\n","Modelo:", self.modelo,"\n","En marcha:",self.enmarcha,"\n","Acelera:",
              self.acelera,"\n","Frena:",self.frena)

# HERENCIA
class Moto(Vehiculo):
    haciendo_caballito = ""
    def caballito(self):
        self.haciendo_caballito = "Voy haciendo caballito"
    
    #SOBRESCRITURA DE METODOS
    def estado (self):
        # OBS: Recordar que siempre antes de sobrescribir el metodo se puede ejecutar el original (metodo el del padre) si es necesario
        Vehiculo.estado(self)
        print(" Caballito:", self.haciendo_caballito)

#miMoto = Moto("Honda","CBR")
#miMoto.caballito()
#miMoto.estado()

class Furgoneta(Vehiculo):
    def carga(self,cargado):
        self.cargado = cargado
        if self.cargado:
            return "La furgoneta está cargada."
        else:
            return "La furgoneta no está cargada."

#mifurgoneta = Furgoneta("Renault", "Kangoo")
#mifurgoneta.arrancar()
#mifurgoneta.estado()

class VElectrico():
    def __init__(self):
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True

# MULTIPLE HERENCIA
# En caso de metodos con el mismo nombre primará el de la clase que se encuentre más a la izquierda.
# Como el constructor igual es un metodo, en este caso se utilizará el constructor de la clase VElectrico,
# y como esta clase no recibe argumentos, la instancia de BicicletaElectrica no debe recibir argumentos.

class BicicletaElectrica(VElectrico, Vehiculo):
    # Si solo tuviera una herencia se podria trabajar el constructor padre de la siguiente forma
    # super().__init__(argumentos)
    def __init__(self, color):
        Vehiculo.__init__(self,"bicicleta","mc2000")
        self.color = color

    def estado (self):
        Vehiculo.estado(self)
        print("Color:",self.color)

miBici = BicicletaElectrica("roja")
miBici.arrancar()
miBici.estado()
#Comprobar si una clase es parte de otra. ARGS(mi objeto, clase a comprobar)
print("Mi bici utiliza la clase vehiculo (Herencia):", isinstance(miBici, Vehiculo))


# POLIMORFISMO
# Es la habilidad que tienen los objetos de diferentes clases para responder a metodos con el mismo nombre
# sin importar el tipo del objeto.

# Esta definición de POO es solo para refrescar conceptos :), python no cuenta con sobrecarga de metodos, java si.
# Inicialmente se entiende que Sobrecarga (Diferente a sobreescritura) hace referencia a un conjunto de Métodos 
# con el mismo Nombre pero diferente Número de Parámetros y/o Tipos de estos, además que estos Métodos se encuentran 
# definidos en una misma Clase. En tanto que Polimorfismo hace referencia a un conjunto de Métodos con el mismo Nombre 
# e igual Número de Parámetros y Tipos, pero que se encuentran definidos en diferentes Clases.



class Coche():
    def desplazamiento(self):
        print("Me desplazo con 4 ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo con 2 ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo con 6 ruedas")

def funcionamiento(objeto):
    objeto.desplazamiento()

miMoto = Moto()
miCamion = Camion()
miCoche = Coche()

funcionamiento(miMoto)
funcionamiento(miCamion)
funcionamiento(miCoche)
