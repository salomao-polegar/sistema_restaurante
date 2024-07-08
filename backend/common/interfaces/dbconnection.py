from common.tipos import ParametroBd
from typing import Protocol, List

class DbConnection (Protocol):
  def buscar_por_parametros(nomeTabela: str, 
                            campos: list[str] | None, 
                            parametros: list[ParametroBd],
                            tipo_where: str = "AND",
                            ordem: List[List[str]] | None = None):
    pass

  def buscar_todas(nomeTabela: str, campos: list[str] | None = None):
    pass

  def inserir(nomeTabela: str, parametros: list[ParametroBd]):
    pass

  def editar(nomeTabela: str, condicoes: list[ParametroBd], parametros: list[ParametroBd]):
    pass

  def deletar(nomeTabela, condicoes = list[ParametroBd]):
    pass

  def retorna_ultimo_id(self, nomeTabela) -> int:
    pass