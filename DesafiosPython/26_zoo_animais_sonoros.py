# 31/05/2025
# Desafio 26 de Abstração: Zoo dos Animais Sonoros

# Importando ferramentas para criação de classes abstratas
from abc import ABC, abstractmethod

# Classe abstrata Animal, que serve como base para todos os animais do zoológico
class Animal(ABC):
    def __init__(self, nome):
        # Atributo comum a todos os animais: nome
        self.nome = nome

    def __str__(self):
        # Retorna uma representação amigável do animal ao usar print()
        return f"Animal: <{self.nome}>"

    @abstractmethod
    def fazer_som(self):
        # Método abstrato que deve ser implementado por cada animal (latir, miar, mugir...)
        pass

    @abstractmethod
    def interagir(self):
        # Método abstrato que define uma interação típica de cada animal
        pass

# Classe Cachorro herda de Animal e implementa seus próprios comportamentos
class Cachorro(Animal):
    def __init__(self, nome):
        # Reaproveita a inicialização da classe base
        super().__init__(nome)

    def fazer_som(self):
        # Som típico do cachorro
        return "Au au!"

    def interagir(self):
        # Comportamento típico do cachorro
        return "balança o rabo"

# Classe Gato herda de Animal e implementa seus próprios comportamentos
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "Miau!"

    def interagir(self):
        return "se esfrega"

# Classe Vaca herda de Animal e implementa seus próprios comportamentos
class Vaca(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        return "Muuuuu!"

    def interagir(self):
        return "mastiga capim"

# Lista com instâncias de animais do zoológico
animais = [
    Cachorro("Doguinho"),
    Gato("Lessie"),
    Vaca("Mimosa")
]

# Teste que geraria erro: não se pode instanciar uma classe abstrata diretamente
# animal = Animal("DaErroAqui")  # Isso causaria um TypeError

# Loop que percorre os animais e exibe seus comportamentos
for a in animais:
    print(f"{a} : {a.interagir()} e faz {a.fazer_som()}")
