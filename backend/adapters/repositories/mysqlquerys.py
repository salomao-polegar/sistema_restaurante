INSERIR_PRODUTO = """INSERT INTO produtos (id, nome, categoria, valor, descricao, ativo) 
                        VALUES (%(id)s, %(nome)s, %(categoria)s, %(valor)s, %(descricao)s, 1)"""

SELECT_PRODUTO_BY_ID = 'Select * FROM produtos where id=%(produto_id)s'

LISTAR_PRODUTOS_ATIVOS = "SELECT * FROM produtos WHERE ativo = 1"

DELETE_PRODUTO = 'delete from produtos where id=%(id)s'