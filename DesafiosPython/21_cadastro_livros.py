# 27/05/2025

class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero

    def exibir_dados(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano: {self.ano}")
        print(f"Gênero: {self.genero}")

# Instanciando os livros
principe = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", "1943", "Ficção Filosófica")
pythonini = Livro("Python para Iniciantes", "João da Silva", "2023", "Programação")
leolivro = Livro("Um dia vou ser adulto", "Leo", "2025", "Reflexivo")

# Lista de livros
lista_livros = [principe, pythonini, leolivro]

# Exibição
for indice, livro in enumerate(lista_livros, start=1):
    print(f"\n📚 Livro {indice}")
    livro.exibir_dados()


    
