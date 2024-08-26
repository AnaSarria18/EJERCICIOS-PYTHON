from animal import Animal

class Pez(Animal):
    def __init__(self, nombre, peso):
        super().__init__(nombre, peso)  
        
        
    def nadar(self):
        print(f"{self.getNombre()} esta nadando.")