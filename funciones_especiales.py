import copy
# FUNCIONES LAMBDA
print("LAMBDA\n---------------")
# OBS: Se utilizan para calculos sencillos, no permiten bucles. El :, vendria siendo como
#      un return
area_triangulo = lambda base, altura : (base * altura) / 2
print(area_triangulo(10,5))




# FILTER
print("\n\nFILTER\n---------------")
# Permite filtrar de una lista o tupla. La función recibe 2 argumenos, la función que se aplicará
# y el listado de numeros.
numbers = (2,3,4,5,6,7,8,9,10)
filtered = filter(lambda value:value%2==0, numbers)
# filtered nos devolverá un iterador, lo parseamos a lista para poder verlo en el print
print(list(filtered))




# MAP
print("\n\nMAP\n---------------")
# Aplica una función a los valores de un iterador y retorna una lista con los valores modificados.
# OBS: Recordemos que en python todo se pasa por referencia así que se modificará el objeto original
#      al utilizar map, recuerda crear una copia del objeto si no deseas que eso suceda.
 
def add_iva(product):
    iva = product['price'] * 0.19
    product['price'] = int(product['price'] + iva)
    return product

products = [{"name" : "Mouse", "price" : 10000}, {"name" : "Mousepad", "price" : 5000}]
products_with_iva = map(add_iva, copy.deepcopy(products))
print(list(products_with_iva))
print(list(products))



