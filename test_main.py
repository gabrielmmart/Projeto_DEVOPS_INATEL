import unittest
from unittest.mock import patch
import HtmlTestRunner
import supermercadoMain

class TesteSupermercado(unittest.TestCase):

    def setUp(self):
        self.supermercado = supermercadoMain.Supermercado() 
        self.dono = supermercadoMain.DonoSupermercado(self.supermercado)
        self.func_1 = supermercadoMain.Funcionario('Gabriel', 'Medeiros', 50000)
        self.emp_2 = supermercadoMain.Funcionario('Ramon', 'Adonis', 60000)

    def test_carrinhoVazio(self):
        c1 = supermercadoMain.Carrinho()
        self.assertFalse(c1.itens)

    def test_produtosExistem(self):
        self.assertTrue(self.supermercado.produtos)

    def test_comprar1Banana(self):
        self.supermercado.comprar_item(1,1)
        self.assertTrue(self.supermercado.carrinho.itens)
        self.assertEqual(self.supermercado.carrinho.calcular_total(), 0.5)

    def test_comprarDemaisDeUmProduto(self):
        self.supermercado.comprar_item(1,9999)
        self.assertEqual(self.supermercado.carrinho.calcular_total(), 0)

    def test_comprar2ProdutosDiferentes(self):
        self.supermercado.comprar_item(1,1)
        self.supermercado.comprar_item(2,5)
        self.assertIsNotNone(self.supermercado.carrinho.itens[1])


    def test_removendoItem(self):
        self.supermercado.comprar_item(1,1)
        self.supermercado.remover_do_carrinho(1)
        self.assertEqual(self.supermercado.carrinho.calcular_total(), 0.0)

    def test_removendoComCarrinhoVazio(self):
        with self.assertRaises(IndexError):
            self.supermercado.remover_do_carrinho(1)

    def test_donoColocaNovoItem(self):
        self.dono.add_produto('Macarrao',2,50)
        self.assertIsNotNone(self.supermercado.produtos[3])

    def test_donoRemoveItem(self):
        self.dono.remover_produto(2)
        self.assertEqual(len(self.supermercado.produtos), 2)

    def test_donoAlteraPreco(self):
        self.dono.update_produto_preco(1,1)
        self.supermercado.comprar_item(1,1)
        self.assertEqual(self.supermercado.carrinho.calcular_total(), 1)

    def test_monthly_schedule(self):

        self.func_1 = Funcionario('Gabriel', 'Medeiros', 50000)
        self.func_2 = Funcionario('Ramon', 'Adonis', 60000)

        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.func_1.horario_funcionario('Maio')
            mocked_get.assert_called_with('http://company.com/Medeiros/Maio')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.func_1.horario_funcionario('Junho')
            mocked_get.assert_called_with('http://company.com/Adonis/Junho')
            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Artefatos'))
    