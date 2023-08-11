from typing import Type

from src.funcionalidade.jogo.modelo_jogo import Jogo
from src.funcionalidade.repositorios.repositorio_memoria import Repositorio


class RepoJogo(Repositorio[Jogo]):
    def modelo(self) -> Type:
        return Jogo
