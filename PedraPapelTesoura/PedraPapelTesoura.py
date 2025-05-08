import random

print("Escolha sua jogada:")
print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

while True:
    jogador = input("\nDigite o número da sua jogada: ")
    if jogador in ["1", "2", "3"]:
        jogador = int(jogador)
        break
    else:
        print("❌ Jogada inválida. Tente novamente.")

# Escolha aleatória do computador
sorteio = [1, 2, 3]
computador = random.choice(sorteio)

# Mostrar a escolha em texto
opcoes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}
print(f"\nVocê escolheu: {opcoes[jogador]}")
print(f"O computador escolheu: {opcoes[computador]}")
# Lógica do jogo
if jogador == computador:
    print("\nDeu empate!")
elif (jogador == 1 and computador == 3) or \
     (jogador == 2 and computador == 1) or \
     (jogador == 3 and computador == 2):
    print("\nJogador vence!")
else:
    print("\nComputador vence!")