#Hacer un programa que lea un numero entero y como resultado mostrar su 
# correspondiente en notacion binaria


numero = int(input("Ingrese numero entero para obtener su binario:"))

binario = ""
numeroIngresado=numero

while(True):
    resultado = numero //2
    residuo = numero % 2
    binario = str(residuo) + binario 
    if(resultado==1):
        binario = str(resultado)  + binario 
        break
    numero = resultado
    

print("Binario resultante:", binario)
#print(binario[::-1])

#solucion dura que es donde se concatena a lo ultimo 
#for i in range(len(binario)-1 , -1 , -1):
    #print(binario[i], end="")


