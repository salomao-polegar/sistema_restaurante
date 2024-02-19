import mysql.connector
from typing import List
import domain, sys
import pandas as pd
from json import loads
from ports.repositories import ProdutoRepositoryPort, ItemRepositoryPort, PedidoRepositoryPort
from .mysqlquerys import *
# TODO
# Pensar em mensagens personalizadas para exceções, inclusive para erro de conexão com o banco de dados


class MysqlRepo(ProdutoRepositoryPort, ItemRepositoryPort, PedidoRepositoryPort):

    def __init__(self):

        if 'pytest' in sys.modules:
            host = '127.0.0.1'
        else:
            host = 'tc_database'

        self._conexao = mysql.connector.connect(
                    user='root',
                    password='ROOTPASS',
                    host=host, # Deve ser o mesmo nome do serviço/container criado no docker-compose.yml, (ou verificar no docker network)
                    port=3306,
                    database='TechChallenge'
                )
        
        

        self._cursor = self._conexao.cursor(dictionary=True)
    
### OPERAÇÕES COM PRODUTOS ###
            
    def inserir_produto(self, produto: domain.Produto) -> domain.produto:
        if not self._conexao.is_connected():
            self.__init__()
        self._cursor.execute(INSERIR_PRODUTO, 
                        ({'id' : produto.id,
                          'nome': produto.nome,
                          'categoria': produto.categoria,
                          'valor': produto.valor,
                          'descricao': produto.descricao,
                          }))
        self._conexao.commit()
        self._conexao.close()
        return self.listar_produtos()[-1]
    
    def retornar_produto(self, produto_id: int) -> domain.Produto | None: 
        if not self._conexao.is_connected():
            self.__init__()
        self._cursor.execute(SELECT_PRODUTO_BY_ID, 
                       ({'produto_id':produto_id}))
        
        for i in self._cursor:
            produto = domain.Produto(
                id=i["id"],
                nome=i["nome"],
                categoria=i["categoria"],
                valor=i["valor"],
                descricao=i["descricao"],
                ativo=i["ativo"],
            )
            
            self._conexao.close()
            return produto
        self._conexao.close()
        return None

    def listar_produtos(self) -> List[domain.Produto]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute(LISTAR_PRODUTOS_ATIVOS)
        produtos = []
        for i in self._cursor:
            produtos.append(domain.Produto(
                id=i["id"],
                nome=i["nome"],
                categoria=i["categoria"],
                valor=i["valor"],
                descricao=i["descricao"],
                ativo=i["ativo"],
            ))

        self._conexao.close()
        return produtos
    
    def listar_lanches(self) -> List[domain.Produto]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 1')
        produtos = self._cursor.fetchall()
        self._conexao.close()
        return produtos
    
    def listar_acompanhamentos(self) -> List[domain.Produto]:
        if not self._conexao.is_connected():
            self.__init__()
        self._cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 2')
        produtos = self._cursor.fetchall()
        self._conexao.close()
        return produtos
    
    def listar_bebidas(self) -> List[domain.Produto]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 3')
        produtos = self._cursor.fetchall()
        self._conexao.close()
        return produtos
    
    def listar_sobremesas(self) -> List[domain.Produto]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 4')
        produtos = self._cursor.fetchall()
        self._conexao.close()
        return produtos

    def editar_produto(self, produto: domain.Produto) -> domain.Produto:
        if not self._conexao.is_connected():
            self.__init__()
        
        
        if produto.nome:
            self._cursor.execute("""UPDATE produtos SET nome = %(nome)s 
                           WHERE id = %(id)s;""", 
                           ({'nome' : produto.nome,
                             'id' : produto.id}))

        if produto.categoria:
            self._cursor.execute("""UPDATE produtos SET categoria = %(categoria)s 
                           WHERE id = %(id)s;""", 
                           ({'categoria' : produto.categoria,
                             'id' : produto.id}))

        if produto.valor:
            self._cursor.execute("""UPDATE produtos SET valor = %(valor)s 
                           WHERE id = %(id)s;""", 
                           ({'valor' : produto.valor,
                             'id' : produto.id}))
        if produto.descricao:
            self._cursor.execute("""UPDATE produtos SET descricao = %(descricao)s 
                           WHERE id = %(id)s;""", 
                           ({'descricao' : produto.descricao,
                             'id' : produto.id}))
        if produto.ativo != None:
            print('update ativo to', produto.ativo)
            self._cursor.execute("""UPDATE produtos SET ativo = %(ativo)s 
                           WHERE id = %(id)s;""", 
                           ({'ativo' : produto.ativo,
                             'id' : produto.id}))

        self._conexao.commit()
        self._conexao.close()
        
        return self.retornar_produto(produto.id)
    
    def deletar_produto(self, produto_id: int) -> bool:
        if not self._conexao.is_connected():
            self.__init__()
        self._cursor.execute(DELETE_PRODUTO, ({'id':produto_id}))
        self._conexao.commit()
        self._conexao.close()
        return True
    
