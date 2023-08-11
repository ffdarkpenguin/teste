import pytest

from src.modelo_jogo import Jogo
from src.modelo_usuario import Usuario
from src.repo_jogo import RepoJogo
from src.repo_usuario import RepoUsuario


@pytest.fixture
def repo_jogo():
    return RepoJogo()


@pytest.fixture
def jogo():
    return Jogo(_id=1, nome='jogo 1')


@pytest.fixture
def repo_usuario():
    return RepoUsuario()


@pytest.fixture
def usuario():
    return Usuario(_id=1, nome='ff', email='ff@ff', cel='91234')
