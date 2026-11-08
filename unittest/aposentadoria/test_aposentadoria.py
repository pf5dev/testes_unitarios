import unittest
from aposentadoria import verificar_qualificacao_empregado, REQUERER,NAO_REQUERER
import os

os.system('cls')

class TesteVerificarQualificacaoEempregado(unittest.TestCase):
    def test_typeerror_idade(self):
        self.assertRaises(TypeError,verificar_qualificacao_empregado,'65',30)
    def test_typeerror_tempo_de_servico(self):
        self.assertRaises(TypeError,verificar_qualificacao_empregado,65,'30')
    def test_valueerror_idade(self):
        self.assertRaises(ValueError,verificar_qualificacao_empregado,0,10)
    def test_valueerror_tempo_de_servico(self):
        self.assertRaises(ValueError,verificar_qualificacao_empregado,20,0)
    def test_requerer_aposentadoria_condicao1(self):
        self.assertEqual(verificar_qualificacao_empregado(65,20),REQUERER)
    def test_requerer_aposentadoria_condicao2(self):
        self.assertEqual(verificar_qualificacao_empregado(59,30),REQUERER)
    def test_requerer_aposentadoria_condicao3(self):
        self.assertEqual(verificar_qualificacao_empregado(60,25),REQUERER)
    def test_requerer_aposentadoria_condicao4(self):
        self.assertEqual(verificar_qualificacao_empregado(59,24),NAO_REQUERER)

if __name__ == '__main__':
    unittest.main()
    
