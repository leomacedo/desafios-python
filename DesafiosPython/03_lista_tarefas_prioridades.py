# 15/04/2025
# 💼 Desafio 3: Lista de Tarefas com Prioridades

# Este programa permite ao usuário adicionar tarefas com níveis de prioridade
# (Alta, Média ou Baixa), e depois exibe as tarefas organizadas por categoria.

# Pergunta quantas tarefas o usuário deseja adicionar
quantidade = int(input("Quantas tarefas deseja adicionar? "))

# Lista para armazenar as tarefas com suas prioridades
tarefas = []

# Coletando as tarefas e suas prioridades
for i in range(quantidade):
    nome = input(f"\nDigite o nome da tarefa {i+1}: ")

    # Loop para garantir uma prioridade válida
    while True:
        prioridade = input("Qual a prioridade dela? 1 - Alta | 2 - Média | 3 - Baixa: ")
        if prioridade in ["1", "2", "3"]:
            break
        else:
            print("❌ Prioridade inválida. Tente novamente.")
    
    # Armazena como tupla: (nome da tarefa, prioridade numérica)
    tarefas.append((nome, int(prioridade)))

# Separando as tarefas por prioridade
alta = []
media = []
baixa = []

for nome, prioridade in tarefas:
    if prioridade == 1:
        alta.append(nome)
    elif prioridade == 2:
        media.append(nome)
    elif prioridade == 3:
        baixa.append(nome)

# Exibindo os resultados organizados
print("\n📌 Tarefas com Prioridade Alta:")
for nome in alta:
    print(f"- {nome}")

print("\n📋 Tarefas com Prioridade Média:")
for nome in media:
    print(f"- {nome}")

print("\n🛋️ Tarefas com Prioridade Baixa:")
for nome in baixa:
    print(f"- {nome}")

