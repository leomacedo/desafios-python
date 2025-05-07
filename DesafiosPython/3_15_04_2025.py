# 💼 Desafio: Lista de tarefas com prioridades
# Crie um programa que:
# Pergunte quantas tarefas a pessoa quer adicionar.
# Para cada tarefa, peça:

# O nome da tarefa.
# A prioridade (Alta, Média ou Baixa).
# Armazene tudo numa lista de tuplas ou listas aninhadas.
# Depois, exiba a lista organizada por prioridade (pode só imprimir em blocos separados, não precisa ordenar ainda).

# Exemplo de saída:

# 📌 Tarefas com Prioridade Alta:
# - Estudar Python

# 📋 Tarefas com Prioridade Média:
# - Caminhar com os pais

# 🛋️ Tarefas com Prioridade Baixa:
# - Assistir BBB

confirm = False
tarefas = int(input("Quantas tarefas deseja adicionar? "))
lista_tupla = []
for i in range(tarefas):
    nome = input(f"Qual é a tarefa de numero {i+1}?: ")

    while True:
        prioridade = input("Qual prioridade dela? 1- Alta  2- Média  3- Baixa: ")
        if prioridade in ["1", "2", "3"]:
            break
        else:
            print("❌ Prioridade inválida. Tente novamente.")
    lista_tupla.append((nome, int(prioridade)))

# Agora vamos separar as listas:
alta = []
media = []
baixa = []

for tarefa in lista_tupla:
    nome, prioridade = tarefa
    if prioridade == 1:
        alta.append(nome)
    elif prioridade == 2:
        media.append(nome)
    elif prioridade == 3:
        baixa.append(nome)

# Exibindo os resultados:
print("\n📌 Tarefas com Prioridade Alta:")
for nome in alta:
    print(f"- {nome}")

print("\n📋 Tarefas com Prioridade Média:")
for nome in media:
    print(f"- {nome}")

print("\n🛋️ Tarefas com Prioridade Baixa:")
for nome in baixa:
    print(f"- {nome}")

