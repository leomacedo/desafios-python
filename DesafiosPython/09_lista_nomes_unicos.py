# 07/05/2025
# 🧩 Desafio – Lista de Nomes Únicos em Ordem Alfabética

# Problema: Dada uma lista de nomes com repetições,
# crie uma função que retorne uma lista com os nomes únicos, em ordem alfabética.

nomes = ["Leo", "Ana", "João", "Leo", "Ana", "Beatriz", "Carlos"]

def ordena_lista_sem_duplicata(lista):
    # Remove duplicatas transformando em conjunto (set)
    nomes_unicos = set(lista)
    # Retorna a lista ordenada alfabeticamente
    return sorted(nomes_unicos)

# Chamada da função e exibição do resultado
print(ordena_lista_sem_duplicata(nomes))
