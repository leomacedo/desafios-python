# 06/06/2025
# Desafio 30 - Consulta de clima atual usando API pública (Open-Meteo)
# Este projeto faz uma requisição GET para uma API pública e mostra a previsão atual de Aracaju

import requests  # Biblioteca para fazer requisições HTTP

# URL da API com latitude e longitude de Aracaju
url = "https://api.open-meteo.com/v1/forecast?latitude=-10.9472&longitude=-37.0731&current_weather=true"

# Envia a requisição para a API
resposta = requests.get(url)

# Verifica se a resposta foi bem-sucedida (código 200 = OK)
if resposta.status_code == 200:
    print("✅ Conexão bem-sucedida com a API de clima!\n")

    # Converte a resposta JSON em dicionário Python
    dados = resposta.json()

    # Acessa os dados atuais de clima de forma segura com .get()
    clima = dados.get("current_weather", {})

    # Exibe as informações para o usuário
    print(f"🌡️ Temperatura: {clima.get('temperature')}°C")
    print(f"💨 Vento: {clima.get('windspeed')} km/h")
    print(f"⏰ Última atualização: {clima.get('time')}")
else:
    # Exibe erro se o status não for 200
    print(f"❌ Erro ao acessar API! Código de status: {resposta.status_code}")
