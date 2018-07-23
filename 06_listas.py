#!/usr/bin/python
#coding=utf-8
# Son los arrays o vectores de Python y son muy flexibles
# Pueden contenter cualquier tipo de dato, incluso otras listas

lista = [2, 0x13, False, "Una cadena de texto", [1, 7.0]]

print lista[0], type(lista[0])
print lista[3], type(lista[3])
print lista[4], type(lista[4])

#elemento de una lista mutidimensional
print lista[4][1], type(lista[4][1])

#las lista no son inmutables
lista[1] = 10
print lista

#accediendo al ultimo elemento
print lista[-1]

#slicing 
print(lista[:3])
print(lista[1:-1])
print(lista[::2]) #slicing con saltos

#inserciones
lista.append('será eliminado luego') #agregar el valor en la ultima posición
print lista

lista.insert(1,200) #inserta el elemento segun el index que indiques
print lista

#eliminar
lista.remove(200)
print lista

#eliminar el ultimo elemento
lista.pop()
print lista

#buscar
print 200 in lista
print 2 in lista

#buscar index
print lista.index(2)

#cantidad de elementos
print len(lista)

#elemento minimo
print min(lista)

#elemento maximo
print max(lista)



