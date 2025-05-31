# 31/05/2025 
# Desafio 25: Sistema de Cadastro de Funcionários com Abstração

# Importando ferramentas para criar classes abstratas
from abc import ABC, abstractmethod

# Classe base abstrata para todos os funcionários
class Funcionario(ABC):
    def __init__(self, nome, salario):
        # Atributos comuns a todos os funcionários
        self.nome = nome
        self.salario = salario

    def __str__(self):
        # Método para retornar uma representação legível do funcionário
        return f"Nome: {self.nome} | Salário: R${self.salario:.2f}"

    @abstractmethod
    def calcular_bonus(self):
        # Método abstrato que obriga as subclasses a implementarem sua versão
        pass

# Classe Gerente, que herda de Funcionario
class Gerente(Funcionario):
    def __init__(self, nome, salario):
        # Chama o construtor da superclasse (Funcionario)
        super().__init__(nome, salario)

    def calcular_bonus(self):
        # Implementação do bônus específico para gerente: 20% do salário
        return self.salario * 0.2

# Classe Desenvolvedor, que também herda de Funcionario
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario):
        # Chama o construtor da superclasse (Funcionario)
        super().__init__(nome, salario)

    def calcular_bonus(self):
        # Implementação do bônus específico para desenvolvedor: 10% do salário
        return self.salario * 0.1

# Função que exibe a folha de pagamento de uma lista de funcionários
def exibir_folha_pagamento(funcionarios):
    print("\n--- Folha de Pagamento ---")
    for f in funcionarios:
        bonus = f.calcular_bonus()  # Chama o método polimórfico
        total = f.salario + bonus
        # Exibe nome, bônus e total a receber do funcionário
        print(f"{f.nome} | Bônus: R${bonus:.2f} | Total: R${total:.2f}")

# Lista de funcionários (instâncias de Gerente e Desenvolvedor)
funcionarios = [
    Gerente("Alice", 5000),
    Desenvolvedor("Bob", 3000)
]

# Chamada da função para exibir a folha de pagamento
exibir_folha_pagamento(funcionarios)


