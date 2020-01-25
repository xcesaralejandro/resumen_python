# 1 - CREAR LISTAS

# Crear lista vacia
mylist = []
# Crear lista con datos iniciales
mylist = ['item 0','item 1','item 2']




# 2 - ACCEDER A ELEMENTOS

# Mediante su indice
# consideración: los indices comienzan en 0
mylist[1]
# Desde el ultimo elemento
# consideración: los indices comienzan en -1 y no 0, -1 = al ultimo elemento
mylist[-1]
# Buscar un indice por elemento
# consideración: Si hay más de un elemento con el mismo valor, retornará solo el indice del primero
mylist.index('item 1')




# 3 - PORCIONES DE LISTAS

# Desde el primer indice hasta uno especifico
mylist[:2]
# Desde un indice especifico hasta el ultimo
mylist[2:]
# Toda la lista
mylist[:] 




# 4 - AGREGAR ELEMENTOS

# Añadir un elemento al final
mylist.append('add at the end')
# Añadir un elemento entremedio de la lista
posicion = 1
mylist.insert(posicion, 'new element position 1')
# Concatenar varios elementos al final de una lista
newlist = ['new list 1','new list 2','new list 3']
mylist.extend(newlist)




# 5 - ELIMINAR ELEMENTOS

# consideración: Si hay más de un elemento igual, solo eliminará el primero
element = "new list 3"
mylist.remove(element)
# eliminar el ultimo elemento
mylist.pop()
# eliminar un elemento en un indice especifico
indice = 1
mylist.pop(indice)




# 6 - COMPROBACIONES

# Ver si un elemento se encuentra en una lista  
element = "new list 1"
element in  mylist




# 7 - OTROS

# Comprobar el tipo de la variable
type(mylist)
# Concatenar lista
list2018 = ['jun18', 'jul18']
list2019 = ['jun19', 'jul19']
allyears = list2018 + list2019
#repetir una lista
allyears * 3