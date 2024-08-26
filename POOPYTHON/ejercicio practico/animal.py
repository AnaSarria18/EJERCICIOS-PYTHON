class Animal():
    
    def __init__(self,nombre, peso) -> None:
        self.__nombre = nombre
        self.__peso = peso
        
    def respirar(self):
        print(f"{self.__nombre} esta Respirando")
        
    
    def getPeso(self):
        return self.__peso
    
    def setPeso(self, peso):
        self.__peso = peso
        
    def getNombre(self):
        return self.__nombre