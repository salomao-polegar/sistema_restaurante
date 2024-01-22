import mysql.connector
from typing import List
import domain, sys
import pandas as pd
from json import loads
from ports.repositories.produto import ProdutoRepositoryPort

# TODO
# Pensar em mensagens personalizadas para exceções, inclusive para erro de conexão com o banco de dados


class MysqlRepo(ProdutoRepositoryPort):

    def __init__(self):

        if 'pytest' in sys.modules:
            host = '127.0.0.1'
        else:
            host = 'tc_database'

        self._connection = mysql.connector.connect(
                    user='root',
                    password='ROOTPASS',
                    host=host, # Deve ser o mesmo nome do serviço/container criado no docker-compose.yml, (ou verificar no docker network)
                    port=3306,
                    database='TechChallenge'
                )
        
        

        self._cursor = self._connection.cursor(dictionary=True)
    
### OPERAÇÕES COM PRODUTOS ###
            
    def insert_produto(self, produto: domain.Produto) -> domain.produto:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute("""INSERT INTO produtos (id, nome, categoria, valor, descricao, ativo) 
                        VALUES (%(id)s, %(nome)s, %(categoria)s, %(valor)s, %(descricao)s, 1)""", 
                        ({'id' : produto.id,
                          'nome': produto.nome,
                          'categoria': produto.categoria,
                          'valor': produto.valor,
                          'descricao': produto.descricao,
                          }))
        self._connection.commit()
        self._connection.close()
        produto = self.get_todos_produtos()[-1]
        return produto
    
    def get_produto(self, produto_id: int) -> domain.Produto | None: 
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)

        cursor.execute('Select * FROM produtos where id=%(produto_id)s', 
                       ({'produto_id':produto_id}))
        
        for i in cursor:
            produto = domain.Produto(
                id=i["id"],
                nome=i["nome"],
                categoria=i["categoria"],
                valor=i["valor"],
                descricao=i["descricao"],
                ativo=i["ativo"],
            )
            
            self._connection.close()
            return produto
        self._connection.close()
        return None

    def get_todos_produtos(self) -> List[domain.Produto]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM produtos WHERE ativo = 1')
        produtos = []
        for i in cursor:
            produtos.append(domain.Produto(
                id=i["id"],
                nome=i["nome"],
                categoria=i["categoria"],
                valor=i["valor"],
                descricao=i["descricao"],
                ativo=i["ativo"],
            ))

        self._connection.close()
        return produtos
    
    def get_lanches(self) -> List[domain.Produto]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 1')
        produtos = cursor.fetchall()
        self._connection.close()
        return produtos
    
    def get_acompanhamentos(self) -> List[domain.Produto]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 2')
        produtos = cursor.fetchall()
        self._connection.close()
        return produtos
    
    def get_bebidas(self) -> List[domain.Produto]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 3')
        produtos = cursor.fetchall()
        self._connection.close()
        return produtos
    
    def get_sobremesas(self) -> List[domain.Produto]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM produtos WHERE ativo = 1 AND categoria = 4')
        produtos = cursor.fetchall()
        self._connection.close()
        return produtos

    def edita_produto(self, produto: domain.Produto) -> domain.Produto:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        
        if produto.nome:
            cursor.execute("""UPDATE produtos SET nome = %(nome)s 
                           WHERE id = %(id)s;""", 
                           ({'nome' : produto.nome,
                             'id' : produto.id}))

        if produto.categoria:
            cursor.execute("""UPDATE produtos SET categoria = %(categoria)s 
                           WHERE id = %(id)s;""", 
                           ({'categoria' : produto.categoria,
                             'id' : produto.id}))

        if produto.valor:
            cursor.execute("""UPDATE produtos SET valor = %(valor)s 
                           WHERE id = %(id)s;""", 
                           ({'valor' : produto.valor,
                             'id' : produto.id}))
        if produto.descricao:
            cursor.execute("""UPDATE produtos SET descricao = %(descricao)s 
                           WHERE id = %(id)s;""", 
                           ({'descricao' : produto.descricao,
                             'id' : produto.id}))
        if produto.ativo != None:
            print('update ativo to', produto.ativo)
            cursor.execute("""UPDATE produtos SET ativo = %(ativo)s 
                           WHERE id = %(id)s;""", 
                           ({'ativo' : produto.ativo,
                             'id' : produto.id}))

        self._connection.commit()
        self._connection.close()
        
        return self.get_produto(produto.id)
    
    def delete_produto(self, produto_id: int) -> bool:
        if not self._connection.is_connected():
            self.__init__()
        self._cursor.execute('delete from produtos where id=%(id)s', ({'id':produto_id}))
        self._connection.commit()
        self._connection.close()
        return True
    
