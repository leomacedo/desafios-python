# 02/06/2025
# Desafio 27 - Programação Orientada a Objetos numa batalha de RPG
# Este projeto simula uma batalha entre personagens com diferentes estilos de ataque
# Aplicando herança, polimorfismo, abstração, randomização!

import random      # Importa biblioteca para gerar valores aleatórios (nível, dano, etc)
import time        # Importa biblioteca para criar pausas
from abc import ABC, abstractmethod  # Importa suporte para classes abstratas

# Classe abstrata base: define atributos e métodos comuns para todos os personagens
class Personagem(ABC):
    def __init__(self, nome, level):
        self.nome = nome
        self.level = level
        self.vida = level * 10  # Vida é calculada com base no nível (ex: nível 7 = 70 de vida)

    def __str__(self):
        classe = self.__class__.__name__  # Pega o nome da subclasse (Guerreiro, Mago, Arqueiro)

        # Dicionário com emojis visuais para cada classe
        emojis = {
            "Guerreiro": "🗡️",
            "Mago": "🔮",
            "Arqueiro": "🏹",
        }

        # Pega o emoji correspondente ou ❓ se não encontrar
        emoji = emojis.get(classe, "❓")

        # Retorna uma string bonitona com todas as informações do personagem
        return f"{self.nome} | Level: {self.level} | Classe: {classe} {emoji}  | Vida: {self.vida} ❤️  "

    def receber_dano(self, dano):
        # Reduz a vida do personagem com base no dano recebido
        if self.vida > dano:
            self.vida -= dano
            print(f"{self.nome} recebeu {dano} de dano.\n{self.nome} tem {self.vida} ❤️  de pontos de vida.")
        else:
            self.vida = 0
            print(f"{self.nome} recebeu {dano} de dano.\n{self.nome} foi nocauteado! 💀 ")

    @abstractmethod
    def atacar(self, inimigo):
        # Método abstrato: será implementado pelas subclasses
        pass

# Classe Guerreiro: dano fixo de 10
class Guerreiro(Personagem):
    def __init__(self, nome, level):
        super().__init__(nome, level)

    def atacar(self, inimigo):
        dano = 10
        print(f"{self.nome} ataca 🗡️  {inimigo.nome}")
        inimigo.receber_dano(dano)

# Classe Mago: dano aleatório entre 5 e 15
class Mago(Personagem):
    def __init__(self, nome, level):
        super().__init__(nome, level)

    def atacar(self, inimigo):
        dano = random.randint(5, 15)  # Sorteia um valor entre 5 e 15
        print(f"{self.nome} ataca 🔮  {inimigo.nome}")
        inimigo.receber_dano(dano)

# Classe Arqueiro: dano fixo de 8 com 30% de chance de ataque crítico (x2)
class Arqueiro(Personagem):
    def __init__(self, nome, level):
        super().__init__(nome, level)

    def atacar(self, inimigo):
        dano = 8
        chance_critica = random.randint(1, 100)
        if chance_critica <= 30:
            dano *= 2
            print(f"{self.nome} acertou um ATAQUE CRÍTICO! Dano dobrado! 🏹🏹 ")

        print(f"{self.nome} ataca 🏹  {inimigo.nome}")
        inimigo.receber_dano(dano)

# Define os níveis aleatórios para cada personagem
levelguerreiro = random.randint(5, 10)
levelmago = random.randint(5, 10)
levelarqueiro = random.randint(5, 10)

# Criação dos personagens com seus níveis sorteados
personagens = [
    Guerreiro("Ryu", levelguerreiro),
    Mago("Nina", levelmago),
    Arqueiro("Bow", levelarqueiro)
]

# Escolhe aleatoriamente 2 personagens para batalhar
escolhidos = random.sample(personagens, 2)

# Função de batalha: alterna ataques até que um dos personagens seja derrotado
def batalha(personagem1, personagem2):
    print("\n🏁 A BATALHA COMEÇOU!")
    print(f"{personagem1.nome} VS {personagem2.nome}")
    print(f"{personagem1} \n{personagem2}\n")

    rodada = 1

    while personagem1.vida > 0 and personagem2.vida > 0:
        print(f"\n--- Rodada {rodada} ---")
        time.sleep(2)  # Pausa para criar suspense

        # Personagem 1 ataca
        personagem1.atacar(personagem2)
        if personagem2.vida <= 0:
            print(f"\n🏆 {personagem1.nome} venceu a batalha!")
            break
        time.sleep(2)
        print()

        # Personagem 2 ataca
        personagem2.atacar(personagem1)
        if personagem1.vida <= 0:
            print(f"\n🏆 {personagem2.nome} venceu a batalha!")
            break

        rodada += 1  # Próxima rodada

# Inicia a batalha entre os dois personagens escolhidos
batalha(escolhidos[0], escolhidos[1])
