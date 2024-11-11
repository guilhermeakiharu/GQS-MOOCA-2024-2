import pytest
from io import StringIO
from unittest.mock import patch

# Suponha que o código acima esteja no arquivo 'produtos.py'

# Importar as funções que você deseja testar
from produtos import adicionar_produto, remover_produto, contar_produtos, imprimir_produtos, produtos


@pytest.fixture
def reset_produtos():
    """Limpa a lista de produtos antes de cada teste"""
    produtos.clear()


def test_adicionar_produto(reset_produtos):
    adicionar_produto("Broca")
    assert "Broca" in produtos

    # Testar tentativa de adicionar o mesmo produto novamente
    adicionar_produto("Broca")
    assert produtos.count("Broca") == 1  # O produto não pode ser adicionado duas vezes


def test_remover_produto(reset_produtos):
    adicionar_produto("Tijolo")
    remover_produto("Tijolo")
    assert "Tijolo" not in produtos

    # Testando remoção de um produto que não existe
    remover_produto("Cimento")
    # Não deve lançar erro, mas pode verificar o comportamento da função via saída se necessário


def test_contar_produtos(reset_produtos):
    adicionar_produto("Porta")
    adicionar_produto("Cimento")
    assert contar_produtos() == 2

    remover_produto("Porta")
    assert contar_produtos() == 1


def test_imprimir_produtos(reset_produtos):
    # Vamos usar o patch para capturar a saída do print
    with patch("sys.stdout", new_callable=StringIO) as fake_out:
        imprimir_produtos()
        output = fake_out.getvalue()
        assert "Não há produtos para exibir." in output  # Verifica saída sem produtos

    # Agora vamos adicionar alguns produtos
    adicionar_produto("Azulejo")
    with patch("sys.stdout", new_callable=StringIO) as fake_out:
        imprimir_produtos()
        output = fake_out.getvalue()
        assert "Azulejo" in output  # Verifica que o produto adicionado é impresso
