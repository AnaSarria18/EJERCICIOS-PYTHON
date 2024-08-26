from animal import Animal

class Perro(Animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)  
        
        
    def ladrar(self):
        print(f"{self.getNombre()} esta ladrando.")