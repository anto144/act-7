from viajero import Viajero
import csv

class ManejadorViajero:
    __listaViajeros = []

    def __init__(self):
        self.__listaViajeros = []
    

    def GenerarLista(self):
        archivo = open("Viajeros.csv")
        reader = csv.reader(archivo, delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera = not bandera
            else:
                numViajero = int(fila[0])
                dni = fila[1]
                nombre = fila[2]
                apellido = fila[3]
                millasAcum = int(fila[4])
                viajero = Viajero(numViajero, dni, nombre, apellido, millasAcum)
                self.__listaViajeros.append(viajero)
        archivo.close()


    def ListarViajeros(self):
        for viajero in self.__listaViajeros:
            print(viajero)
            print("\n".center(20,"-"))


    def buscar(self,NroViaj):
            i = 0
            while(self.__listaViajeros[i].getnumViajero() != NroViaj):
                i += 1
            ViajeroEncontrado= self.__listaViajeros[i]
            print("VIAJERO ENCONTRADO:")
            print(ViajeroEncontrado)
            return ViajeroEncontrado
    
    #opcion1
    def MayorCantidad(self):
        mayor = self.__listaViajeros[0]
        for viajero in self.__listaViajeros:
            if(viajero > mayor):
                mayor = viajero
        return mayor