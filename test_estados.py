import pytest
from estados import adicionar_estado, remover_estado, contar_estados, imprimir_estados, estados  # Importa a lista estados

# Fixture que limpa a lista de estados antes de cada teste
@pytest.fixture(autouse=True)
def limpa_estados():
    estados.clear()  # Limpa a lista de estados antes de cada teste
    yield  # Permite que o teste execute
    estados.clear()  # Limpa novamente após o teste

def test_adicionar_estado():
    adicionar_estado("Bahia")
    assert "Bahia" in estados

def test_adicionar_estado_existente():
    adicionar_estado("São Paulo")
    adicionar_estado("São Paulo")  # Tentar adicionar o mesmo estado
    assert estados.count("São Paulo") == 1  # Deve continuar 1

def test_remover_estado():
    adicionar_estado("Rio de Janeiro")
    remover_estado("Rio de Janeiro")
    assert "Rio de Janeiro" not in estados

def test_remover_estado_inexistente():
    remover_estado("Bahia")  # Tentar remover um estado que não existe
    assert "Bahia" not in estados

def test_contar_estados():
    adicionar_estado("Minas Gerais")
    adicionar_estado("Ceará")
    assert contar_estados() == 2  # A função deve contar corretamente

def test_imprimir_estados(capsys):
    adicionar_estado("Paraná")
    imprimir_estados()
    captured = capsys.readouterr()
    assert "Estados:" in captured.out
    assert "Paraná" in captured.out
