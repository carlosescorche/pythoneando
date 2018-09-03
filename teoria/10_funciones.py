#!/usr/bin/python

def operaciones(num1,num2):
    print("Serie de operaciones para los numeros", num1, "y", num2)
    print(num1 , " + ", num2 , " = ", num1+num2)
    print(num1 , " - ", num2 , " = ", num1-num2)   
    print(num1 , " * ", num2 , " = ", num1*num2)

    # "and" es un operador logico que indica una comparacion Y
    # tambien existe el "or" que es un O y el "not" para negar
    # aqui comprobamos que ninguno de los dos numeros sea un cero
    # ya que eso haria una division que daria error

    if num1 != 0 and num2 != 0:
        print(num1 , " / ", num2 , " = ", float(num1)/float(num2))  

operaciones(100,5)
operaciones(num2=5,num1=100) #no importa el orden siempre y cuando indentifiques el valor con el nombre de variable

#Valores por defectos
def numeroYcolor(numero=5,color="rojo"):
    print("Numero ", numero , " y color ", color)

numeroYcolor() #valores por defectos
numeroYcolor(10) #afecta el primer argumento
numeroYcolor(color="azul") #afecta el segundo argumento
numeroYcolor(7,"verde")

#funciones con paramentos indefinidos
def recibe_tuplas(*args):
    print(args)

recibe_tuplas("carlos","escorche")

def recibe_diccionario(**args):
    print(args)
 
recibe_diccionario(nombre="carlos",apellido="escorche")

#devolviendo paramentos indefinidos
def devuelve_tuplas():
    return "carlos","escorche",26

print(devuelve_tuplas()) #imprime tupla

(nombre,apellido,edad) =  devuelve_tuplas() #asigna los valores a una lista de variables

print(nombre,apellido,edad)