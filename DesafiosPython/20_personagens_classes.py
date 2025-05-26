# 25/05/2025 e 26/05/2025
# Desafio 20

# Criação da classe Personagem
class Personagem:
    def __init__(self, nome, classe_personagem, nivel, vida):
        self.nome = nome
        self.classe_personagem = classe_personagem
        self.nivel = nivel
        self.vida = vida

    def exibir_ficha(self):
        print(f"Nome: {self.nome}")
        print(f"Classe: {self.classe_personagem}")
        print(f"Nível: {self.nivel}")
        print(f"Vida: {self.vida}")
        print("-" * 25)

    def receber_dano(self, quantidade):
        self.vida -= quantidade
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {quantidade} de dano! Vida atual: {self.vida}")

    def subir_nivel(self):
        self.nivel += 1
        self.vida += 20
        print(f"{self.nome} subiu para o nível {self.nivel}! Vida aumentada para {self.vida}")

# Criando 3 personagens diferentes
arthos = Personagem("Arthos", "Guerreiro", 5, 120)
lyra = Personagem("Lyra", "Maga", 7, 80)
thorne = Personagem("Thorne", "Arqueiro", 4, 100)

# Usando os métodos!
arthos.receber_dano(30)
lyra.subir_nivel()

# Exibindo os dados atualizados de cada personagem
print("\nFicha dos Personagens:")
arthos.exibir_ficha()
lyra.exibir_ficha()
thorne.exibir_ficha()

