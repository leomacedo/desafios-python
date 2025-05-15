# 15/05/2025

# Importa bibliotecas: 'os' para comandos do sistema e 'time' para pausas
import os
import time

# Função que limpa a tela do terminal, compatível com Windows e Unix
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função que exibe o cabeçalho principal do programa
def exibir_cabecalho():
    print("🎓 CALCULADORA DE MÉDIAS ESCOLARES 🎓")
    print("-" * 40)

# Função que limpa a tela e exibe novamente o cabeçalho (evita repetição de código)
def reiniciar_tela_com_cabecalho():
    limpar_tela()
    exibir_cabecalho()

# Função genérica para obter um número válido do usuário
# Pode ser usada para inteiros ou floats, com validação personalizada
def obter_numero_valido(prompt, tipo=float, condicao=lambda x: True, mensagem_erro="Entrada inválida. Tente novamente."):
    while True:
        try:
            # Tenta converter a entrada para o tipo desejado
            valor = tipo(input(prompt))
            # Se a condição for satisfeita, retorna o valor
            if condicao(valor):
                return valor
            else:
                # Se não, limpa a tela, mostra o cabeçalho e exibe a mensagem de erro
                reiniciar_tela_com_cabecalho()
                print(mensagem_erro)
        except ValueError:
            # Caso ocorra erro na conversão, reinicia tela e mostra erro
            reiniciar_tela_com_cabecalho()
            print(mensagem_erro)

# Função principal do programa
def main():
    # Limpa a tela e exibe o cabeçalho
    reiniciar_tela_com_cabecalho()

    # Solicita o nome do aluno e formata com a primeira letra maiúscula
    nome_aluno = input("Informe o nome do aluno: ").strip().title()

    # Pergunta quantas matérias serão avaliadas, com validação
    qtd_materias = obter_numero_valido(
        "Quantas matérias serão avaliadas? ",
        tipo=int,
        condicao=lambda x: x > 0,
        mensagem_erro="Digite um número inteiro positivo."
    )

    # Listas para armazenar nomes das matérias e suas respectivas notas
    materias = []
    notas = []

    # Loop para entrada das matérias e notas
    for i in range(qtd_materias):
        reiniciar_tela_com_cabecalho()
        print(f"Matéria {i + 1} de {qtd_materias}")
        
        # Entrada e formatação do nome da matéria
        materia = input("Nome da matéria: ").strip().title()

        # Entrada da nota com validação entre 0 e 10
        nota = obter_numero_valido(
            f"Nota de {materia}: ",
            tipo=float,
            condicao=lambda x: 0 <= x <= 10,
            mensagem_erro="Digite uma nota entre 0 e 10."
        )

        # Armazena os dados nas listas
        materias.append(materia)
        notas.append(nota)

    # Calcula a média final
    media = sum(notas) / qtd_materias

    # Exibe o resultado final na tela
    limpar_tela()
    print("📋 RESULTADO FINAL")
    print("-" * 40)
    print(f"Aluno: {nome_aluno}")
    print("Notas:")

    # Lista cada matéria com sua nota correspondente
    for mat, nt in zip(materias, notas):
        print(f" - {mat}: {nt}")

    # Mostra a média formatada com duas casas decimais
    print(f"\n🧮 Média final: {media:.2f}")

    # Avalia a situação do aluno com base na média
    if media >= 7:
        print("✅ Situação: Aprovado!")
    elif media >= 5:
        print("⚠️ Situação: Recuperação.")
    else:
        print("❌ Situação: Reprovado.")

    print("-" * 40)
    print("Fim do programa.")
    
    # Pausa de 2 segundos antes de encerrar
    time.sleep(2)

# Ponto de entrada do programa
if __name__ == "__main__":
    main()
