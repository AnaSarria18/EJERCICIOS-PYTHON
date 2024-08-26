from animal import Animal

class Gato(Animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)  
        

    def maullar(self):
        print(f"{self.getNombre()} esta maullando.")