# 💡 Mini-desafio Extra — Listas e for com criatividade!
# Você vai criar um mini-programa que faz o seguinte:

# 💬 Descrição:
# Pergunta ao usuário quantos nomes ele quer adicionar;

# Usa um laço for para pedir que ele digite os nomes e vá adicionando em uma lista com append;

# Depois, imprime uma frase personalizada para cada nome da lista, como por exemplo:

import random

# Lista de mensagens
expressões = ["Seja bem-vindo(a)!", "Que bom te ver!" , "Sinta-se em casa!"]

# Lista de nomes
lista = []

# Coletando a quantidade
quantidade = int(input("Quantos nomes você quer adicionar?"))

# Preenchendo a lista com os nomes
for i in range(quantidade):
    nome = input(f"Digite o {i+1}º nome: ")
    lista.append(nome)

# Exibindo mensagens personalizadas
print("\n🎉 Mensagens personalizadas:")
for i,nome in enumerate(lista, start =1):
    mensagem = random.choice(expressões)
    print(f"Nome {i}: {nome} - {mensagem}")


