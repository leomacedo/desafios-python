# 16/04/2025
# 🧪 Desafio: Calculadora de Médias com Listas

# Objetivo:
# Criar um programa que peça ao usuário quantas notas quer adicionar,
# colete essas notas em uma lista, calcule a média e informe a situação do aluno:
# "Aprovado", "Recuperação" ou "Reprovado", conforme a média final.

# Solicita ao usuário quantas notas ele deseja informar
notas_aluno = int(input("Quantas notas quer adicionar? "))

# Cria uma lista vazia para armazenar as notas
lista_notas = []

# Loop para coletar as notas com base na quantidade informada
for i in range(notas_aluno):
    nota = input(f"\nQual é a nota de número {i+1}?: ")
    lista_notas.append(float(nota))  # Converte a nota para float e adiciona à lista

# Calcula a média das notas usando sum() e len()
media = sum(lista_notas) / len(lista_notas)

# Exibe todas as notas digitadas
print(f"\nTodas as notas: {lista_notas}")

# Verifica a média e imprime a situação do aluno
if media >= 7:
    print(f"\n✅ Aluno aprovado com média: {media:.2f}")
elif media >= 5:
    print(f"\n⚠️ Aluno em recuperação com média: {media:.2f}")
else:
    print(f"\n❌ Aluno reprovado com média: {media:.2f}")
