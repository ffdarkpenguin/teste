from typing import Type

from src.ddd.dominio.jogo import Jogo
from src.ddd.repositorios.repositorio_memoria import Repositorio


class RepoJogo(Repositorio[Jogo]):
    def modelo(self) -> Type:
        return Jogo
