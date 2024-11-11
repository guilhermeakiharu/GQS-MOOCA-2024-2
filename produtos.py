# estado.py

# Lista para armazenar os produtos
produtos = []

# Função para adicionar um produto
def adicionar_produto(nome_produto):
    if nome_produto not in produtos:
        produtos.append(nome_produto)
        print(f"Produto '{nome_produto}' adicionado com sucesso.")
    else:
        print(f"O produto '{nome_produto}' já existe.")

# Função para remover um produto
def remover_produto(nome_produto):
    if nome_produto in produtos:
        produtos.remove(nome_produto)
        print(f"Produto '{nome_produto}' removido com sucesso.")
    else:
        print(f"O produto '{nome_produto}' não existe na lista.")

# Função para contar o número de produtos
def contar_produtos():
    return len(produtos)  # Retorna o total de produtos

# Função para imprimir todos os produtos
def imprimir_produtos():
    if produtos:
        print("Produtos:")
        for produto in produtos:
            print(f"- {produto}")
    else:
        print("Não há produtos para exibir.")

# Exemplo de uso das funções
if __name__ == "__main__":  # Isso só será executado se o script for executado diretamente
    adicionar_produto("Broca")
    adicionar_produto("Tijolo")
    adicionar_produto("Porta")
    adicionar_produto("Cimento")
    adicionar_produto("Azulejo")
    
    imprimir_produtos()
    print(f"Total de produtos: {contar_produtos()}")
    remover_produto("Broca")
    imprimir_produtos()
    print(f"Total de produtos: {contar_produtos()}")
