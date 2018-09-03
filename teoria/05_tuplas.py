#!/usr/bin/python

# Las tuplas son colecciones mas ligeras que las listas,
# una vez creadas son inmutables y su tamano no puede variar.
# Su constructor es la coma, pero se aconseja enumerarlas entre parentesis

tupla = True,10,"hola",[1,23] #puede contener cualquier valor
print(tupla, type(tupla))

#Covertir lista en tupla
tupla = tuple([1,2,3,4,5,6,7,8,9,10])
print(tupla)

#segmentar tuplas
print(tupla[:3])
print(tupla[1:4])
print(tupla[-1])

#(inicio:fin:salto) cada cuanto seleccionar el elemento
print(tupla[1:20:2])
print(tupla[::2])

#busqueda
print(tupla.count(20))
print(tupla.index(3))
print(5 in tupla)
#contar 
print(len(tupla))

#recorrer
for i in tupla:
    pass
    #print i

