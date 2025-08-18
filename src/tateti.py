from .tablero import Tablero

class Tateti:
    def __init__(self):
        self.turno = "X"
        self.tablero = Tablero()
    
    def ocupar_casilla(self, fila, columna):
        self.tablero.poner_ficha(fila, columna, self.turno)
        self.cambiar_turno()
    
    def cambiar_turno(self):
        if self.turno == "X":
            self.turno = "O"
        else:
            self.turno = "X"
    
    def verificar_ganador(self):
        for fila in self.tablero.contenedor:
            if fila[0] == fila[1] == fila[2] != "":
                return fila[0]
            
        for col in range(3):
            if (self.tablero.contenedor[0][col] == self.tablero.contenedor[1][col] == self.tablero.contenedor[2][col] != ""):
                return self.tablero.contenedor[0][col]
            
        if (self.tablero.contenedor[0][0] == self.tablero.contenedor[1][1] == self.tablero.contenedor[2][2] != ""):
            return self.tablero.contenedor[0][0]
        
        if (self.tablero.contenedor[0][2] == self.tablero.contenedor[1][1] == self.tablero.contenedor[2][0] != ""):
            return self.tablero.contenedor[0][2]
        
        return None

    def verificar_empate(self):
        if self.verificar_ganador():
            return False
            
        for fila in self.tablero.contenedor:
            for casilla in fila:
                if casilla == "":
                    return False
        
        return True