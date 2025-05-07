# 🧩 Desafio – Super Vendedor do Mês
# Você recebeu um dicionário com o número de vendas realizadas por cada vendedor em um mês:

vendas = {
    'Lucia': 15,
    'Roberto': 22,
    'Amanda': 31,
    'João': 17,
    'Felipe': 31,
    'Clara': 25
}
# Tarefa 1: Encontre quem foi o(a) vendedor(a) com o maior número de vendas usando max() com key=.

# Tarefa 2 (extra): O que acontece se dois vendedores empatarem com o mesmo número de vendas? Qual deles aparece como vencedor?

# Tente responder e fazer um pequeno teste no código.


# Passo 1: Encontrar o maior número de vendas
maior_valor = max(vendas.values())

# Passo 2: Criar uma lista para armazenar os nomes dos empatados
empatados = []

# Passo 3: Verificar quem tem esse número de vendas
for nome, qtd in vendas.items():
    if qtd == maior_valor:
        empatados.append(nome)

# Passo 4: Exibir os nomes e a quantidade
print(f"\nEsses vendedores empataram com {maior_valor} vendas:")
for nome in empatados:
    print(f"- {nome}")
#Resposta para a Tarefa 2: A Amanda apareceu como vencedor. Mas há um empate.