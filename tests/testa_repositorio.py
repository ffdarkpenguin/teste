import pytest

from src import erros


parametros = [
    ('repo_jogo', 'jogo'),
    ('repo_usuario', 'usuario')
]


@pytest.mark.parametrize(
        'repo, params',
        parametros
)
def testa_insere_adiciona_dados_no_banco(repo, params, request):
    repo1 = request.getfixturevalue(repo)
    params1 = request.getfixturevalue(params)
    repo1.insere(params1)
    assert repo1.busca_por_id(1) == params1


@pytest.mark.parametrize(
        'repo, params',
        parametros
)
def testa_busca_por_id_inexistente_gera_erro(repo, params, request):
    repo1 = request.getfixturevalue(repo)
    _ = request.getfixturevalue(params)
    with pytest.raises(erros.NaoEncontrado):
        repo1.busca_por_id(1)


@pytest.mark.parametrize(
        'repo, params',
        parametros
)
def testa_busca_por_id_retorna_objeto_com_id_buscado(
        repo, params, request):
    repo1 = request.getfixturevalue(repo)
    params1 = request.getfixturevalue(params)
    repo1.insere(params1)
    ret = repo1.busca_por_id(1)
    assert ret.id == params1.id
