# 04/05/2025
# Enunciado:
# Você recebeu uma lista com o nome de alunos que responderam a uma pesquisa. Alguns nomes aparecem mais de uma vez, porque alguns alunos responderam mais de uma vez (espertinhos!).

# Seu desafio é criar uma função que conte quantas vezes cada aluno respondeu e depois diga quem respondeu mais vezes.


# Lista de respostas dos alunos
respostas = ['Ana', 'Carlos', 'Ana', 'João', 'Maria', 'João', 'Ana']

# Dicionário para armazenar a contagem de respostas de cada aluno
contagem = {}

# Contando quantas vezes cada nome aparece na lista
for nome in respostas:
    # Se o nome já está no dicionário, aumente a contagem
    if nome in contagem:
        contagem[nome] += 1
    # Se o nome não está no dicionário, adicione ele com contagem 1
    else:
        contagem[nome] = 1

# Mostrando o total de respostas por aluno
for nome, quantidade in contagem.items():
    print(f"{nome}: {quantidade} vez(es)")

# Descobrindo quem respondeu mais vezes
maior_frequencia = ""  # Inicializa a variável para o nome com maior frequência
maior_quantidade = 0   # Inicializa a variável para a quantidade de respostas

# Verificando qual nome tem a maior contagem
for nome, quantidade in contagem.items():
    # Se a quantidade de respostas for maior que a atual, atualize as variáveis
    if quantidade > maior_quantidade:
        maior_frequencia = nome
        maior_quantidade = quantidade

# Exibindo o resultado final: quem respondeu mais vezes
print(f"\n{maior_frequencia} foi a pessoa que respondeu mais vezes: {maior_quantidade} vezes")