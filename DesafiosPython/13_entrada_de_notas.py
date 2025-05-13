# 13/05/2025
# Desafio 13 - Validação e análise estatística de notas de alunos
# Este programa solicita ao usuário uma lista de notas (de 0 a 10), separadas por espaço.
# Ele valida as entradas, filtra valores inválidos e, caso tenha entradas válidas,
# exibe estatísticas como média, maior e menor nota.

import statistics as stat  # Importa a biblioteca statistics para cálculos como média
import sys  # Importa a biblioteca sys para poder encerrar o programa com sys.exit()

# Loop principal que garante que o usuário só saia quando inserir pelo menos uma nota válida
while True:
    # Entrada do usuário com instruções claras
    notas = input("Digite uma lista de notas de um aluno separados por espaço: ")

    # Separa os valores digitados com base nos espaços e gera uma lista de itens
    itens = notas.split()

    notas_validas = []         # Lista que vai armazenar apenas notas válidas (entre 0 e 10)
    entradas_invalidas = 0     # Contador de entradas inválidas

    # Percorre cada item digitado
    for item in itens:
        try:
            # Tenta converter o item para float
            nota = float(item)
            
            # Verifica se está dentro da faixa permitida (0 a 10)
            if nota < 0 or nota > 10:
                print(f"⚠️  Atenção: '{nota}' não é uma nota válida e será ignorada. Ela precisa estar entre 0 a 10")
                entradas_invalidas += 1  
            else:
                notas_validas.append(nota)  # Nota válida é adicionada à lista
        except ValueError:
            # Caso o item não seja um número (ex: letra ou símbolo), o erro é tratado aqui
            print(f"⚠️  Atenção: '{item}' não é uma nota válida e será ignorada.")
            entradas_invalidas += 1

    # Caso nenhuma nota válida tenha sido inserida
    if not notas_validas:
        print(f"\nQuantidade de entradas inválidas: {entradas_invalidas}")
        print("❌ Nenhuma nota válida foi registrada.")
        repetir = input("Deseja tentar novamente? (s/n): ").lower()

        # Se o usuário não quiser tentar de novo, o programa encerra aqui
        if repetir != 's':
            print("Programa encerrado. Até logo!")
            sys.exit()
    else:
        break  # Sai do loop porque pelo menos uma nota válida foi registrada

# Essa parte só será executada se houver pelo menos uma nota válida

# Exibe as quantidades de entradas válidas e inválidas
print(f"\nQuantidade de entradas inválidas: {entradas_invalidas}")
print(f"Quantidade de entradas válidas: {len(notas_validas)}")

# Exibe a lista de notas válidas em ordem crescente
print(f"\nLista de notas registradas: {sorted(notas_validas)}")

# Calcula e exibe os dados estatísticos das notas
media = stat.mean(notas_validas)
maxima = max(notas_validas)
minima = min(notas_validas)

print(f"Média geral: {media: .2f}")
print(f"Máxima nota: {maxima}")
print(f"Mínima nota: {minima}")
