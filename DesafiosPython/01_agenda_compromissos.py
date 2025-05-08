# 13/04/2025
# 🧩 Desafio extra para amanhã (nível: criativo e prático)
# Desafio: Criar uma agenda simples de 3 compromissos com listas!

# ✅ Peça para o usuário digitar 3 compromissos e armazene em uma lista
# ✅ Depois, imprima a agenda do dia com uma mensagem para cada compromisso (use for!)
# ✅ Extra: use \n e f-strings pra deixar bonito!


# Criando uma lista vazia para armazenar os compromissos
agenda = []

# Coletando 3 compromissos do usuário e armazenando na lista
for i in range(3):
    compromisso = input(f"Digite o {i+1}º compromisso do dia: ")
    agenda.append(compromisso)

# Exibindo a agenda do dia com uma mensagem para cada compromisso
print("\n📅 Sua agenda de hoje:")
for i in range(3):
    print(f"{i+1}️⃣  - {agenda[i]}")

# Mensagem final para desejar um bom dia de compromissos
print("\n✨ Que seu dia seja produtivo!")
