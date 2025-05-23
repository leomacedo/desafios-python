# 22/05/2025

# Dicionário que associa cada personagem com sua velocidade média em km/h
personagens = {
    "Sonic": 60,     # Sonic é o mais rápido, né? Lógico!
    "Tails": 50,     # Tails é o fofinho inteligente, mas também corre bem
    "Knuckles": 55   # Knuckles tem força... e boas pernas também!
}

# Tempo em que a corrida será avaliada (em minutos)
tempo = 3

# Função que calcula a distância percorrida, dado a velocidade (km/h) e o tempo (minutos)
def calcular_distancia(velocidade, tempo):
    # Conversão: tempo/60 transforma minutos em horas para o cálculo ficar coerente
    distancia = velocidade * tempo / 60
    return distancia

# Loop que percorre cada personagem e calcula sua distância em 3 minutos
for personagem, velocidade in personagens.items():
    distancia = calcular_distancia(velocidade, tempo)
    # Mostra a distância que cada personagem percorreu no tempo definido
    print(f"{personagem} fez uma distância de {distancia:.2f} km no tempo de {tempo} minutos")

# Lista por compreensão para filtrar personagens que correram mais que 1.5 km
rapidos = [
    personagem
    for personagem, velocidade in personagens.items()
    if calcular_distancia(velocidade, tempo) > 1.5
]

# Mostra quais personagens são "bem rápidos" com base na distância de 1.5 km
print(f"\nOs personagens {rapidos} são bem rápidos. E conseguiram ultrapassar pelo menos 1.5km em {tempo} minutos")

# Criação de um novo dicionário com a distância percorrida por cada personagem
distancias = {
    personagem: calcular_distancia(velocidade, tempo)
    for personagem, velocidade in personagens.items()
}

# max() com key=distancias.get retorna o personagem com a maior distância
vencedor = max(distancias, key=distancias.get)

# Imprime o campeão da corrida
print(f"\nO vencedor da corrida é {vencedor}")
