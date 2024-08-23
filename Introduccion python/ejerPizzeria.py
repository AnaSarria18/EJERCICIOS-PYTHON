#ejercicio pizzeria

#Lista de pizza vegetariana
vegetariana = ["Pimiento", "Tofu"]
noVegetariana = ["Peperoni", "Jamón", "Salmón"]

opcionPizza = int (input("Tipo de pizza\n1.Vegetariana\n2.No vegetariana\n Seleccione Pizza:"))

if opcionPizza==1:
    print("INGREDIENTE PIZZA VEGETARIANA")
    print("1. ", vegetariana[0])
    print("2. ", vegetariana[1])
    ingrediente = int(input("Seleccione Ingrediente: (1,2):"))
    ingredientesPizza = ["Tomate", "Mozarella", vegetariana[ingrediente-1]]
    
else:
    print("INGREDIENTE PIZZA NO VEGETARIANA")
    print("1. ", noVegetariana[0])
    print("2. ", noVegetariana[1])
    print("3. ", noVegetariana[2])
    ingrediente = int(input("Seleccione Ingrediente: (1,2,3):"))
    ingredientesPizza = ["Tomate", "Mozarella", noVegetariana[ingrediente-1]]
    

print("Ingredientes de la pizza seleccionada\n", ingredientesPizza)
    
    
    