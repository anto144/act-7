class Viajero:
    __numViajero = 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millasAcum = 0

    def __init__(self, numViajero, dni, nombre, apellido, millasAcum):
        self.__numViajero = numViajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum
    
    def __str__(self):
        return "Numero de viajero: {}\nDNI: {}\nNombre: {}\nApellido: {}\nMillas acumuladas: {}".format(self.__numViajero, self.__dni, self.__nombre, self.__apellido, self.__millasAcum)
    
    def getnumViajero(self):
        return self.__numViajero

    def getdni(self):
        return self.__dni
    
    def getnombre(self):
        return self.__nombre
    
    def getapellido(self):
        return self.__apellido

    def cantidadMillas(self):
        return self.__millasAcum
    
    def __gt__(self, otro):
        if(type(self) == type(otro)):
            return (self.__millasAcum > otro.__millasAcum)
    
    def __add__(self, millas):
        return Viajero(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcum + millas)
    
    def __sub__(self, millas):
        return Viajero(self.__numViajero,self.__dni,self.__nombre,self.__apellido,self.__millasAcum - millas)
    #nuevo
    def __eq__(self, millas):
        return (self.cantidadMillas() == millas)
    
    def __radd__(self, millas):
        return self + millas
    
    def __rsub__(self, millas):
        return self - millas