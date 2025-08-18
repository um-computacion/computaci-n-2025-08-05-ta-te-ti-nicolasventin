import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.tateti import Tateti
from src.tablero import Tablero, PosOcupadaException, PosInvalida
from src.jugador import Jugador

class TestTablero(unittest.TestCase):
    
    def test_poner_ficha_valida(self):
        tablero = Tablero()
        tablero.poner_ficha(0, 0, "X")
        self.assertEqual(tablero.contenedor[0][0], "X")
    
    def test_posicion_ocupada(self):
        tablero = Tablero()
        tablero.poner_ficha(1, 1, "X")
        with self.assertRaises(PosOcupadaException):
            tablero.poner_ficha(1, 1, "O")
    
    def test_posicion_invalida(self):
        tablero = Tablero()
        with self.assertRaises(PosInvalida):
            tablero.poner_ficha(3, 0, "X")

class TestJugador(unittest.TestCase):
    
    def test_crear_jugador(self):
        jugador = Jugador("Diego", "X")
        self.assertEqual(jugador.nombre, "Diego")
        self.assertEqual(jugador.ficha, "X")
    
    def test_obtener_info(self):
        jugador = Jugador("Camila", "O")
        resultado = jugador.obtener_info()
        self.assertEqual(resultado, "Camila (O)")

class TestTateti(unittest.TestCase):
    
    def test_turno_inicial(self):
        tateti = Tateti()
        self.assertEqual(tateti.turno, "X")
    
    def test_ocupar_casilla_cambia_turno(self):
        tateti = Tateti()
        tateti.ocupar_casilla(0, 0)
        self.assertEqual(tateti.turno, "O")
    
    def test_victoria_fila(self):
        tateti = Tateti()
        tateti.tablero.contenedor[0] = ["X", "X", "X"]
        ganador = tateti.verificar_ganador()
        self.assertEqual(ganador, "X")
    
    def test_victoria_columna(self):
        tateti = Tateti()
        tateti.tablero.contenedor[0][0] = "O"
        tateti.tablero.contenedor[1][0] = "O"
        tateti.tablero.contenedor[2][0] = "O"
        ganador = tateti.verificar_ganador()
        self.assertEqual(ganador, "O")
    
    def test_empate(self):
        tateti = Tateti()
        tateti.tablero.contenedor = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["O", "X", "O"]
        ]
        self.assertTrue(tateti.verificar_empate())

if __name__ == '__main__':
    unittest.main()
