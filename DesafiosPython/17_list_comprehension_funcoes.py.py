# 21/05/2025

# Lista base utilizada nos dois desafios
lista = [1, 2, 3, 4, 5, 6, 7]

def dobro_dos_impares(lista):
    """
    Função que retorna uma nova lista com o dobro apenas dos números ímpares da lista original.
    Utiliza list comprehension com um filtro condicional (if).
    """
    return [
        num * 2 for num in lista 
        if num % 2 != 0  # Filtra apenas os ímpares
    ]

def imparx3_parmenos1(lista):
    """
    Função que modifica cada elemento da lista:
    - Se for ímpar, multiplica por 3.
    - Se for par, subtrai 1.
    Utiliza list comprehension com if/else inline.
    """
    return [
        num * 3 if num % 2 != 0 else num - 1 
        for num in lista
    ]

# Execução das funções e impressão dos resultados
resultado = dobro_dos_impares(lista)
resultado2 = imparx3_parmenos1(lista)

print("Dobro dos ímpares:", resultado)
print("Ímpares x3 | Pares -1:", resultado2)
