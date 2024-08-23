#hacer un programa en python que implemente una fucnion que reciba como parametro una lista 
#con numero enteros y como resultado debe devolver la suma de los numeros

def sumaLista(listaNumeros):
    suma=0
    for numero in listaNumeros:
        suma += numero
    return suma


numeros = [2,5,8,4,7,9]

sumaNumeros = sumaLista(numeros)

print(sumaNumeros)


