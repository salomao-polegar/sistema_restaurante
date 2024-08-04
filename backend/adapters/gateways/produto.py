from entities import Produto
from common.interfaces.dbconnection import DbConnection
from common.interfaces.gateways import ProdutoGatewayInterface
from common.tipos import ParametroBd
from common.dto import ProdutoDTO
from typing import List

class ProdutoGateway (ProdutoGatewayInterface):
    repositorio: DbConnection
    nomeTabela = "produtos"

    def __init__(self, repositorio: DbConnection):
        self.repositorio = repositorio
    
    def listar_todos(self) -> List[Produto]:
        result = self.repositorio.buscar_todas(self.nomeTabela, None)

        if result == None: return None
        else:
            returnData: List[Produto] = []
            
            for p in result:
                returnData.append(Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal']))
                
            return returnData
        
    def listar_lanches(self) -> List[Produto]:
        result = self.repositorio.buscar_por_parametros(self.nomeTabela, None, [ParametroBd(campo='categoria', valor=1)])

        if result == None: return None
        else:
            returnData: List[Produto] = []
            
            for p in result:
                returnData.append(Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal']))
                
            return returnData
    
    def listar_acompanhamentos(self) -> List[Produto]:
        result = self.repositorio.buscar_por_parametros(self.nomeTabela, None, [ParametroBd(campo='categoria', valor=2)])

        if result == None: return None
        else:
            returnData: List[Produto] = []
            
            for p in result:
                returnData.append(Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal']))
                
            return returnData
    
    def listar_bebidas(self) -> List[Produto]:
        result = self.repositorio.buscar_por_parametros(self.nomeTabela, None, [ParametroBd(campo='categoria', valor=3)])

        if result == None: return None
        else:
            returnData: List[Produto] = []
            
            for p in result:
                returnData.append(Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal']))
                
            return returnData
    
    def listar_sobremesas(self) -> List[Produto]:
        result = self.repositorio.buscar_por_parametros(self.nomeTabela, None, [ParametroBd(campo='categoria', valor=4)])

        if result == None: return None
        else:
            returnData: List[Produto] = []
            print(result)
            for p in result:
                returnData.append(Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal']))
                
            return returnData

        
    def novo(self, produto_dto: ProdutoDTO) -> Produto:
        parametros: List[ParametroBd] = []
        
        parametros.append(ParametroBd(campo = "nome", valor = produto_dto.nome))
        parametros.append(ParametroBd(campo = "categoria", valor = produto_dto.categoria))
        parametros.append(ParametroBd(campo = "valor", valor = produto_dto.valor))
        parametros.append(ParametroBd(campo = "descricao", valor = produto_dto.descricao))
        parametros.append(ParametroBd(campo = "ativo", valor = produto_dto.ativo))
        parametros.append(ParametroBd(campo = "foto_principal", valor = produto_dto.foto_principal))
        self.repositorio.inserir(self.nomeTabela, parametros)

        id_inserido = self.repositorio.retorna_ultimo_id(self.nomeTabela)
        
        return Produto(
                    id = id_inserido,
                    nome = produto_dto.nome,
                    categoria = produto_dto.categoria,
                    valor = produto_dto.valor,
                    descricao = produto_dto.descricao,
                    ativo = produto_dto.ativo) 

    def retornar_pelo_id(self, produto_id: int) -> Produto:
        retornoBd = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "id", valor = produto_id)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None

        p = retornoBd[0]
        return Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal'])
        
    def editar(self, produto_dto: ProdutoDTO) -> Produto:
        parametros: List[ParametroBd] = []
        parametros.append(ParametroBd(campo = "nome", valor = produto_dto.nome))
        parametros.append(ParametroBd(campo = "categoria", valor = produto_dto.categoria))
        parametros.append(ParametroBd(campo = "valor", valor = produto_dto.valor))
        parametros.append(ParametroBd(campo = "descricao", valor = produto_dto.descricao))
        parametros.append(ParametroBd(campo = "ativo", valor = produto_dto.ativo))
        parametros.append(ParametroBd(campo = "foto_principal", valor = produto_dto.foto_principal))
        
        retornoBd = self.repositorio.editar(
            self.nomeTabela,
            [ParametroBd(campo = "id", valor = produto_dto.id)],
            parametros
        )
        if retornoBd == None: return None
        
        produto_editado = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "id", valor = produto_dto.id)])

        if produto_editado == None: return None
        if len(produto_editado) < 1: return None

        p = produto_editado[0]
        return Produto(
                    id = p['id'],
                    nome = p['nome'],
                    categoria = p['categoria'],
                    valor = p['valor'],
                    descricao = p['descricao'],
                    ativo = p['ativo'],
                    foto_principal = p['foto_principal'])
        

    def deletar(self, produto_id: int) -> bool:
        self.repositorio.deletar(
            self.nomeTabela,
            [ParametroBd(campo = "id", valor = produto_id)]
        )
        return True
