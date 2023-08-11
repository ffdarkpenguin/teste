from typing import Type

from src.zorra_total.modelo_jogo import Jogo
from src.zorra_total.repositorio_memoria import Repositorio


class RepoJogo(Repositorio[Jogo]):
    def modelo(self) -> Type:
        return Jogo
