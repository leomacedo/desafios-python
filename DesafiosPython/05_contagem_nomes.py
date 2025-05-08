# 02/05/2025
# Contexto:
# Você tem uma lista com os nomes dos membros da torcida que interagiram num tweet. Você quer criar uma função que:

# Conta quantas vezes um nome aparece.

# Retorna se um nome aparece mais de uma vez.

# Usa um for loop dentro de uma função.

# Usa uma variável global para contar quantos nomes repetidos existem.

# Lista de nomes dos membros da torcida
nomes = ['Ana', 'João', 'Ana', 'Maria', 'João', 'Ana', 'Carlos', 'Maria']

# Função que conta quantas vezes um nome aparece na lista
def contar_nome(lista, nome_lista):
    contador = 0
    for nome in lista:
        if nome == nome_lista:  # Se o nome na lista for igual ao nome procurado
            contador += 1  # Aumenta o contador
    return contador  # Retorna o número de vezes que o nome apareceu

# Função que lista todos os nomes e quantas vezes eles aparecem
def lista_nomes():
    nomes_contados = []  # Lista para armazenar os nomes já processados
    for nome in nomes:
        if nome not in nomes_contados:  # Verifica se o nome já foi contado
            quantidade = contar_nome(nomes, nome)  # Conta a ocorrência do nome
            print(f"{nome} : {quantidade} vez(es)")  # Exibe o nome e sua quantidade de ocorrências
            nomes_contados.append(nome)  # Adiciona o nome à lista de contados para não contar mais de uma vez

# Função que encontra o nome que mais aparece na lista
def nome_mais(lista):
    mais_frequente = ""  # Nome mais frequente, inicialmente vazio
    maior_contagem = 0  # Contagem inicial
    nomes_contados = []  # Lista para armazenar os nomes já processados

    for nome in lista:
        if nome not in nomes_contados:  # Verifica se o nome já foi contado
            contagem = contar_nome(lista, nome)  # Conta as ocorrências desse nome
            if contagem > maior_contagem:  # Se for mais frequente que o anterior
                mais_frequente = nome  # Atualiza o nome mais frequente
                maior_contagem = contagem  # Atualiza a maior contagem
            nomes_contados.append(nome)  # Adiciona o nome à lista de contados

    print(f"\nO nome que mais aparece é {mais_frequente} ({maior_contagem} vezes).")

# Outra versão para encontrar o nome mais frequente, usando o método count()
def nome_mais2(lista):
    nome_mais_frequente = ""  # Nome mais frequente, inicialmente vazio
    maior_quantidade = 0  # Contagem inicial
    nomes_contados = []  # Lista para armazenar os nomes já processados

    for nome in lista:
        if nome not in nomes_contados:  # Verifica se o nome já foi contado
            contagem = lista.count(nome)  # Conta as ocorrências do nome usando o método count()
            if contagem > maior_quantidade:  # Se for mais frequente que o anterior
                nome_mais_frequente = nome  # Atualiza o nome mais frequente
                maior_quantidade = contagem  # Atualiza a maior quantidade
            nomes_contados.append(nome)  # Adiciona o nome à lista de contados

    print(f"\nO nome que mais aparece é {nome_mais_frequente} ({maior_quantidade} vezes).")

# Para rodar as funções, descomente as linhas abaixo:
# lista_nomes()
# nome_mais(nomes)
# nome_mais2(nomes)



# Explicação do Código:

# Função contar_nome(): Conta quantas vezes um nome específico aparece na lista.

# Função lista_nomes(): Lista todos os nomes e quantifica suas ocorrências, sem repetir.

# Função nome_mais(): Encontra o nome mais frequente, utilizando a função contar_nome().

# Função nome_mais2(): Outra forma de encontrar o nome mais frequente, mas usando o método count() para contar as ocorrências diretamente na lista.