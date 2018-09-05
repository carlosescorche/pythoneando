#!/usr/bin/env python3

# ex19: Functions and Variables


def imp(n):
    a,b = 0,1
    while a <= n:
        print(a,end=" ")
        a,b = b,a+b

i = imp
print(i)
i(2000)


# valores por omision

i = 5
def f(arg=i):
    print(arg)

i = 6
f() #>> 5

def f(a,l=[]):
    l.append(a)
    return l

print('-'*10)
print(f(10))
print(f(20))  


def animal(nombre, peso, color = 'negro', pies = 2): 
    print("El animal %s pesa %d kg es de color %s y tiene %s pies" % (nombre, peso,color,pies))

print('-'*10)
animal('perro',10,pies=4,color='blanco')
animal('gorilla',50,pies=2)


def ventadequeso(tipo,*args,**dics):
    print("queso tipo: {tipo}".format(tipo = tipo))
    
    for a in args:
        print(a)

    for i,v in dics.items():
        print(i," : ", v)

print('-'*10)
ventadequeso('mantecoso',"es sabroso","pero tiene mucha grasa",cliente="lider",venderdor='jose')
print('-'*10)
ventadequeso('gauda',cliente="totus",venderdor='jose')

m = list(map(lambda x,y : x + y, [2,4,6],[8,10,12]))

print('-'*10)
print(m)

m = list(map(lambda x : x['name'] == "carlos", [{'name' : 'carlos'},{'name' : 'liyoamny'}]))

print('-'*10)
print(m)

