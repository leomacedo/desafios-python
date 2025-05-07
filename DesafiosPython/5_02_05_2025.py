# Contexto:
# Você tem uma lista com os nomes dos membros da torcida que interagiram num tweet. Você quer criar uma função que:

# Conta quantas vezes um nome aparece.

# Retorna se um nome aparece mais de uma vez.

# Usa um for loop dentro de uma função.

# Usa uma variável global para contar quantos nomes repetidos existem.

nomes = ['Ana', 'João', 'Ana', 'Maria', 'João', 'Ana', 'Carlos', 'Maria']

def contar_nome(lista, nome_lista):
    contador = 0
    for nome in lista:
        if nome == nome_lista:
            contador += 1
    return contador

def lista_nomes():
    nomes_contados = []
    for nome in nomes:
        if nome not in nomes_contados:
            quantidade = contar_nome(nomes, nome)
            print(f"{nome} : {quantidade} vez(es)")
            nomes_contados.append(nome)

def nome_mais(lista):
    mais_frequente = ""
    maior_contagem = 0
    nomes_contados = []

    for nome in lista:
        if nome not in nomes_contados:
            contagem = contar_nome(lista, nome)
            if contagem > maior_contagem:
                mais_frequente = nome
                maior_contagem = contagem
            nomes_contados.append(nome)

    print(f"\nO nome que mais aparece é {mais_frequente} ({maior_contagem} vezes).")

def nome_mais2(lista):
    nome_mais_frequente = ""
    maior_quantidade = 0
    nomes_contados = []

    for nome in lista:
        if nome not in nomes_contados:
            contagem = lista.count(nome)
            if contagem > maior_quantidade:
                nome_mais_frequente = nome
                maior_quantidade = contagem
            nomes_contados.append(nome)

    print(f"\nO nome que mais aparece é {nome_mais_frequente} ({maior_quantidade} vezes).")


# lista_nomes()
# nome_mais(nomes)
# nome_mais2(nomes)
