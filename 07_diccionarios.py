#!/usr/bin/python
#coding=utf-8

# Los diccionarios son matrices asociativas, lo que viene a ser 
# en PHP los arrays asociativos por clave y valor que tanto me gustan
# En los diccionarios se accede al valor a traves de la clave
# A diferencia de las listas y tuplas son colecciones desordenadas

materias = {}

#asignaciones
materias['lunes'] = ['ingles','matematicas']
materias['martes'] = ['progracion','logíca']
materias['miercoles'] = ['diseno UI','algoritmo']
materias['jueves'] = ['diseno UX']
materias['viernes'] = ' libre'

print materias

#obtiene el valor de la clave
print materias.get('lunes')

#comprobación - verifica si existe la clave
print "es falso", materias.has_key('marte')
print "es verdadero", materias.has_key('martes')

#mostrar claves
print materias.keys()

#mostrar valores 
print materias.values()

#eliminar
del(materias['viernes'])
print materias

#pop
print materias.pop('lunes')
print materias

#items - muestra tuplas con clave, valor
print materias.items()



