import unittest
import calculadora

class TestCalc(unittest.TestCase):

    def test_adicao(self):
        resultado = calculadora.adicao(2, 3)
        self.assertEqual(resultado, 5)

    def test_subtracao(self):
        resultado = calculadora.subtracao(2, 3)
        self.assertEqual(resultado, -1)
    
    def test_multplicacao(self):
        resultado = calculadora.multiplicacao(2, 3)
        self.assertEqual(resultado, 6)

    def test_divisao(self):
        resultado = calculadora.divisao(6, 3)
        self.assertEqual(resultado, 2)

        with self.assertRaises(ValueError):
            calculadora.divisao(10, 0)

if __name__ == '__main__':
    unittest.main()