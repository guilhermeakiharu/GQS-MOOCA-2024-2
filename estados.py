# estado.py

# Lista para armazenar os estados
estados = []

# Função para adicionar um estado
def adicionar_estado(nome_estado):
    if nome_estado not in estados:
        estados.append(nome_estado)
        print(f"Estado '{nome_estado}' adicionado com sucesso.")
    else:
        print(f"O estado '{nome_estado}' já existe.")

# Função para remover um estado
def remover_estado(nome_estado):
    if nome_estado in estados:
        estados.remove(nome_estado)
        print(f"Estado '{nome_estado}' removido com sucesso.")
    else:
        print(f"O estado '{nome_estado}' não existe na lista.")

# Função para contar o número de estados
def contar_estados():
    return len(estados)  # Retorna o total de estados

# Função para imprimir todos os estados
def imprimir_estados():
    if estados:
        print("Estados:")
        for estado in estados:
            print(f"- {estado}")
    else:
        print("Não há estados para exibir.")

# Exemplo de uso das funções
if __name__ == "__main__":  # Isso só será executado se o script for executado diretamente
    adicionar_estado("Bahia")
    adicionar_estado("São Paulo")
    adicionar_estado("Rio de Janeiro")
    imprimir_estados()
    contar_estados()
    remover_estado("Bahia")
    imprimir_estados()
    contar_estados()
