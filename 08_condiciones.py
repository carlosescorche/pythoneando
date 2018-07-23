#!/usr/bin/python
#coding=utf-8

#IF
nota = 10
if nota == 10 :
    print('has sacado un 10')
    print('puntuación perfecta')

#IF-ELSE
nota = 7
if nota >= 5:
    print("Felicidades has aprobado con un {}".format(nota))
else:
    print("Has reprobado con un {}".format(nota))

#IF-ELIF-ELSE
nota = 4
if nota > 9 :
    print("Has sacado un sobresaliente")
    print("Buen trabajo")
elif nota >= 5 :
    print("Has sacado un" , nota)
    print("Podrias haberlo hecho mejor")
else:
    print("Has sacado un" , nota)
    print("Menudo desastre")

#asignando valor condicionado
valor = "aprobado" if nota >= 5 else "reprobado"
print valor