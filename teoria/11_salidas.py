#!/usr/bin/python
#coding=utf-8

#La función print() es la forma general de mostrar información por pantalla. 
#Generalmente podemos mostrar texto y variables separándolos con comas

h = "hola"
m = "mundo"
n = 10
p = "primer texto de salida", h, m, " con un número", n
print(p)

#Es una funcionalidad de las cadenas de texto que nos permite formatear 
#información en una cadena (variables o valores literales) cómodamente utilizando identificadores referenciados

p = "Un texto '{}' y número '{}'".format(h,n)
print(p)

#podemos referenciar a partir de la posición de los valores utilizando índices
p = "Un texto '{1}' y un número '{0}'".format(n,h)
print(p)

#podemos utilizar identificador con una clave y luego pasarlas en el format
p = "un texto '{h}' y un número '{n}'".format(n=n,h=h)
print(p)

#Alineamiento a la derecha en 30 caracteres
print( "{:>30}".format("palabra") )

#Alineamiento a la izquierda en 30 caracteres
print( "{:30}".format("palabra") )

#Truncamiento a 3 caracteres
print( "{:.5}".format("palabra") )

#Formateo de números enteros, rellenados con espacios
print("{:4d}".format(10))
print("{:4d}".format(100))
print("{:4d}".format(1000))

#Formateo de números enteros, rellenados con ceros
print("{:04d}".format(10))
print("{:04d}".format(100))
print("{:04d}".format(1000))

#Formateo de números flotantes, rellenados con espacios
print("{:7.3f}".format(3.1415926))
print("{:7.3f}".format(153.21))

#Formateo de números flotantes, rellenados con ceros
print("{:07.3f}".format(3.1415926))
print("{:07.3f}".format(153.21))

