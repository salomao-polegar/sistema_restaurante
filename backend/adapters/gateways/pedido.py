from entities import Pedido
from common.interfaces.dbconnection import DbConnection
from common.interfaces.gateways import PedidoGatewayInterface
from common.tipos import ParametroBd
from common.dto import PedidoDTO
from typing import List

class PedidoGateway (PedidoGatewayInterface):
    repositorio: DbConnection
    nomeTabela = "pedidos"

    def __init__(self, repositorio: DbConnection):
        self.repositorio = repositorio
    
    def listar_todos(self) -> List[Pedido]:
        ordem = [
            ['status_pedido', 'ASC'],
            ['datahora_recebido', "ASC"],
            
        ]
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela, 
            None, 
            [
                ParametroBd(campo = "status_pedido", valor = 1),
                ParametroBd(campo = "status_pedido", valor = 2),
                ParametroBd(campo = "status_pedido", valor = 3)
            ], 
            "OR",
            ordem)

        if result == None: return None
        
        returnData: List[Pedido] = []

        for p in result:
            returnData.append(Pedido(
                id = p['id'],
                status_pedido= p['status_pedido'],
                cliente= p['cliente'],
                datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                status_pagamento=p['status_pagamento']))
            
        return returnData
        
    def novo(self, pedido_dto: PedidoDTO) -> bool:
        parametros: List[ParametroBd] = []
        
        parametros.append(ParametroBd(campo = "status_pedido", valor = pedido_dto.status_pedido))
        parametros.append(ParametroBd(campo = "cliente", valor = pedido_dto.cliente))
        parametros.append(ParametroBd(campo = "status_pagamento", valor = pedido_dto.status_pagamento))
        
        return self.repositorio.inserir(self.nomeTabela, parametros)

    def retornar_pelo_id(self, pedido_id: int) -> Pedido:
        retornoBd = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "id", valor = pedido_id)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None

        p = retornoBd[0]
        return Pedido(
                    id = p['id'],
                    status_pedido= p['status_pedido'],
                    cliente= p['cliente'],
                    datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                    status_pagamento=p['status_pagamento'])
        
    def editar(self, pedido_dto: PedidoDTO) -> bool:
        parametros: List[ParametroBd] = []
        parametros.append(ParametroBd(campo = "status_pedido", valor = pedido_dto.status_pedido))
        parametros.append(ParametroBd(campo = "cliente", valor = pedido_dto.cliente))
        parametros.append(ParametroBd(campo = "datahora_recebido", valor = pedido_dto.datahora_recebido))
        parametros.append(ParametroBd(campo = "datahora_preparacao", valor = pedido_dto.datahora_preparacao))
        parametros.append(ParametroBd(campo = "datahora_pronto", valor = pedido_dto.datahora_pronto))
        parametros.append(ParametroBd(campo = "datahora_finalizado", valor = pedido_dto.datahora_finalizado))
        parametros.append(ParametroBd(campo = "status_pagamento", valor = pedido_dto.status_pagamento))
        
        retornoBd = self.repositorio.editar(
            self.nomeTabela,
            [ParametroBd(campo = "id", valor = pedido_dto.id)],
            parametros
        )
        if retornoBd == None: return None
        return True

    def deletar(self, pedido_id: int) -> bool:
        self.repositorio.deletar(
            self.nomeTabela,
            [ParametroBd(campo = "id", valor = pedido_id)]
        )
        return True
    
    def listar_pedidos_recebidos(self) -> List[Pedido]:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "status_pedido", valor = 1)])

        if result == None: return None
        if len(result) < 1: return None
        
        returnData: List[Pedido] = []
        for p in result:
            returnData.append(Pedido(
                id = p['id'],
                status_pedido= p['status_pedido'],
                cliente= p['cliente'],
                datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                status_pagamento=p['status_pagamento']))
            
        return returnData


    def listar_pedidos_em_preparacao(self) -> List[Pedido]:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "status_pedido", valor = 2)])

        if result == None: return None
        if len(result) < 1: return None
        
        returnData: List[Pedido] = []
        for p in result:
            returnData.append(Pedido(
                id = p['id'],
                status_pedido= p['status_pedido'],
                cliente= p['cliente'],
                datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                status_pagamento=p['status_pagamento']))
            
        return returnData
    
    def listar_pedidos_finalizados(self) -> List[Pedido]:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "status_pedido", valor = 3)])

        if result == None: return None
        if len(result) < 1: return None
        
        returnData: List[Pedido] = []
        for p in result:
            returnData.append(Pedido(
                id = p['id'],
                status_pedido= p['status_pedido'],
                cliente= p['cliente'],
                datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                status_pagamento=p['status_pagamento']))
            
        return returnData

    def listar_pedidos_nao_finalizados(self) -> List[Pedido]:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "status_pedido", valor = 1),
            ParametroBd(campo = "status_pedido", valor = 2),
            ParametroBd(campo = "status_pedido", valor = 3)])

        if result == None: return None
        if len(result) < 1: return None
        
        returnData: List[Pedido] = []
        for p in result:
            returnData.append(Pedido(
                id = p['id'],
                status_pedido= p['status_pedido'],
                cliente= p['cliente'],
                datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                status_pagamento=p['status_pagamento']))
            
        return returnData
    
    def listar_fila(self) -> list:
        result = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "status_pedido", valor = 1)])
        # TODO: status = 1 OR status = 2

        if result == None: return None
        if len(result) < 1: return None
        
        returnData: List[Pedido] = []
        for p in result:
            returnData.append(Pedido(
                id = p['id'],
                status_pedido= p['status_pedido'],
                cliente= p['cliente'],
                datahora_recebido= p['datahora_recebido'],
                datahora_preparacao = p['datahora_preparacao'],
                datahora_pronto = p['datahora_pronto'],
                datahora_finalizado= p['datahora_finalizado'],
                status_pagamento=p['status_pagamento']))
            
        return returnData

    def retorna_status_pagamento(self, pedido_id: int) -> str:
        retornoBd = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            ['status_pagamento'],
            [ParametroBd(campo = "id", valor = pedido_id)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None
        print(retornoBd[0]['status_pagamento'])
        return str(retornoBd[0]['status_pagamento'])


    def retorna_ultimo_id(self) -> int:
        return self.repositorio.retorna_ultimo_id(self.nomeTabela)[0]['id']
    