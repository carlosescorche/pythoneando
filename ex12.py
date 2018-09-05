#!/usr/bin/env python3

#nombre.capitalize()
#nombre.upper()
#nombre.title()
#nombre.lower()

while True:
    try:
        print("Escribe tu nombre de usuario")
        nombre = input(">")

        if not(len(nombre) > 6 and len(nombre) < 12):
            print('El nombre debe tener entre 6 a 12 caracteres')
        elif not nombre.isalnum():
            print('El nombre debe ser alfanumerico')
        else:
            break
    except:
        print("Problema con el nombre ingresado")