### OPERAÇÕES COM CLIENTES ###
    
    def insert_cliente(self, cliente: domain.Cliente) -> domain.cliente:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute("""INSERT INTO clientes (id, cpf, nome, email, telefone, ativo) 
                        VALUES (%(id)s, %(cpf)s, %(nome)s, %(email)s, %(telefone)s, 1)""", 
                        ({'id' : cliente.id,
                          'cpf': cliente.cpf,
                          'nome': cliente.nome,
                          'email': cliente.email,
                          'telefone': cliente.telefone,
                          }))
        self._connection.commit()
        self._connection.close()
        return cliente
    
    def get_cliente(self, cliente_id: int) -> domain.Cliente | None: 
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)

        cursor.execute('Select * FROM clientes where id=%(cliente_id)s', 
                       ({'cliente_id':cliente_id}))
        
        for i in cursor:
            cliente = domain.Cliente(
                id=i["id"],
                cpf=i['cpf'],
                nome=i["nome"],
                email=i["email"],
                telefone=i["telefone"],
                ativo = i['ativo']
            )
            
            self._connection.close()
            return cliente
        self._connection.close()
        return None

    def get_todos_clientes(self) -> List[domain.Cliente]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM clientes WHERE ativo = 1')
        clientes = cursor.fetchall()
        self._connection.close()
        return clientes
    
    def edita_cliente(self, cliente: domain.Cliente) -> domain.Cliente:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
               
        if cliente.nome:
            cursor.execute("""UPDATE clientes SET nome = %(nome)s 
                           WHERE id = %(id)s;""", 
                           ({'nome' : cliente.nome,
                             'id' : cliente.id}))

        if cliente.email:
            cursor.execute("""UPDATE clientes SET email = %(email)s 
                           WHERE id = %(id)s;""", 
                           ({'email' : cliente.email,
                             'id' : cliente.id}))

        if cliente.telefone:
            cursor.execute("""UPDATE clientes SET telefone = %(telefone)s 
                           WHERE id = %(id)s;""", 
                           ({'telefone' : cliente.telefone,
                             'id' : cliente.id}))
        if cliente.ativo:
            cursor.execute("""UPDATE clientes SET ativo = %(ativo)s 
                           WHERE id = %(id)s;""", 
                           ({'ativo' : cliente.ativo,
                             'id' : cliente.id}))

        self._connection.commit()
        self._connection.close()
        
        return cliente
    
    def delete_cliente(self, cliente: domain.Cliente) -> bool:
        if not self._connection.is_connected():
            self.__init__()
        self._cursor.execute('delete from clientes where id=%(id)s', ({'id':cliente.id}))
        self._connection.commit()
        self._connection.close()
        return True
    
