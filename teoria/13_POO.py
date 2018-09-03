#!/usr/bin/python
#coding=utf-8

#tipica clase productos
class Producto():

    codigo = 1020 # atributos hacen referencia a las variables internas de la clase
    nombre = ''
    descripcion = ''
    pvp = ''

    #Constructor Se llama automáticamente al crear una instancia de clase.
    #Self sirve para hacer referencia a los métodos y atributos base de una clase dentro de sus propios métodos.
    def __init__(self,codigo,nombre):
        self.codigo = codigo
        self.nombre = nombre
        print("producto creado")

    # Metodos Hacen referencia a las funciones internas de la clase.
    def guardar(self):
        print('producto guardado')
    
    def eliminar(self):
        pass

    def modificar(self):
        pass
    
    #encapsulamiento
    #Consiste en denegar el acceso a los atributos y métodos internos de la clase desde el exterior
    #En Python no existe, pero se puede simular precediendo atributos y métodos con dos barras bajas __:

    # __atributo_privado = valor

    def __metodo_privado(self):
        print("Soy un método inalcanzable desde fuera")

    #metodos especiales 

    # Destructor de clase (al borrar la instancia)
    def __del__(self):
        print("El producto codigo", self.codigo, "fue eliminado")
    
    #Para devolver una cadena por defecto al convertir un objeto a una cadena con str(objeto)
    def __str__(self):
        return "Mostrando detalles del producto codigo {} nombre {}".format(self.codigo,self.nombre)

    #Para devolver un número que simula la longitud del objeto len(objeto)
    def __len__(self):
        return self.codigo


p = Producto(1020,'test')

print(str(p))
print(len(p))

#herencia
class Libro(Producto): #heredando de la clase de productos
    pass



Libro(1023,'libro').guardar()





    
