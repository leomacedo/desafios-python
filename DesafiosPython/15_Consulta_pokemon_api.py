# 16/05/2025 
# Desafio: Criar uma Pokédex com uso de API e módulos externos

# Importamos o módulo requests, que permite fazer requisições HTTP (como GET) para acessar dados de APIs
import requests

# Importamos o módulo os para poder limpar a tela do terminal de forma multiplataforma
import os

# Dicionário que associa tipos de Pokémon com seus respectivos emojis
emoji_tipos = {
    "electric": "⚡",
    "fire": "🔥",
    "water": "💧",
    "grass": "🌿",
    "flying": "🕊️",
    "bug": "🐛",
    "poison": "☠️",
    "normal": "🙂",
    "ground": "🌍",
    "rock": "🪨",
    "psychic": "🔮",
    "ghost": "👻",
    "ice": "❄️",
    "dragon": "🐉",
    "dark": "🌑",
    "steel": "⚙️",
    "fairy": "✨",
    "fighting": "🥊"
}

# Função para limpar a tela do terminal (usamos 'cls' para Windows e 'clear' para Unix/Linux/Mac)
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função principal que busca e mostra os dados do Pokémon consultado
def mostrar_dados_pokemon(nome):
    # Montamos a URL da API, incluindo o nome do Pokémon fornecido pelo usuário
    url = f"https://pokeapi.co/api/v2/pokemon/{nome}"
    
    # Fazemos uma requisição GET para a API usando a URL
    resposta = requests.get(url)

    # Se a resposta tiver código 200 (sucesso), processamos os dados
    if resposta.status_code == 200:
        dados = resposta.json()  # Convertendo a resposta em JSON (dicionário Python)

        # Extraímos o nome, altura e peso do Pokémon
        nome_pokemon = dados["name"].capitalize()
        altura = dados["height"]
        peso = dados["weight"]

        # Extraímos os tipos (lista de dicionários) e pegamos apenas o nome do tipo
        tipos = [tipo["type"]["name"] for tipo in dados["types"]]

        # Adicionamos emojis aos tipos, se houver no dicionário
        tipos_com_emoji = [f"{emoji_tipos.get(t, '')} {t}" for t in tipos]

        # Limpamos a tela para deixar a saída mais bonita
        limpar_tela()

        # Exibimos os dados formatados
        print(f"🔍  Pokédex - Resultado da busca 🔎\n")
        print(f"📛 Nome: {nome_pokemon}")
        print(f"📏 Altura: {altura}")
        print(f"⚖️  Peso: {peso}")
        print(f"🏷️  Tipos: {', '.join(tipos_com_emoji)}\n")

    else:
        # Se a API não encontrou o Pokémon, avisamos o usuário
        print("❌ Pokémon não encontrado. Verifique o nome e tente novamente.\n")

# Loop principal do programa que permite o usuário consultar vários Pokémons
def iniciar_pokedex():
    while True:
        # Solicitamos o nome do Pokémon ao usuário
        nome = input("Digite o nome de um Pokémon (ou 'sair' para encerrar): ").lower()
        
        # Se o usuário digitar "sair", encerramos o loop
        if nome == "sair":
            print("👋 Até a próxima!")
            break

        # Chamamos a função que mostra os dados do Pokémon
        mostrar_dados_pokemon(nome)

# Chamamos a função principal para iniciar o programa
iniciar_pokedex()
