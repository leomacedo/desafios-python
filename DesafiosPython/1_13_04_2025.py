# 🧩 Desafio extra para amanhã (nível: criativo e prático)
# Desafio: Criar uma agenda simples de 3 compromissos com listas!

# ✅ Peça para o usuário digitar 3 compromissos e armazene em uma lista
# ✅ Depois, imprima a agenda do dia com uma mensagem para cada compromisso (use for!)
# ✅ Extra: use \n e f-strings pra deixar bonito!



# Programa: Agenda de Compromissos 🗓️

# Criando lista vazia
agenda = []

# Coletando 3 compromissos
for i in range(3):
    compromisso = input(f"Digite o {i+1}º compromisso do dia: ")
    agenda.append(compromisso)

# Exibindo a agenda com estilo
print("\n📅 Sua agenda de hoje:")
for i in range(3):
    print(f"{i+1}️⃣  - {agenda[i]}")


print("\n✨ Que seu dia seja produtivo!")
