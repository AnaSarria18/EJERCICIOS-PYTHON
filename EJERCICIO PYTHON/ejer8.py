#Funciones

def sumar(x,y):
    return x + y

suma = sumar(5,3)
print(suma)

def mostrarDatos(nombre="Maria", apellido="Luna"):
    print(nombre,apellido)
    
mostrarDatos()
mostrarDatos(nombre="Rosa")

mostrarDatos(apellido="Gutierrez")
mostrarDatos(apellido="Perez", nombre="Alejandro")


def obtenerCiudad(ciudad:str)->str:
    return ciudad


ciudad = obtenerCiudad("Medellin")
print(ciudad)

