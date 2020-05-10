# PRUEBAS
# importamos la libreria de pruebas
import doctest
import math


# Las pruebas las realizamos con las mismas comillas de comentarios,
# la diferencia es que para escribir el codigo de pruebas hay que utilizar
# una nomenclatura especifica.

# ESTRUCTURA DE LA PRUEBA:
# >>> CODIGO
# ... TABULACIÓN/ANIDACIÓN PARA EL CÓDIGO
# Llamado a la función
# Resultado esperado

# Las pruebas pueden ir mezcladas de documentación y puede haber más de una prueba
# dentro de las """, para ello las pruebas deben estar separadas por una line vacia.
# OBS: Para omitir excepciones en el codigo de pruebas se puede poner exactamente el
# codigo arrojado en la excepción con los valores gatillantes del error, tal cual.
# Si salta una excepción y usted la tiene controlada pero con los valores gatillantes
# diferentes, no funcionará.
# Para omitir los valores gatillantes de la expción y controlar la excepción por tipo
# se debe agregar solo la primera y ultima linea, poniendo entre medio '...' precedido
# de una tabulación

def raizCuadrada(listaNumeros):
    """
    Este es un bloque de pruebas.

    La siguiente prueba pasa sin problemas:

    >>> lista=[]
    >>> for n in [4, 9, 16]:
    ...     lista.append(n)
    >>> raizCuadrada(lista)
    [2.0, 3.0, 4.0]

    Este código falla, por que no se puede obtener la raiz cuadrada de un
    numero negativo, sin embargo tenermos controlada la excepción

    >>> lista=[]
    >>> for n in [4, 9, -16]:
    ...     lista.append(n)
    >>> raizCuadrada(lista)
    Traceback (most recent call last):
        ...
    ValueError: math domain error
    """
    return [math.sqrt(n) for n in listaNumeros]


# EJECUTAR LAS PRUEBAS
doctest.testmod()
