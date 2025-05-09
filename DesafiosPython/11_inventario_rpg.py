# Data: 09/05/2025
# Sistema de inventário de um jogo de RPG.
# O inventário armazena os itens carregados pelo jogador e gera informações úteis.

itens_coletados = (
    "Poção de Vida", "Espada de Ferro", "Poção de Vida",
    "Escudo de Madeira", "Poção de Mana", "Poção de Vida",
    "Espada de Ferro", "Arco Curto", "Poção de Mana"
)

precos_itens = {
    "Poção de Vida": 50,
    "Poção de Mana": 40,
    "Espada de Ferro": 200,
    "Escudo de Madeira": 150,
    "Arco Curto": 100
}

# Tarefa 1: Contar quantas vezes cada item aparece
# Criação de um dicionário de contagem
contagem = {}
for item in itens_coletados:
    # O método .get(nome, 0) retorna o valor da chave se ela existir, ou 0 se não existir
    contagem[item] = contagem.get(item, 0) + 1
# Mostrando o total de itens de cada item coletado
for item, quantidade in contagem.items():
    print(f"{item}: {quantidade} vez(es)")

# Tarefa 2: Criar um conjunto com os itens únicos
# Transformando a tupla em um conjunto.
itens_unicos = set(itens_coletados)
print(f"\nItens únicos: {itens_unicos}")

# Tarefa 3: Calcular o valor total do inventário
# Dica: Quero saber o valor total dos itens → Preciso multiplicar preço pela quantidade de cada um → Preço tá no dicionário A, quantidade no dicionário B 
# → Então percorro um deles e busco no outro.
# Valor total dos itens.
valor_total = 0
for item, quantidade in contagem.items():
    preco = precos_itens[item]
    valor_total += preco * quantidade
print(f"\nValor total do inventário: {valor_total} moedas")

# Tarefa 4: Mostrar o dicionário com item e quantidade
# Já tinha feito o dicionário na tarefa 1 na variável contagem
print(f"\nDicionário de contagem: {contagem}")

# Tarefa 5: Listagem detalhada do inventário
# Percorrendo o Dicionário A e pegando um valor do dicionário B. Quase mesma lógica da Tarefa 3
print("\nListagem detalhada do inventário:")
for item, quantidade in contagem.items():
    preco_total = precos_itens[item] * quantidade
    print(f"{item} - Quantidade: {quantidade} - Valor Total: {preco_total} moedas")
