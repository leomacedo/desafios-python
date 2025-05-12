# 12/05/2025
# Importa funções e módulos para cálculos matemáticos e estatísticos
import math
import statistics as stat
from math import sqrt as raiz

numeros = input("Digite uma lista de números separados por espaço: ")
# Separa os números digitados usando o espaço como delimitador
itens = numeros.split()

# Validação básica de números
lista_numeros = []
# Tenta converter cada item em número float; ignora o que não for número
for item in itens:
    try:
        numero = float(item)
        lista_numeros.append(numero)
    except ValueError:
        print(f"⚠️  Atenção: '{item}' não é um número válido e será ignorado.")

# Verifica se a lista tem elementos válidos
if not lista_numeros:
    print("❌ Nenhum número válido foi digitado. Encerrando o programa.")
# Garante que há ao menos um número válido antes de prosseguir com os cálculos
else:
    print(f"Números válidos: {lista_numeros}")

    # Calcula e exibe a média dos números
    media = stat.mean(lista_numeros)
    print(f"Média: {media:.2f}")

    # Calcula e exibe a mediana dos números
    mediana = stat.median(lista_numeros)
    print(f"Mediana: {mediana:.2f}")

    # Calcula e exibe o desvio padrão (se houver mais de um número)
    desvio = stat.stdev(lista_numeros) if len(lista_numeros) > 1 else 0
    print(f"Desvio padrão: {desvio:.2f}")

    menor_num = min(lista_numeros)
    maior_num = max(lista_numeros)

    raiz_quadrada = raiz(maior_num)
    print(f"Raiz quadrada do maior número ({maior_num}): {raiz_quadrada:.2f}")

    # Verifica se o menor número é um inteiro positivo antes de calcular o fatorial
    if menor_num.is_integer() and menor_num >= 0:
        fatorial = math.factorial(int(menor_num))
        print(f"Fatorial do menor número ({int(menor_num)}): {fatorial}")
    else:
        print(f"O Fatorial do menor número ({menor_num}) não pode ser calculado pois não é um inteiro positivo.")
