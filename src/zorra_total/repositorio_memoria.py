from typing import TypeVar, Generic, Type
from abc import abstractmethod

from pydantic import BaseModel

from src import erros

Modelo = TypeVar('Modelo', bound=BaseModel)


class Repositorio(list, Generic[Modelo]):
    @abstractmethod
    def modelo(self) -> Type:
        ...

    def insere(self, param: Modelo):
        dados = param.model_dump(by_alias=True)
        try:
            self.busca_por_id(dados['_id'])
            raise erros.Duplicado(
                f'Já existe um registro com ID: {dados["_id"]}')
        except erros.NaoEncontrado:
            self.append(dados)

    def busca_por_id(self, _id) -> Modelo:
        try:
            dados = next(x for x in self if x['_id'] == _id)
            return self.modelo()(**dados)
        except StopIteration:
            raise erros.NaoEncontrado(f'Não encontrei registro com ID: {_id}')
