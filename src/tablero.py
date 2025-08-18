class PosOcupadaException(Exception):
    pass

class PosInvalida(ValueError):
    pass


class Tablero:
    def __init__(self):
        self.contenedor = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""],
        ]
    
    def mostrar_tablero(self):
        print("\n   0   1   2")
        for i, fila in enumerate(self.contenedor):
            print(f"{i}  {fila[0] or ' '} | {fila[1] or ' '} | {fila[2] or ' '}")
            if i < 2:
                print("  -----------")
    

    def poner_ficha(self, fila, columna, ficha):
        
        if not (0 <= fila <= 2) or not (0 <= columna <= 2):
            raise PosInvalida("Posicion no válida")
        
        if self.contenedor[fila][columna] != "":
            raise PosOcupadaException("Posicion ocupada")
        
        self.contenedor[fila][columna] = ficha
