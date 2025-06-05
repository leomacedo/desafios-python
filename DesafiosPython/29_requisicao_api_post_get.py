import requests  # Importa a biblioteca requests para fazer requisições HTTP

# Define a URL do endpoint da API (JSONPlaceholder, usado para testes)
url = "https://jsonplaceholder.typicode.com/posts"

# Define os cabeçalhos da requisição (headers), indicando que o conteúdo será JSON
headers = {
    "Content-Type": "application/json"
}

# Define o corpo da requisição (body), com os dados que serão enviados no POST
body = {
    "title": "O primeiro POST",
    "body": "Hoje eu fiz minha primeira requisição POST com Python!",
    "userId": 1
}

# Define os parâmetros de consulta para uma requisição GET
params = {
    "userId": 1  # Vamos buscar todos os posts do usuário com ID 1
}

# Faz uma requisição POST, enviando os dados no corpo em formato JSON
response = requests.post(url, headers=headers, json=body)

print("----- Simulação de um POST --------")
print("Status:", response.status_code)  # Exibe o status da requisição (201 = criado com sucesso)
print("Resposta da API:")
print(response.json())  # Exibe o conteúdo retornado em formato JSON (inclui um id gerado automaticamente)
print()

# Faz uma requisição GET para buscar posts do userId=1
response = requests.get(url, params=params)

print("------ Pegando requisição da API seguindo os parâmetros -----")
print("Status:", response.status_code)  # Exibe o status (200 = sucesso)
print("Resposta da API:")
print(response.json())  # Exibe os posts encontrados para o userId=1
