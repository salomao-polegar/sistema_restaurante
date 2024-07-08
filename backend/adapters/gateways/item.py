from typing import Protocol, List
from entities.item import Item
from entities.produto import Produto
from entities.pedido import Pedido
from common.dto import ItemDTO, PedidoDTO
from external.mysql_database import DbConnection
from common.interfaces.gateways import ItemGatewayInterface
from common.tipos import ParametroBd

class ItemGateway(ItemGatewayInterface):
    repositorio: DbConnection
    nomeTabela = "itens"

    def __init__(self, repositorio: DbConnection):
        self.repositorio = repositorio

    def novo(self, item_dto: ItemDTO) -> bool:
        parametros: List[ParametroBd] = []
        
        parametros.append(ParametroBd(campo = "produto", valor = item_dto.produto.id))
        parametros.append(ParametroBd(campo = "pedido", valor = item_dto.pedido.id))
        parametros.append(ParametroBd(campo = "quantidade", valor = item_dto.quantidade))
        parametros.append(ParametroBd(campo = "descricao", valor = item_dto.descricao))
        parametros.append(ParametroBd(campo = "valor", valor = item_dto.valor))
        
        
        return self.repositorio.inserir(self.nomeTabela, parametros)
   
    def listar_itens(self, pedido_id: int) -> List[Item]:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela, 
            None,
            [ParametroBd(campo = "pedido", valor = pedido_id)]
            )

        if result == None: return None
        else:
            returnData: List[Item] = []
            
            for p in result:
                returnData.append(Item(
                    produto= Produto(id=p['produto']),
                    pedido = Pedido(id=p['pedido']),
                    quantidade = p['quantidade'],
                    descricao = p['descricao'],
                    valor = p['valor']))
                
            return returnData
        
    def retornar_item(self, item_dto: ItemDTO) -> List[Item]:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela, 
            None,
            [ParametroBd(campo = "pedido", valor = item_dto.pedido),
             ParametroBd(campo = "produto", valor = item_dto.produto)]
            )

        if result == None: return None
        else:
            returnData: List[Item] = []
            
            for p in result:
                returnData.append(Item(
                    produto= Produto(id=p['produto']),
                    pedido = Pedido(id=p['pedido']),
                    quantidade = p['quantidade'],
                    descricao = p['descricao']))
                
            return returnData

    
    def editar(self, item_dto: ItemDTO) -> bool:
        parametros: List[ParametroBd] = []
        parametros.append(ParametroBd(campo = "quantidade", valor = item_dto.quantidade))
        parametros.append(ParametroBd(campo = "descricao", valor = item_dto.descricao))
        
        retornoBd = self.repositorio.editar(
            self.nomeTabela,
            [ParametroBd(campo = "produto", valor = item_dto.produto),
            ParametroBd(campo = "pedido", valor = item_dto.pedido)],
            parametros
        )
        if retornoBd == None: return None
        return True

    def deletar(self, item_dto: ItemDTO) -> bool:
        self.repositorio.deletar(
            self.nomeTabela,
            [ParametroBd(campo = "produto", valor = item_dto.produto),
             ParametroBd(campo = "pedido", valor = item_dto.pedido)]
        )
        return True