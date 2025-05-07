# 🧪 Desafio: Calculadora de Médias com Listas
# Crie um programa que:
# Pergunte ao usuário quantas notas ele quer adicionar.
# Peça cada nota (use um loop).
# Armazene as notas numa lista.
# Calcule e exiba a média.
# Diga se a pessoa está:
# "Aprovada" se a média for maior ou igual a 7.
# "Recuperação" se for entre 5 e 6.9.
# "Reprovada" se for menor que 5.
# Se quiser, posso te dar uma dica com estrutura de while e for, mas tenta do seu jeito primeiro 😉


notas_aluno = int(input("Quantas notas quer adicionar? "))

# Criada a lista de notas
lista_notas = []

# Preenchimento de notas
for i in range(notas_aluno):
    nota = input(f"\nQual é a nota de numero {i+1}?: ")
    lista_notas.append(float(nota))

# Calculo da média
media = sum(lista_notas) / len(lista_notas)


print(f"\nTodas as notas: {lista_notas}")

if media >= 7:
    print(f"\nAluno aprovado com média: {media}")
elif media >= 5:
    print(f"\nAluno em recuperação com média: {media}")
else:
    print(f"\nAluno reprovado com média: {media}")
    