### OPERAÇÕES COM PEDIDOS ###
    
    def insert_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute("""INSERT INTO pedidos (cliente) 
                        VALUES (%(cliente)s)""", 
                        ({'cliente': pedido.cliente,
                          }))
        self._connection.commit()
        self._connection.close()
        todos_pedidos = self.get_todos_pedidos()[-1]
        
        # TODO
        # Por algum motivo, não está retornando o objeto criado.
        # O retorno deve ser com ID, então devemos fazer outra consulta no banco de dados para verificar qual o ID inserido
        return todos_pedidos
    
    def get_pedido(self, pedido_id: int) -> domain.Pedido | None: 
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)

        cursor.execute('Select * FROM pedidos where id=%(pedido_id)s', 
                       ({'pedido_id':pedido_id}))
        
        for i in cursor:
            
            pedido = domain.Pedido(
                id=i["id"],
                status_pedido=i['status_pedido'],
                cliente=i["cliente"],
                datahora=i["datahora"]
            )
            
            self._connection.close()
            return pedido
        self._connection.close()
        return None

    def get_todos_pedidos(self) -> List[domain.Pedido]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM pedidos;')
        pedidos = []
        for i in cursor:
            pedidos.append(domain.Pedido(
                id=i["id"],
                status_pedido=i['status_pedido'],
                cliente=i["cliente"],
                datahora=i["datahora"])
            )
        
        self._connection.close()
        return pedidos
    
    def get_pedidos_recebidos(self) -> List[domain.Pedido]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM pedidos WHERE status_pedido = 1')
        pedidos = cursor.fetchall()
        self._connection.close()
        return pedidos

    def get_pedidos_em_preparacao(self) -> List[domain.Pedido]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM pedidos WHERE status_pedido = 2')
        pedidos = cursor.fetchall()
        self._connection.close()
        return pedidos    

    def get_pedidos_finalizados(self) -> List[domain.Pedido]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM pedidos WHERE status_pedido = 3')
        pedidos = cursor.fetchall()
        self._connection.close()
        return pedidos

    def get_pedidos_nao_finalizados(self) -> List[domain.Pedido]:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM pedidos WHERE status_pedido = 1 OR WHERE status_pedido = 2 OR WHERE status_pedido = 3')
        pedidos = cursor.fetchall()
        self._connection.close()
        return pedidos
    
    def edita_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
               
        if pedido.status_pedido:
            cursor.execute("""UPDATE pedidos SET status_pedido = %(status_pedido)s 
                           WHERE id = %(id)s;""", 
                           ({'status_pedido' : pedido.status_pedido,
                             'id' : pedido.id}))
        self._connection.commit()
        self._connection.close()
        
        return pedido
    
    def delete_pedido(self, pedido: domain.Pedido) -> bool:
        if not self._connection.is_connected():
            self.__init__()
        self._cursor.execute('delete from pedidos where id=%(id)s', ({'id':pedido.id}))
        self._connection.commit()
        self._connection.close()
        return True
    
    def get_fila(self) -> list:
        # pedidos recebidos e em preparação

        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        cursor.execute('Select * FROM pedidos WHERE status_pedido = 1 OR status_pedido = 2 ORDER BY datahora ASC')
        pedidos = cursor.fetchall()
        self._connection.close()
        
        fila = pd.DataFrame(pedidos)[['id', 'status_pedido', 'cliente', 'datahora']]
        fila['posicao'] = fila.index
        fila['posicao'] = fila['posicao'].apply(lambda x: x+1)
        return (loads(fila.to_json(orient='records')))
        
    def editar_produtos_no_pedido(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:

        if not self._connection.is_connected():
            self.__init__()
        cursor = self._connection.cursor(dictionary=True)
        if produto.quantidade:
            cursor.execute("""UPDATE produtos_do_pedido SET quantidade = %(quantidade)s 
                           WHERE id_pedido = %(id)s AND id_produto = %(id)s;""", 
                           ({'quantidade' : produto.quantidade,
                             'id_pedido' : produto.pedido,
                             'id_produto' : produto.produto
                             }))

        self._connection.commit()
        self._connection.close()
        
        return self.produtos_no_pedido(produto.pedido)

    def produtos_no_pedido(self, pedido_id: int) -> List[domain.ProdutoNoPedido]:
        if not self._connection.is_connected():
            self.__init__()

        cursor = self._connection.cursor(dictionary=True)
        cursor.execute("""SELECT pro.nome, quantidade from produtos pro
                        inner join produtos_do_pedido pp on (pro.id = pp.id_produto)
                        inner join pedidos ped on (ped.id = pp.id_pedido)
                        where ped.id = %(id_pedido)s;""", 
                        ({"id_pedido" : pedido_id}))
        produtos_no_pedido = cursor.fetchall()
        self._connection.commit()
        self._connection.close()
        return produtos_no_pedido

    def adiciona_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        if not self._connection.is_connected():
            self.__init__()

        cursor = self._connection.cursor(dictionary=True)
        cursor.execute("""INSERT INTO produtos_do_pedido (id_produto, id_pedido, quantidade) 
                    VALUES (%(id_produto)s, %(id_pedido)s, %(quantidade)s);""", 
                    ({
                        "id_pedido" : produto.pedido, 
                        "id_produto" : produto.produto,
                        "quantidade": produto.quantidade}))
        self._connection.commit()
        self._connection.close()
        return produto


        # buscar se já existir mesmo id, somente alterar a quantidade