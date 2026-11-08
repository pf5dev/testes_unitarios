import unittest
from escolar import avaliar_notas
import os

os.system('cls')

class TestEscolar(unittest.TestCase):
    def test_n1_numero_extremo(self):
        self.assertRaises(ValueError,avaliar_notas,-1,0,0,0,)
    
    def test_n2_numero_extremo(self):
        self.assertRaises(ValueError,avaliar_notas,0,-1,0,0)
    
    def test_n3_numero_extremo(self):
        self.assertRaises(ValueError,avaliar_notas,0,0,-1,0)
    
    def test_saida_A1(self):
        self.assertEqual(avaliar_notas(10,10,10,10),'A')

    def test_saida_A2(self):
        self.assertEqual(avaliar_notas(9,9,9,9),'A')

    def test_saida_B1(self):
        self.assertEqual(avaliar_notas(8.9,8.9,8.9,8.9),'B')

    def test_saida_B2(self):
        self.assertEqual(avaliar_notas(7.5,7.5,7.5,7.5),'B')
    
    def test_saida_C1(self):
        self.assertEqual(avaliar_notas(7.4,7.4,7.4,7.4),'C')

    def test_saida_C2(self):
        self.assertEqual(avaliar_notas(6.0,6.0,6.0,6.0),'C')

    def test_saida_D1(self):
        self.assertEqual(avaliar_notas(5.9,5.9,5.9,5.9),'D')

    def test_saida_D2(self):
        self.assertEqual(avaliar_notas(0.0,0.0,0.0,0.0),'D')

if __name__ == '__main__':
    unittest.main()
