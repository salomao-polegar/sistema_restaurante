import mysql.connector
from typing import List
import domain, sys
from ports.repositories.produto import ProdutoRepositoryPort

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
        produtos = cursor.fetchall()
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
        if produto.ativo:
            cursor.execute("""UPDATE produtos SET ativo = %(ativo)s 
                           WHERE id = %(id)s;""", 
                           ({'ativo' : produto.ativo,
                             'id' : produto.id}))

        self._connection.commit()
        self._connection.close()
        
        return produto
    
    def delete_produto(self, produto: domain.Produto) -> bool:
        if not self._connection.is_connected():
            self.__init__()
        self._cursor.execute('delete from produtos where id=%(id)s', ({'id':produto.id}))
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
    