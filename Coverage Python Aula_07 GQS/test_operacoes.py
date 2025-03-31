# test_operacoes.py
import unittest
from Aula_04 import soma, subtracao, divisao, multiplicacao  # Supondo que suas funções estão no arquivo "main.py"

class TestOperacoesMatematicas(unittest.TestCase):
    def test_soma(self):
        self.assertEqual(soma(2, 3), 5)
        self.assertEqual(soma(-1, 1), 0)

    def test_subtracao(self):
        self.assertEqual(subtracao(2, 1), 1)
        self.assertEqual(subtracao(0, 5), -5)

    def test_multiplicacao(self):
        self.assertEqual(multiplicacao(3, 3), 9)
        self.assertEqual(multiplicacao(-2, 3), -6)

    def test_divisao(self):
        self.assertEqual(divisao(10, 2), 5)
        with self.assertRaises(ValueError):
            divisao(10, 0)

if __name__ == '__main__':
    unittest.main()
