#!/usr/bin/python

#while
segundos = 5
while segundos > 0 :
    print "La bomba explotara en {} segundo".format(segundos)
    segundos= segundos - 1;
print "BOOOOMMM!!"

numero = 1
while numero <= 10:
    numero = numero + 1
    if numero % 2 != 0:
        continue # if el numero no es par continua con el bucle 
    print numero, "es par"

#FOR
frutero = ["limon", "naranja", "manzana"]
for fruta in frutero:
    print fruta

#for con acumulador
for i in range(10):
    print i,"\n"

for i in range(10,20,2): #saltando en dos en dos en un rango del 10 al 20
    print i


