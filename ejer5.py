#estructuras repetitivas

for i in range(10):
    print(i)
    
for i in range(1,11):
    print(i)
    
for i in range(1, 11, 2):
    print(i)
    
for i in range(3):
    for j in range(3):
        print(i, j)


ciudades = ["Cali", "Ppopayan", "Neiva", "Quilla"]

for ciudad in ciudades:
    print(ciudad)
    longitudCiudad = len(ciudad)
    print(f"Longitud: {longitudCiudad}")
    
    
for i in range(len(ciudades)):
    print(ciudades[i])

posNeiva = ciudades.index("Neiva")
print(posNeiva)



# while
i = 0
while (i < 10):
    print(i)
    i += 1
else:
    print("no ingrese")
    
    
    
while(True):
    print("hola")
    x = 5
    if x == 5:
        break
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    