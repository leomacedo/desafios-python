# 04/05/2025
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

# Tarefa 1: Encontre quem foi o(a) vendedor(a) com o maior número de vendas usando max() com key=
maior_vendedor = max(vendas, key=vendas.get)
print(f"Vendedor com mais vendas (usando max + key): {maior_vendedor} - {vendas[maior_vendedor]} vendas")

# Tarefa 2 (extra): Testar empate
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

# 📝 Resposta para a Tarefa 2:
# Usando apenas max(vendas, key=vendas.get), o Python retorna o primeiro nome que aparece com o maior valor,
# ou seja, Amanda. Mas ao verificar manualmente, vemos que Felipe também teve 31 vendas.
