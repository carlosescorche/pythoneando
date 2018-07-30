#!/usr/bin/python
#coding=utf-8

#Excepciones
#Son bloques de código excepcionales que nos permiten continuar con la 
#ejecución de un programa pese a que ocurra un error.

#Para prevenir el error, debemos poner el código propenso a error un bloque 
#try y l1uego encadenaremos un bloque except para tratar la excepción
try:
    n = float(input("Introduce un número: "))
    m = 4
    print("{}/{}={}".format(n,m,n/m))
except:
    print("Ha ocurrido un error, introduce bien el número")