class Empleado():
    
    def __init__(self, nombre:str, cargo:str, sueldo:int) -> None:
        self.__nombre = nombre
        self.__cargo = cargo
        self.__sueldo = sueldo
        
    
    def getNombre(self)->str:
        return self.__nombre
    
    def getCargo(self)->str:
        return self.__cargo
    
    def getSueldo(self)->int:
        return self.__sueldo
    

    def __str__(self) -> str:
        return f"{self.__nombre} con cargo {self.__cargo}"