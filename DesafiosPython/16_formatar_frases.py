# 19/05/2025
# Lista original de frases com palavras separadas por hífens
# Desafio para exercitar List Comprehension
frases = [
    "eu-gosto-de-café",
    "hoje-é-um-bom-dia",
    "python-é-legal"
]

# Etapa 1: Substituir os hífens "-" por espaços " "
# Isso deixa as frases mais parecidas com frases normais
frases = [frase.replace("-", " ") for frase in frases]
# Resultado parcial: ['eu gosto de café', 'hoje é um bom dia', 'python é legal']

# Etapa 2: Para cada frase, fazemos o seguinte:
#  - Dividimos a frase em palavras usando .split()
#  - Usamos list comprehension para capitalizar cada palavra com .capitalize()
#  - Depois, juntamos tudo de novo com ' '.join() para voltar a ser uma frase única
frases_formatadas = [' '.join([palavra.capitalize() for palavra in frase.split()]) for frase in frases]
# Resultado final: ['Eu Gosto De Café', 'Hoje É Um Bom Dia', 'Python É Legal']

# Exibe o resultado no terminal
print(frases_formatadas)
