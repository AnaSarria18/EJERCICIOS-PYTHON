from pez import Pez
from perro import Perro
from gato import Gato


pez = Pez(nombre="Polo", peso=2.0)
perro = Perro(nombre="Manchas", peso=30)
gato = Gato(nombre="Lila", peso=10)


pez.respirar()
pez.nadar()
print(f"El peso del pez {pez.getNombre()} es {pez.getPeso()} kg")


perro.respirar()
perro.ladrar()
print(f"El Peso del perro {perro.getNombre()} es  {perro.getPeso()} kg")


gato.respirar()
gato.maullar()
print(f"El Peso del gato {gato.getNombre()} es  {gato.getPeso()} kg")


#podemos cambiar el peso 
gato.setPeso(45)
print(f"El gato ahora pesa  {gato.getNombre()} : {gato.getPeso()} kg")