#!/usr/bin/python

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