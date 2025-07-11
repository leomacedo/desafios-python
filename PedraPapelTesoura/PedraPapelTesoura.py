import random
import os

opcoes = {1: "✊ Pedra", 2: "✋ Papel", 3: "✌️  Tesoura"}
placar_jogador = 0
placar_computador = 0

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

nome_jogador = input("Digite seu nome para começar: ")

def exibir_placar(tipo):
        print(f"\nPlacar {tipo}:")
        print(f"{nome_jogador}: {placar_jogador} | Computador: {placar_computador}")

while True:
    limpar_tela()    
    print("\nEscolha sua jogada:")
    print("1 - ✊ Pedra")
    print("2 - ✋ Papel")
    print("3 - ✌️  Tesoura")
    print("9 - ❌ Sair do jogo")

    exibir_placar("parcial")

    while True:
        jogador = input("\nDigite o número da sua jogada: ")
        if jogador in ["1", "2", "3", "9"]:
            jogador = int(jogador)
            break
        else:
            print("❌ Jogada inválida. Tente novamente.")

    if jogador == 9:
        print(f"\nObrigado por jogar {nome_jogador}! Até a próxima 👋")
        exibir_placar("final")
        if placar_jogador == placar_computador:
            print("\nO jogo terminou empatado!")
        elif placar_jogador > placar_computador:
            print("\nParabéns! Você ganhou!")
        else:
            print("\nVocê perdeu! Melhor sorte na próxima!")
        break

    # Escolha aleatória do computador
    computador = random.choice([1, 2, 3])

    # Mostrar a escolha em texto
    print(f"\n{nome_jogador} escolheu: {opcoes[jogador]}")
    print(f"O computador escolheu: {opcoes[computador]}")


    # Lógica do jogo
    if jogador == computador:
        print("\n🤝 Deu empate!")
    elif (jogador == 1 and computador == 3) or \
        (jogador == 2 and computador == 1) or \
        (jogador == 3 and computador == 2):
        print(f"\n🏆 {nome_jogador} vence!")
        placar_jogador +=1
    else:
        print("\n💻 Computador vence!")
        placar_computador +=1

    input("\nPressione Enter para continuar...")

