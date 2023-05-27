class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade


class Carrinho:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade):
        self.itens.append((produto, quantidade))

    def remover_item(self, produto):
        for item in self.itens:
            if item[0] == produto:
                self.itens.remove(item)
                break
            else:
                raise IndexError('Index out of bounds exception')

    def calcular_total(self):
        total = 0
        for item in self.itens:
            produto, quantidade = item
            total += produto.preco * quantidade
        return total


class DonoSupermercado:
    def __init__(self, supermercado):
        self.supermercado = supermercado

    def add_produto(self, nome, preco, quantidade):
        produto = Produto(nome, preco, quantidade)
        self.supermercado.produtos.append(produto)
        print("Produto adicionado com sucesso.")

    def remover_produto(self, produto_index):
        try:
            produto = self.supermercado.produtos[produto_index - 1]
            self.supermercado.produtos.remove(produto)
            print("Produto removido com sucesso.")
        except IndexError:
            print("Numero de produto invalido.")

    def update_produto_preco(self, produto_index, novo_preco):
        try:
            produto = self.supermercado.produtos[produto_index - 1]
            produto.preco = novo_preco
            print("Preco do produto atualizado.")
        except IndexError:
            print("Numero de produto invalido.")

    def update_produto_quantidade(self, produto_index, nova_quantidade):
        try:
            produto = self.supermercado.produtos[produto_index - 1]
            produto.quantidade = nova_quantidade
            print("Quantidade do produto atualizada.")
        except IndexError:
            print("Numero de produto invalido.")


class Supermercado:
    def __init__(self):
        self.produtos = [
            Produto("Banana", 0.5, 50),
            Produto("Leite", 5, 100),
            Produto("Laranja", 1.5, 75),
        ]
        self.carrinho = Carrinho()

    def ver_produtos(self):
        print("\n=====================")
        print("Produtos disponiveis:")
        for i, produto in enumerate(self.produtos, 1):
            print(f"{i}. {produto.nome} - ${produto.preco}")
        print("=====================")

    def comprar_item(self, produto_index, quantidade):
        produto = self.produtos[produto_index - 1]
        if produto.quantidade >= quantidade:
            self.carrinho.adicionar_item(produto, quantidade)
            produto.quantidade -= quantidade
            print("Item adicionado ao carrinho.")
        else:
            print("Quantidade insuficiente.")

    def remover_do_carrinho(self, produto_index):
        produto, quantidade = self.carrinho.itens[produto_index - 1]
        self.carrinho.remover_item(produto)
        produto.quantidade += quantidade
        print("Item removido do carrinho.")

    def ver_carrinho(self):
        print("\n####################")
        print("Carrinho:")
        for i, item in enumerate(self.carrinho.itens, 1):
            produto, quantidade = item
            print(f"{i}. {produto.nome} - ${produto.preco} x {quantidade}")
        print(f"Total: ${self.carrinho.calcular_total()}")
        print("####################")


def main():
    supermercado = Supermercado()
    owner = DonoSupermercado(supermercado)

    while True:
        print("\n--- Supermercado Inatel ---")
        print("1. Mostrar produtos")
        print("2. Adicionar item ao carrinho")
        print("3. Remover item do carrinho")
        print("4. Ver carrinho")
        print("5. Adicionar produto (Dono)")
        print("6. Remover produto (Dono)")
        print("7. Atualizar preco do produto (Dono)")
        print("8. Atualizar quantidade do produto (Dono)")
        print("9. Sair")

        choice = input("O que deseja fazer? (1-9): ")

        if choice == "1":
            supermercado.ver_produtos()
        elif choice == "2":
            supermercado.ver_produtos()
            produto_index = int(input("Entre o numero do produto: "))
            quantidade = int(input("Entre a quantidade quantidade: "))
            supermercado.comprar_item(produto_index, quantidade)
        elif choice == "3":
            supermercado.ver_carrinho()
            produto_index = int(input("Entre o numero do produto a ser removido: "))
            supermercado.remover_do_carrinho(produto_index)
        elif choice == "4":
            supermercado.ver_carrinho()
        elif choice == "5":
            nome = input("Entre o nome do produto: ")
            preco = float(input("Entre o preco do produto: "))
            quantidade = int(input("Entre a quantidade do produto: "))
            owner.add_produto(nome, preco, quantidade)
        elif choice == "6":
            supermercado.ver_produtos()
            produto_index = int(input("Entre o numero do produto a ser removido: "))
            owner.remover_produto(produto_index)
        elif choice == "7":
            supermercado.ver_produtos()
            produto_index = int(input("Entre o numero do produto a ser atualizado: "))
            novo_preco = float(input("Entre o novo preco do produto: "))
            owner.update_produto_preco(produto_index, novo_preco)
        elif choice == "8":
            supermercado.ver_produtos()
            produto_index = int(input("Entre o numero do produto a ser atualizado: "))
            nova_quantidade = int(input("Entre a nova quantidade: "))
            owner.update_produto_quantidade(produto_index, nova_quantidade)
        elif choice == "9":
            print("Obrigado, volte sempre!")
            break
        else:
            print("Escolha inválida. Tente novamente.")


if __name__ == "__main__":
    main()