### OPERAÇÕES COM CLIENTES ###
    
    def inserir_cliente(self, cliente: domain.Cliente) -> domain.cliente:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute("""INSERT INTO clientes (id, cpf, nome, email, telefone, ativo) 
                        VALUES (%(id)s, %(cpf)s, %(nome)s, %(email)s, %(telefone)s, 1)""", 
                        ({'id' : cliente.id,
                          'cpf': cliente.cpf,
                          'nome': cliente.nome,
                          'email': cliente.email,
                          'telefone': cliente.telefone,
                          }))
        self._conexao.commit()
        self._conexao.close()
        return self.listar_clientes()[-1]
    
    def retornar_cliente_pelo_id(self, cliente_id: int) -> domain.Cliente | None: 
        if not self._conexao.is_connected():
            self.__init__()
        

        self._cursor.execute('Select * FROM clientes where id=%(cliente_id)s', 
                       ({'cliente_id':cliente_id}))
        
        for i in self._cursor:
            cliente = domain.Cliente(
                id=i["id"],
                cpf=i['cpf'],
                nome=i["nome"],
                email=i["email"],
                telefone=i["telefone"],
                ativo = i['ativo']
            )
            
            self._conexao.close()
            return cliente
        self._conexao.close()
        return None
    
    def retornar_cliente_pelo_cpf(self, cliente_cpf: int) -> domain.Cliente | None: 
        if not self._conexao.is_connected():
            self.__init__()
        

        self._cursor.execute('Select * FROM clientes where cpf=%(cliente_cpf)s', 
                       ({'cliente_cpf':cliente_cpf}))
        
        for i in self._cursor:
            cliente = domain.Cliente(
                id=i["id"],
                cpf=i['cpf'],
                nome=i["nome"],
                email=i["email"],
                telefone=i["telefone"],
                ativo = i['ativo']
            )
            
            self._conexao.close()
            return cliente
        self._conexao.close()
        return None

    def listar_clientes(self) -> List[domain.Cliente]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM clientes WHERE ativo = 1')
        
        clientes = []
        for i in self._cursor:
            clientes.append(domain.Cliente(
                id=i["id"],
                cpf=i['cpf'],
                nome=i["nome"],
                email=i["email"],
                telefone=i["telefone"],
                ativo = i['ativo']
            ))
        self._conexao.close()
        return clientes
    
    def editar_cliente(self, cliente: domain.Cliente) -> domain.Cliente:
        if not self._conexao.is_connected():
            self.__init__()
        
               
        if cliente.nome:
            self._cursor.execute("""UPDATE clientes SET nome = %(nome)s 
                           WHERE id = %(id)s;""", 
                           ({'nome' : cliente.nome,
                             'id' : cliente.id}))

        if cliente.email:
            self._cursor.execute("""UPDATE clientes SET email = %(email)s 
                           WHERE id = %(id)s;""", 
                           ({'email' : cliente.email,
                             'id' : cliente.id}))

        if cliente.telefone:
            self._cursor.execute("""UPDATE clientes SET telefone = %(telefone)s 
                           WHERE id = %(id)s;""", 
                           ({'telefone' : cliente.telefone,
                             'id' : cliente.id}))
        if cliente.ativo != None:
            self._cursor.execute("""UPDATE clientes SET ativo = %(ativo)s 
                           WHERE id = %(id)s;""", 
                           ({'ativo' : cliente.ativo,
                             'id' : cliente.id}))

        self._conexao.commit()
        self._conexao.close()
        
        return self.retornar_cliente_pelo_id(cliente.id)
    
    def deletar_cliente(self, cliente_id: int) -> bool:
        if not self._conexao.is_connected():
            self.__init__()
        self._cursor.execute('delete from clientes where id=%(id)s', ({'id':cliente_id}))
        self._conexao.commit()
        self._conexao.close()
        return True
    
