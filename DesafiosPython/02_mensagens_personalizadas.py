# 14/04/2025
# 💡 Mini-desafio Extra — Listas e for com criatividade!
# Você vai criar um mini-programa que faz o seguinte:

# 💬 Descrição:
# Pergunta ao usuário quantos nomes ele quer adicionar;

# Usa um laço for para pedir que ele digite os nomes e vá adicionando em uma lista com append;

# Depois, imprime uma frase personalizada para cada nome da lista, como por exemplo:

import random

# Lista de mensagens personalizadas para os nomes
expressões = ["Seja bem-vindo(a)!", "Que bom te ver!", "Sinta-se em casa!"]

# Lista para armazenar os nomes digitados pelo usuário
lista = []

# Perguntando quantos nomes o usuário quer adicionar
quantidade = int(input("Quantos nomes você quer adicionar?"))

# Coletando os nomes do usuário e adicionando na lista
for i in range(quantidade):
    nome = input(f"Digite o {i+1}º nome: ")
    lista.append(nome)

# Exibindo uma mensagem personalizada para cada nome da lista
print("\n🎉 Mensagens personalizadas:")
for i, nome in enumerate(lista, start=1):
    mensagem = random.choice(expressões)  # Escolhe uma mensagem aleatória da lista
    print(f"Nome {i}: {nome} - {mensagem}")


