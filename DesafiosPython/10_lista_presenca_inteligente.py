# 08/05/2025
# 🧠 Desafio: Lista de Presença Inteligente
# Você está ajudando na organização de um evento. Existem dois conjuntos:
# convidados: contém os nomes de todas as pessoas convidadas.
# presentes: contém os nomes das pessoas que compareceram.

# Crie um programa que:
# Mostre quem foi ao evento e estava realmente convidado.
# Mostre quem compareceu sem convite.

# Verifique se todos os convidados compareceram.


convidados = {"Alice", "Bruno", "Carla", "Davi"}
presentes = {"Bruno", "Davi", "Eva"}


# Presentes e convidados:
print(f"✅ Presentes e convidados: {convidados.intersection(presentes)}")

# Convidados presentes e sem convite
print(f"⚠️  Presentes sem convite: {presentes.difference(convidados)}")

# Condicional que verifica se todos os convidados apareceram.
compareceu = presentes.issubset(convidados)

if compareceu:
    print(f"✅ Todos os convidados estavam presentes")
else:
    print(f"❌ Nem todos os convidados compareceram")

