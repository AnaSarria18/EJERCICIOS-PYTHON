class Persona():
    #constructor
    """_summary_
        Constructor de la clase Persona
    Args:
    identificacion (str): # de docuemento de identificacion
    nombre (str): nombre completo de la persona 
    correo (str): correo electrinico de la persona
    """

    def __init__(self, identificacion: str = "15",
                 nombre: str = "Juan", correo: str = "juan@gmail.com"):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__correo = correo
        
    def getIdentificacion(self) -> str:
        return self.__identificacion
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getCorreo(self) -> str:
        return self.__correo
    
    
    #modificar el atributo con set
    def setIdentificacion(self, nuevoValoridentificacion) -> None:
        self.__identificacion = nuevoValoridentificacion
        
    
    def setNombre(self, nuevoValorNombre) -> None:
        self.__nombre = nuevoValorNombre
        
        
    def setCorreo(self, nuevoValorCorreo) -> None:
        self.__correo = nuevoValorCorreo
        
        
    def saludar(self) -> None:
        print(f"Desde persona. Hola soy un objeto  de tipo {type(self).__name__}")
        
    