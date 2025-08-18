from .tateti import Tateti
from .jugador import Jugador

def main():
    print("Bienvenidos al tateti")

    nombre1 = input("Nombre del Jugador X: ")
    nombre2 = input("Nombre del Jugador O: ")

    jugador_x = Jugador(nombre1, "X")
    jugador_o = Jugador(nombre2, "O")
    
    while True:
        juego = Tateti()
        
        while True:
            print("Tablero: ")
            juego.tablero.mostrar_tablero()
            jugador_actual = jugador_x if juego.turno == "X" else jugador_o
            print(f"Turno: {jugador_actual.obtener_info()}")

            while True:
                try:
                    fila = int(input("Ingrese fila (0-2): "))
                    columna = int(input("Ingrese columna (0-2): "))
                    juego.ocupar_casilla(fila, columna)
                    break
                except ValueError:
                    print("Ingrese números válidos entre 0 y 2")
                except Exception as e:
                    print(f"Error: {e}")
            
            ganador = juego.verificar_ganador()
            if ganador:
                juego.tablero.mostrar_tablero()
                jugador_ganador = jugador_x if ganador == "X" else jugador_o
                print(f"Ganó {jugador_ganador.nombre}!")
                break
            
            if juego.verificar_empate():
                juego.tablero.mostrar_tablero()
                print("Empate")
                break
        
        while True:
            respuesta = input("\n Jugar otra vez? (s/n): ").lower()
            if respuesta in ['s', 'si', 'sí']:
                break
            elif respuesta in ['n', 'no']:
                return
            else:
                print("Responda 's' para sí o 'n' para no")

if __name__ == '__main__':
    main()
