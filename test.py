
import unittest
from bubblesort import BubbleSort

class TestBubbleSort(unittest.TestCase):

    def setUp(self):
        self.ordenador = BubbleSort()
    # CP1: 1-2-8
    def test_cp1(self):
        # Arrange
        valores = [5]
        esperado = [5]
        # Act
        resultado = self.ordenador.bubbleSort(valores)
        # Assert (Verify)
        self.assertEqual(esperado, resultado)

    def test_cp3(self):
        valores = [1, 2]
        esperado = [1, 2]
        resultado = self.ordenador.bubbleSort(valores)
        self.assertEqual(esperado, resultado)

    def test_cp4(self):
        valores = [2, 1]
        esperado = [1, 2]
        resultado = self.ordenador.bubbleSort(valores)
        self.assertEqual(esperado, resultado)

if __name__ == "__main__":
    unittest.main()

