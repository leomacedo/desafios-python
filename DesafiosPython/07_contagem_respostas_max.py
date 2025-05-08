# 04/05/2025
# Enunciado:
# Você recebeu uma lista com o nome de alunos que responderam a uma pesquisa. Alguns nomes aparecem mais de uma vez, porque alguns alunos responderam mais de uma vez (espertinhos!).

# Seu desafio é criar uma função que conte quantas vezes cada aluno respondeu e depois diga quem respondeu mais vezes.


# Lista de respostas dos alunos
respostas = ['Ana', 'Carlos', 'Ana', 'João', 'Maria', 'João', 'Ana']

# Dicionário para armazenar a contagem de respostas de cada aluno
contagem = {}

# Contando quantas vezes cada nome aparece usando o método .get()
for nome in respostas:
    # O método .get(nome, 0) retorna o valor da chave se ela existir, ou 0 se não existir
    contagem[nome] = contagem.get(nome, 0) + 1

# Mostrando a contagem de respostas por aluno
for nome, quantidade in contagem.items():
    print(f"{nome}: {quantidade} vez(es)")

# Descobrindo quem respondeu mais vezes, usando o método max() do dicionário
# O max() encontra o maior valor, baseado na função chave 'contagem.get'
maior_frequencia = max(contagem, key=contagem.get)

# Exibindo o nome com mais respostas e a quantidade
print(f"\n{maior_frequencia} foi a pessoa que respondeu mais vezes: {contagem[maior_frequencia]} vezes")
