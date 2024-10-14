import unittest
from src.OperacionesEntero import OperacionesEnteros
class TestOperacionesEntero(unittest.TestCase):
    def setUp(self):
        self.operaciones = OperacionesEnteros( )

    def tearDown(self):
        self.operaciones = None

    def test_MCD(self):
        # Arrange
        numero1 = 100
        numero2 = 25
        resultadoEsperado = 25

        # Do
        resultadoActual = self.operaciones.MCD(numero1,numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM(self):
        # Arrange
        numero1 = 4
        numero2 = 5
        resultadoEsperado = 20

        # Do
        resultadoActual = self.operaciones.MCM(numero1, numero2)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

    def test_MCM_de_tres(self):
        # Arrange
        numero1 = 4
        numero2 = 5
        numero3 = 6
        resultadoEsperado = 60

        # Do
        resultadoActual = self.operaciones.MCM_de_tres(numero1, numero2, numero3)

        # Assert
        self.assertEqual(resultadoEsperado, resultadoActual)

        def test_MCM_de_cuatro(self):
            # Arrange
            numero1 = 4
            numero2 = 5
            numero3 = 6
            numero4 = 7
            resultadoEsperado = 420

            # Do
            resultadoActual = self.operaciones.MCM_de_cuatro(numero1, numero2, numero3, numero4)

            # Assert
            self.assertEqual(resultadoEsperado, resultadoActual)

        if __name__ == '__main__':
            unittest.main()