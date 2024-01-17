# PEDIDO

# Os clientes podem se identificar ou não, montando um combo com: lanches, acompanhamentos e bebidas

from enum import Enum

# Gerenciamento de Produtos e Categorias
# Categorias fixas

class CategoriaProduto(Enum):
    LANCHE = 1
    ACOMPANHAMENTO = 2
    BEBIDA = 3
    SOBREMESA = 4


class Produto():

    def adicionar_produto(self, nome, categoria, valor, descricao = '', ativo = 1):
        self.nome = nome # lanche, acompanhamento ou bebida
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao
        self.ativo = ativo

    def ativar_produto(self):
        self.ativo = 1

    def desativar_produto(self):
        self.ativo = 0

    def editar_produto(self, nome = None, categoria = None, valor = None, descricao = None, ativo = None):
        if nome:
            self.nome = nome # lanche, acompanhamento ou bebida
        if categoria:
            self.categoria = categoria
        if valor:
            self.valor = valor
        if descricao:
            self.descricao = descricao
        if ativo:
            self.ativo = ativo

class Pedido():

    def __init__(self):
        self.produtos = []

    def adicionar_produto_ao_pedido(self, produto:Produto):
        self.produtos.append(produto)

    def retornar_itens_pedido(self):
        return self.produtos
    

    
