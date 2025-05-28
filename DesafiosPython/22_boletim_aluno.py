# 28/05/2025

# Importa a biblioteca statistics com apelido "stat" para usar a função de média
import statistics as stat

# Criação da classe Aluno, que representa um estudante com nome, matrícula e lista de notas
class Aluno:
    def __init__(self, nome, matricula, lista_notas):
        # Atributos da classe: nome do aluno, número de matrícula e lista de notas (inicialmente vazia)
        self.nome = nome
        self.matricula = matricula
        self.lista_notas = lista_notas

    # Método para adicionar uma nova nota à lista do aluno
    def adicionar_nota(self, nota):
        self.lista_notas.append(nota)
        print(f"A nota {nota} foi adicionada na lista de {self.nome}")

    # Método que calcula e retorna a média das notas usando a função mean() da biblioteca statistics
    def calcular_media(self):
        media = stat.mean(self.lista_notas)
        return media

    # Método para exibir todos os dados do aluno formatados
    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Matricula: {self.matricula}")
        print(f"Notas: {self.lista_notas}")
        # Aqui chamamos o método calcular_media() e formatamos com duas casas decimais
        print(f"Media Final: {self.calcular_media(): .2f}")

# Criamos uma instância da classe Aluno com nome "Leonardo", matrícula "1234" e uma lista de notas vazia
leo = Aluno("Leonardo", "1234", [])

# Adicionando três notas para o aluno "leo"
leo.adicionar_nota(8.5)
leo.adicionar_nota(10)
leo.adicionar_nota(5)

# Exibindo os dados completos do aluno após adicionar as notas
leo.exibir_dados()
