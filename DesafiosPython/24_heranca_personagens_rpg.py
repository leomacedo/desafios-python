# 30/05/2025
# Desafio 24 – Herança em Personagens de RPG

# Classe base que representa um personagem genérico
class Personagem:
    def __init__(self, nome, nivel, vida):
        # Atributos comuns a todos os personagens
        self.nome = nome
        self.nivel = nivel
        self.vida = vida

    # Método para exibir os atributos do personagem
    def exibir_status(self):
        print(f"Nome: {self.nome}")
        print(f"Nivel: {self.nivel}")
        print(f"Vida : {self.vida}")
        print()

    # Método para reduzir a vida do personagem quando ele recebe dano
    def receber_dano(self, dano):
        if self.vida > dano:
            self.vida -= dano
            print(f"O Personagem {self.nome} recebeu {dano} de dano. E ficou com {self.vida} de pontos de vida.")
        else:
            self.vida = 0
            print(f"O Personagem {self.nome} foi nocauteado!")

# Classe Guerreiro herda da classe Personagem
class Guerreiro(Personagem):
    def __init__(self, nome, nivel, vida):
        # Chama o construtor da classe pai
        super().__init__(nome, nivel, vida)

    # Método exclusivo do Guerreiro
    def atacar(self):
        print(f"O Guerreiro {self.nome} ataca com a espada")

# Classe Mago herda da classe Personagem
class Mago(Personagem):
    def __init__(self, nome, nivel, vida):
        super().__init__(nome, nivel, vida)

    # Método exclusivo do Mago
    def lancar_magia(self):
        print(f"O Mago {self.nome} lança uma bola de fogo!")

# Classe Monstro herda da classe Personagem
class Monstro(Personagem):
    def __init__(self, nome, nivel, vida):
        super().__init__(nome, nivel, vida)

    # Método exclusivo do Monstro
    def patada(self):
        print(f"O Monstro {self.nome} atacou com uma patada")

# Instanciando personagens com atributos personalizados
guerreiro = Guerreiro("Leo", 10, 10000)
mago = Mago("Gui", 9, 9000)
monstro = Monstro("Medo", 3, 3000)

# Simulação da batalha entre os personagens
monstro.patada()
guerreiro.receber_dano(500)
mago.lancar_magia()
monstro.receber_dano(1300)
guerreiro.atacar()
monstro.receber_dano(1700)

# Exibe o status atualizado de todos os personagens após a batalha
print(f"\nStatus dos personagens:")
guerreiro.exibir_status()
mago.exibir_status()
monstro.exibir_status()




    


