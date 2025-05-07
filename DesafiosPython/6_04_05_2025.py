# Enunciado:
# Você recebeu uma lista com o nome de alunos que responderam a uma pesquisa. Alguns nomes aparecem mais de uma vez, porque alguns alunos responderam mais de uma vez (espertinhos!).

# Seu desafio é criar uma função que conte quantas vezes cada aluno respondeu e depois diga quem respondeu mais vezes.


#Solução 1

respostas = ['Ana', 'Carlos', 'Ana', 'João', 'Maria', 'João', 'Ana']

contagem = {}

# Contando quantas vezes cada nome aparece
for nome in respostas:
    if nome in contagem:
        contagem[nome] += 1
    else:
        contagem[nome] = 1

# Mostrando o total de respostas por aluno
for nome, quantidade in contagem.items():
    print(f"{nome}: {quantidade} vez(es)")

# Descobrindo quem respondeu mais vezes
maior_frequencia = ""
maior_quantidade = 0

for nome, quantidade in contagem.items():
    if quantidade > maior_quantidade:
        maior_frequencia = nome
        maior_quantidade = quantidade

print(f"\n{maior_frequencia} foi a pessoa que respondeu mais vezes: {maior_quantidade} vezes")



#Solução 2


# respostas = ['Ana', 'Carlos', 'Ana', 'João', 'Maria', 'João', 'Ana']

# contagem = {}

# # O método .get(nome, 0) retorna o valor da chave se ela existir, ou 0 se não existir
# for nome in respostas:
#     contagem[nome] = contagem.get(nome, 0) + 1

# # Mostrando a contagem
# for nome, quantidade in contagem.items():
#     print(f"{nome}: {quantidade} vez(es)")

# # Descobrindo o nome com mais repetições
# maior_frequencia = max(contagem, key=contagem.get)
# print(f"\n{maior_frequencia} foi a pessoa que respondeu mais vezes: {contagem[maior_frequencia]} vezes")
