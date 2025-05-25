# 25/05/2025
# Incompleto...

# Criação da classe Personagem
class Personagem:
    def __init__(self, nome, classe_personagem, nivel, vida):
        self.nome = nome
        self.classe_personagem = classe_personagem
        self.nivel = nivel
        self.vida = vida

# Criando 3 personagens diferentes
personagem1 = Personagem("Arthos", "Guerreiro", 5, 120)
personagem2 = Personagem("Lyra", "Maga", 7, 80)
personagem3 = Personagem("Thorne", "Arqueiro", 4, 100)

# Exibindo os dados de cada personagem
print("Ficha do Personagem 1:")
print("Nome:", personagem1.nome)
print("Classe:", personagem1.classe_personagem)
print("Nível:", personagem1.nivel)
print("Vida:", personagem1.vida)
print()

print("Ficha do Personagem 2:")
print("Nome:", personagem2.nome)
print("Classe:", personagem2.classe_personagem)
print("Nível:", personagem2.nivel)
print("Vida:", personagem2.vida)
print()

print("Ficha do Personagem 3:")
print("Nome:", personagem3.nome)
print("Classe:", personagem3.classe_personagem)
print("Nível:", personagem3.nivel)
print("Vida:", personagem3.vida)
