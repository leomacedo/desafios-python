# Problema: Dada uma lista de nomes com repetições, crie uma função que retorne uma lista com os nomes únicos, em ordem alfabética.



nomes = ["Leo", "Ana", "João", "Leo", "Ana", "Beatriz", "Carlos"]

def ordena_lista_sem_duplicata(lista):
    nomes_unicos = set(lista)
    return sorted(nomes_unicos)

print(ordena_lista_sem_duplicata(nomes))