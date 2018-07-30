#!/usr/bin/python
#coding=utf-8

#Utilizando un while(true), podemos asegurárnos de que el usuario introduce bien el valor
#Repitiendo la lectura por teclado hasta que lo haga bien, y entonces rompemos el bucle con un break:
while True:
    try:
        n = float(input("Introduce un número: "))
        m = 4
        print("{}/{}={}".format(n,m,n/m))
        break
    except:
        print("Ha ocurrido un error, introduce bien el número")