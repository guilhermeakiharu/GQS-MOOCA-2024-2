# estado.py

# Lista para armazenar os estados
produtos = []

# Função para adicionar um estado
def adicionar_produto(nome_produto):
    if nome_produto not in produtos:
        produtos.append(nome_produto)
        print(f"Estado '{nome_produto}' adicionado com sucesso.")
    else:
        print(f"O estado '{nome_produto}' já existe.")

# Função para remover um estado
def remover_estado(nome_produto):
    if nome_produto in produtos:
        produtos.remove(nome_produto)
        print(f"Estado '{nome_produto}' removido com sucesso.")
    else:
        print(f"O estado '{nome_produto}' não existe na lista.")

# Função para contar o número de estados
def contar_produtos():
    return len(produtos)  # Retorna o total de estados

# Função para imprimir todos os estados
def imprimir_produtos():
    if produtos:
        print("produtos:")
        for produto in produtos:
            print(f"- {produto}")
    else:
        print("Não há estados para exibir.")

# Exemplo de uso das funções
if __name__ == "__main__":  # Isso só será executado se o script for executado diretamente
    adicionar_produto("Bahia")
    adicionar_produto("Minas Gerais")
    adicionar_produto("São Paulo")
    adicionar_produto("Recife")

    adicionar_produto("Rio de Janeiro")
    imprimir_produtos()
    contar_produtos()
    remover_produto("Bahia")
    imprimir_produtos()
    contar_produtos()
