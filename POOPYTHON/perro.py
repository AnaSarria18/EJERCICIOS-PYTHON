class Perro():
    #constructor
    def __init__(self, nombre, raza):
        self.nombre = nombre
        self.raza = raza
    #metodos
    def ladrar(self):
        print("Guauuu")
    
    def caminar(self, pasos):
        print(f" {self.nombre} esta caminando {pasos} pasos")
        
    
    