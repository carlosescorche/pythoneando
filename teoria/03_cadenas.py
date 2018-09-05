#!/usr/bin/python
#coding=utf-8

# cadenas normales
c = 'áèïóù'
print("áèïóù" , type(c))
# cadenas unicode
c = u'áèïóù'
print("u'áèïóù'" , type(c))
# cadenas raw
r = r"\n"
print("r\"\\n\"= " + r)

#Cadenas con varias lineas
cadena = """
            Esto es una cadena
            De varias lineas
        """
print(cadena, end=" ")

#Concatenar
h = "hola"
m = "mundo"
hm = h + m
hh = h * 2

print(hm)
print(hh)

#obtener el largo
print(len(h))

#segmentar
print(hm[:4])
print(hm[:])
print(hm[4:])

#las cadenas son inmutables
#h[2] = "c"
print(h)

#recorrer cadena
for letra in hm:
    print(letra)

#buscar
print("o" in hm)


