#hacer un programa que permita crear una lista de palabras y que , a continuacion, pida una palabra y diga cuantas veces aparece esa palabra en la lista 

palabras = []

for i in range(10):
    palabra = input("Ingrese una palabra:")
    palabras.append(palabra)
    
palabraAbuscar = input("Ingrese palabra a buscar:")

#solucion 1 version corta

cantidad = palabras.count(palabraAbuscar)
print(f"La palabra {palabraAbuscar} se encuentra {cantidad} en la lista \n {palabras}")


#solucion 2 version larga 

contador = 0
for palabra in palabras:
    if palabra == palabraAbuscar:
        contador += 1
print(f"La palabra {palabraAbuscar} se encuentra {contador} en la lista \n {palabras}")