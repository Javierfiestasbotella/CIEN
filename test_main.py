import unittest
import pygame
from unittest.mock import patch
from main import Jugador, tirar_dado, triple_dado, mostrar_info_jugador, actualizar_tirada
from unittest.mock import patch, MagicMock  # Agregar MagicMock aquí

class TestMain(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pygame.init()  # Inicializar Pygame

    @classmethod
    def tearDownClass(cls):
        pygame.quit()  # Cerrar Pygame después de que se hayan ejecutado todas las pruebas

    def test_triple_dado(self):
        # Prueba para asegurar que la función triple_dado() genera una lista de tres valores entre 1 y 6
        tirada = triple_dado()
        self.assertEqual(len(tirada), 3)  # Verificar que la tirada contiene tres valores
        for valor in tirada:
            self.assertTrue(1 <= valor <= 6)  # Verificar que cada valor está entre 1 y 6

    def test_tirar_dado(self):
        # Prueba para asegurar que la función tirar_dado() suma correctamente los puntos y los almacena en el jugador
        jugador = Jugador("TestPlayer")
        puntos = tirar_dado(jugador)
        self.assertEqual(jugador.puntos, puntos)  # Verificar que los puntos se sumaron correctamente al jugador
        self.assertTrue(0 <= jugador.puntos <= 18)  # Verificar que la suma de puntos está en el rango esperado
        # Prueba con un jugador que ya tiene puntos acumulados
        jugador.puntos = 10
        puntos = tirar_dado(jugador)
        self.assertEqual(jugador.puntos, 10 + puntos)  # Verificar que los puntos se sumaron correctamente al jugador
        self.assertTrue(10 <= jugador.puntos <= 28)  # Verificar que la suma de puntos está en el rango esperado
    
    def test_mostrar_info_jugador(self):
        # Prueba para asegurar que la función mostrar_info_jugador() muestra la información del jugador correctamente
        jugador = Jugador("TestPlayer")
        ventana_mock = MagicMock()  # Mock para simular la ventana de juego
        mostrar_info_jugador(jugador, 100, 100)  # Llamar a la función
        # Verificar que se llamó a la función para dibujar texto en la ventana con la información del jugador
        ventana_mock.blit.assert_called()

    def test_actualizar_tirada(self):
        # Prueba para asegurar que la función actualizar_tirada() actualiza la tirada del jugador en la pantalla correctamente
        jugador = Jugador("TestPlayer")
        ventana_mock = MagicMock()  # Mock para simular la ventana de juego
        actualizar_tirada(jugador)  # Llamar a la función
        # Verificar que se llamó a la función para dibujar la tirada del jugador en la ventana
        ventana_mock.blit.assert_called()
if __name__ == '__main__':
    unittest.main()

