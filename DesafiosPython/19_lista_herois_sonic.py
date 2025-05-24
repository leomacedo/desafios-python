# 23/05/2025

# Conteúdo para treinar indexação negativa slice e comando del

# Há uma lista de hérois e vamos fazer 6 tarefas manipulando a lista:
herois = ["Sonic", "Tails", "Knuckles", "Shadow", "Silver", "Amy", "Espio"]

# Criada uma função de exibição
def exibicao_de_listas(mensagem, lista):
    print(f"\n{mensagem}")
    print(", ".join(lista))

# 0- Lista de heróis original:
exibicao_de_listas("Nossos heróis: ", herois)

# 1- Acesse o último herói da lista usando indexação negativa e imprima:
print(f"\nO último herói é: {herois[-1]}")

# 2- Crie uma nova lista chamada velocistas contendo apenas os 3 primeiros heróis.
velocistas = herois[:3]
exibicao_de_listas("Os velocistas: ", velocistas)

# 3- Crie outra lista chamada ultimos_herois contendo os 3 últimos nomes da lista original, usando slice com step negativo.
ultimos_herois = herois[-1:-4:-1]
exibicao_de_listas("Os ultimos hérois: ", ultimos_herois)

# 4- Remova o segundo herói da lista original com del.
del herois[1]

# 5- Imprima a lista original atualizada após a exclusão.
exibicao_de_listas("Lista original depois da exclusão do segundo herói: ", herois)

# 6- Inverta a lista original com slice e imprima.
exibicao_de_listas("Lista original invertida: ", herois[::-1])

# 7- Faça uma lista com os nomes dos hérois invertidos
invertidos = [nome[::-1] for nome in herois]
exibicao_de_listas("Nomes invertidos: ", invertidos)