### OPERAÇÕES COM PEDIDOS ###
    
    def inserir_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute("""INSERT INTO pedidos (cliente) 
                        VALUES (%(cliente)s)""", 
                        ({'cliente': pedido.cliente,
                          }))
        self._conexao.commit()
        self._conexao.close()
        pedido = self.listar_pedidos()[-1]
        
        return pedido
    
    def retornar_pedido(self, pedido_id: int) -> domain.Pedido | None: 
        if not self._conexao.is_connected():
            self.__init__()
        

        self._cursor.execute('Select * FROM pedidos where id=%(pedido_id)s', 
                       ({'pedido_id':pedido_id}))
        
        for i in self._cursor:
            
            pedido = domain.Pedido(
                id=i["id"],
                status_pedido=i['status_pedido'],
                cliente=i["cliente"],
                datahora=i["datahora"]
            )
            
            self._conexao.close()
            return pedido
        self._conexao.close()
        return None

    def listar_pedidos(self) -> List[domain.Pedido]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM pedidos WHERE status_pedido != 4 ORDER BY status_pedido DESC;')
        pedidos = []
        for i in self._cursor:
            pedidos.append(domain.Pedido(
                id=i["id"],
                status_pedido=i['status_pedido'],
                cliente=i["cliente"],
                datahora=i["datahora"])
            )
        
        self._conexao.close()
        return pedidos
    
    def listar_pedidos_recebidos(self) -> List[domain.Pedido]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM pedidos WHERE status_pedido = 1')
        pedidos = self._cursor.fetchall()
        self._conexao.close()
        return pedidos

    def listar_pedidos_em_preparacao(self) -> List[domain.Pedido]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM pedidos WHERE status_pedido = 2')
        pedidos = self._cursor.fetchall()
        self._conexao.close()
        return pedidos    

    def listar_pedidos_finalizados(self) -> List[domain.Pedido]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM pedidos WHERE status_pedido = 3')
        pedidos = self._cursor.fetchall()
        self._conexao.close()
        return pedidos

    def listar_pedidos_nao_finalizados(self) -> List[domain.Pedido]:
        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM pedidos WHERE status_pedido = 1 OR WHERE status_pedido = 2 OR WHERE status_pedido = 3')
        pedidos = self._cursor.fetchall()
        self._conexao.close()
        return pedidos
    
    def editar_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        if not self._conexao.is_connected():
            self.__init__()
        
               
        if pedido.status_pedido:
            self._cursor.execute("""UPDATE pedidos SET status_pedido = %(status_pedido)s 
                           WHERE id = %(id)s;""", 
                           ({'status_pedido' : pedido.status_pedido,
                             'id' : pedido.id}))
        self._conexao.commit()
        self._conexao.close()
        
        return self.retornar_pedido(pedido.id)
    
    def deletar_pedido(self, pedido_id: int) -> bool:
        if not self._conexao.is_connected():
            self.__init__()
        self._cursor.execute('delete from pedidos where id=%(id)s', ({'id':pedido_id}))
        self._conexao.commit()
        self._conexao.close()
        return True
    
    def listar_fila(self) -> list:
        # pedidos recebidos e em preparação

        if not self._conexao.is_connected():
            self.__init__()
        
        self._cursor.execute('Select * FROM pedidos WHERE status_pedido = 1 OR status_pedido = 2 ORDER BY datahora ASC')
        pedidos = self._cursor.fetchall()
        self._conexao.close()
        
        fila = pd.DataFrame(pedidos)[['id', 'status_pedido', 'cliente', 'datahora']]
        fila['posicao'] = fila.index
        fila['posicao'] = fila['posicao'].apply(lambda x: x+1)
        return (loads(fila.to_json(orient='records')))
    
    def retorna_status_pagamento(self, pedido_id: int) -> str:
        if not self._conexao.is_connected():
            self.__init__()
        
        status_pagamento = self._cursor.execute('Select status_pagamento_pedido FROM pedidos WHERE id = %(id)s', ({'id' : pedido_id}))
        self._conexao.close()

        return (status_pagamento)
    
    # ITENS
    def editar_item(self, item: domain.Item) -> domain.Item:

        if not self._conexao.is_connected():
            self.__init__()
        
        if item.quantidade:
            self._cursor.execute("""UPDATE itens SET quantidade = %(quantidade)s 
                           WHERE id_pedido = %(id_pedido)s AND id_produto = %(id_produto)s;""", 
                           ({'quantidade' : item.quantidade,
                             'id_pedido' : item.pedido,
                             'id_produto' : item.produto
                             }))

        self._conexao.commit()
        self._conexao.close()
        
        return item

    def listar_itens(self, pedido_id: int) -> List[domain.Item]:
        if not self._conexao.is_connected():
            self.__init__()

        
        self._cursor.execute("""SELECT pro.id AS "produto", ped.id AS "pedido", pp.quantidade from produtos pro
                        inner join itens pp on (pro.id = pp.id_produto)
                        inner join pedidos ped on (ped.id = pp.id_pedido)
                        where ped.id = %(id_pedido)s;""", 
                        ({"id_pedido" : pedido_id}))
        itens = []
        for i in self._cursor:
            itens.append(domain.Item(
                produto = i['produto'],
                pedido = i['pedido'],
                quantidade=i['quantidade']
            ))
        

        self._conexao.commit()
        self._conexao.close()
        return itens

    def inserir_item(self, item: domain.Item) -> domain.Item:
        if not self._conexao.is_connected():
            self.__init__()

        
        self._cursor.execute("""INSERT INTO itens (id_produto, id_pedido, quantidade) 
                    VALUES (%(id_produto)s, %(id_pedido)s, %(quantidade)s);""", 
                    ({
                        "id_pedido" : item.pedido, 
                        "id_produto" : item.produto,
                        "quantidade": item.quantidade}))
        self._conexao.commit()
        self._conexao.close()
        return item
    
    def deletar_item(self, produto: domain.Item) -> bool:
        if not self._conexao.is_connected():
            self.__init__()

        
        self._cursor.execute("""DELETE FROM itens WHERE id_produto = %(id_produto)s AND id_pedido = %(id_pedido)s;""", 
                    ({
                        "id_pedido" : produto.pedido, 
                        "id_produto" : produto.produto
                        }))
        self._conexao.commit()
        self._conexao.close()
        return True


        # buscar se já existir mesmo id, somente alterar a quantidade