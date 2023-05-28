import unittest
import HtmlTestRunner
import supermercadoMain

class TesteSupermercado(unittest.TestCase):

    def setUp(self):
        self.supermercado = supermercadoMain.Supermercado() 

    def test_carrinhoVazio(self):
        c1 = supermercadoMain.Carrinho()
        self.assertFalse(c1.itens)

    def test_produtosExistem(self):
        self.assertTrue(self.supermercado.produtos)

    def test_comprar1Banana(self):
        self.supermercado.comprar_item(1,1)
        self.assertTrue(self.supermercado.carrinho.itens)
        self.assertEqual(self.supermercado.carrinho.calcular_total(), 0.5)

    def test_comprar2Produtos(self):
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
        dono = supermercadoMain.DonoSupermercado(self.supermercado)
        dono.add_produto('Macarrao',2,50)
        self.assertIsNotNone(self.supermercado.produtos[3])

    def test_donoColocaNovoItem(self):
        dono = supermercadoMain.DonoSupermercado(self.supermercado)
        dono.add_produto('Macarrao',2,50)
        self.assertIsNotNone(self.supermercado.produtos[3])


if __name__ == '__main__':
    #unittest.main()
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Artefatos'))
    