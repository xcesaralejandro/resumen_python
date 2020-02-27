# CREAR UN PAQUETE DISTRIBUIBLE

# OBS: Este fichero debe ir en la raiz para que tenga acceso a todos los paquetes y siempre debe llamarse setup.py

#Importamos la herramienta de configuración
from setuptools import setup

# Definimos la configuración de nuestro paquete
setup(
    name="paquetecalculos",
    version = 2,
    description = "Este es mi primer paquete",
    author = "César M.",
    author_email = "cesar.mcid@gmail.com",
    url = "www.somepage.cl",
    # Acá va el paquete y los subpaquetes, se empaquetan todos los modulos del respectivo paquete
    packages=[
        "Calculos_paquete", "Calculos_paquete.subpaquete"
    ]
)

# Posteriormente abrir cmd en la ruta donde se encuentra este archivo.
# ejecutar el comando "python setup.py sdist" para crear el paquete distribuible
# Luego de eso nos creará dos carpetas, dist y la carpeta NOMBREPAQUETE.egg-info
# Para distribuir el paquete se utiliza el dentro de la carpeta dist :) 


# Para instalar un paquete, abres cmd en el directorio donde se encuentra el paquete instalable
# usar el comando "pip3 install NOMBREPAQUETE.extensiones"

# Ahora todo lo disponible en el paquete se instaló en el directorio de python y está disponible
# para ser utilizado en cualquier lado.


# para desintalar un paquete se debe utilizar el comando "pip3 uninstall NOMBRE_PAQUETE_EN_EL_SETUP.PY"

