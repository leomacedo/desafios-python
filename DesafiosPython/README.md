# Desafios de Python - Portfólio

Repositório com os desafios que venho resolvendo no meu processo de aprendizado em Python. Cada arquivo representa um exercício prático, com foco em lógica, sintaxe e estrutura de código. Os desafios estão organizados em ordem de criação.

## Lista de desafios

| Nº  | Nome do Arquivo                  | Descrição                                         | Data       |
|-----|----------------------------------|---------------------------------------------------|------------|
| 01  | 01_agenda_compromissos.py        | Agenda simples de compromissos com formatação     | 13/04/2025 |
| 02  | 02_mensagens_personalizadas.py   | Mensagens personalizadas com nomes e expressões   | 14/04/2025 |
| 03  | 03_lista_tarefas_prioridades.py  | Lista de tarefas organizadas por prioridade       | 15/04/2025 |
| 04  | 04_calculadora_de_medias.py      | Calculadora de médias com avaliação de aprovação  | 16/04/2025 |
| 05  | 05_contagem_nomes.py             | Contagem de nomes e nome mais frequente           | 02/05/2025 |
| 06  | 06_contagem_respostas_for.py     | Contagem de respostas com dicionário e for        | 04/05/2025 |
| 07  | 07_contagem_respostas_max.py     | Contagem otimizada usando .get() e max()          | 04/05/2025 |
| 08  | 08_super_vendedor.py             | Identifica o vendedor com mais vendas (ou empate) | 04/05/2025 |
| 09  | 09_lista_nomes_unicos.py         | Ordena nomes únicos de uma lista com repetições   | 07/05/2025 |
| 10  | 10_lista_presenca_inteligente.py | Analisa lista de presença com base nos convidados | 08/05/2025 |


Este repositório contém uma série de desafios de programação em Python que resolvi para aprimorar minhas habilidades. Abaixo você pode conferir os detalhes dos desafios que fiz.

## Desafios

### Desafio 1: Agenda de Compromissos 🗓️

Este programa solicita ao usuário que insira três compromissos para o dia e os armazena em uma lista. Depois, exibe esses compromissos com uma mensagem numerada e estilizada. Ao final, ele deseja ao usuário um dia produtivo.

**Principais características:**
- Uso de listas para armazenar os compromissos.
- Laço `for` para coletar e exibir as informações.
- Uso de f-strings e formatação para deixar a saída mais estilosa.

**Tecnologias/Conceitos usados:**
- Listas  
- Laços `for`  
- `input()` e `print()`  
- Formatação de strings com f-strings

---

### Desafio 2: Mensagens Personalizadas 🎉

Neste programa, o usuário pode adicionar um número específico de nomes e, para cada nome, uma mensagem personalizada é gerada aleatoriamente a partir de uma lista de expressões.

**Principais características:**
- Uso de listas para armazenar os nomes e as mensagens.
- Laço `for` para coletar e exibir os dados.
- Uso de `random.choice()` para escolher uma mensagem aleatória.

**Tecnologias/Conceitos usados:**
- Listas  
- Função `random.choice()`  
- Laços `for`  
- `input()` e `print()`

---

### Desafio 3: Lista de Tarefas com Prioridades 💼

Este programa permite ao usuário cadastrar uma quantidade específica de tarefas, definindo para cada uma a prioridade (Alta, Média ou Baixa). As tarefas são então organizadas em blocos separados por prioridade e exibidas de forma clara e categorizada.

**Principais características:**
- Cadastro dinâmico de tarefas com prioridade.
- Separação das tarefas em blocos visuais por prioridade.
- Verificação de entrada para garantir valores válidos.

**Tecnologias/Conceitos usados:**
- Tuplas e listas aninhadas  
- Condicionais `if/elif`  
- Laço `for`  
- Função `input()` e `print()`

---

### Desafio 4: Calculadora de Médias com Listas 🧪

Neste programa, o usuário pode adicionar quantas notas quiser e, ao final, o programa calcula a média dessas notas. Dependendo da média, ele retorna uma mensagem de aprovação, recuperação ou reprovação.

**Principais características:**
- Uso de listas para armazenar as notas.
- Laço `for` para coletar as notas e calcular a média.
- Condicionais para avaliar o status do aluno (Aprovado, Recuperação ou Reprovado).

**Tecnologias/Conceitos usados:**
- Listas  
- Laços `for`  
- Funções `input()` e `print()`  
- Formatação de números com `"{:.2f}"`

---

### Desafio 5: Contagem de Nomes e Nome Mais Frequente 📊

Neste programa, a função conta quantas vezes um nome aparece em uma lista e retorna o nome mais frequente. Utiliza loops e variáveis globais para contar e exibir o nome mais repetido.

**Principais características:**
- Contagem de ocorrências de um nome específico.
- Determinação do nome mais frequente usando loops.
- Uso de variáveis globais para controle da contagem.

**Tecnologias/Conceitos usados:**
- Laços `for`  
- Funções  
- Uso de variáveis globais  
- Função `list.count()`

---

### Desafio 6: Contagem de Respostas com Laço for 🔄

Neste programa, o objetivo é contar quantas vezes cada aluno respondeu a uma pesquisa e determinar qual aluno respondeu mais vezes. Utiliza-se um laço `for` e um dicionário para armazenar as respostas.

**Principais características:**
- Uso de dicionários para armazenar a contagem das respostas.
- Laço `for` para iterar sobre as respostas.
- Verificação para contar corretamente o número de respostas de cada aluno.
- Identificação do aluno com mais respostas.

**Tecnologias/Conceitos usados:**
- Laços `for`  
- Dicionários  
- Condicionais `if`  
- `input()` e `print()`

---

### Desafio 7: Contagem de Respostas com Métodos Avançados 🔧

Neste desafio, a solução é aprimorada com o uso do método `.get()` de dicionários e a função `max()` para encontrar o aluno que mais respondeu de forma mais eficiente.

**Principais características:**
- Utilização do método `.get()` para simplificar a contagem de respostas.
- Uso da função `max()` para encontrar a chave com o maior valor de maneira otimizada.
- Código mais limpo e compacto, sem perder clareza.

**Tecnologias/Conceitos usados:**
- Dicionários  
- Método `.get()`  
- Função `max()`  
- Laços `for`

---

### Desafio 8: Super Vendedor do Mês 🏆


Neste desafio, trabalhamos com um dicionário que armazena o número de vendas realizadas por vendedores. O objetivo principal era identificar quem vendeu mais, e como tarefa extra, analisar o que ocorre em caso de empate.

**Principais características:**
- Utilização da função `max()` com `key=` para encontrar o vencedor.
- Verificação manual de possíveis empates entre vendedores.
- Impressão estilizada dos resultados.

**Resposta para a tarefa extra:**  
Ao usar `max(vendas, key=vendas.get)`, o Python retorna apenas o primeiro vendedor com o maior valor — neste caso, Amanda. No entanto, Felipe também teve 31 vendas. Para identificar todos os vencedores em caso de empate, foi necessário fazer uma varredura com `for` e `if`.

**Tecnologias/Conceitos usados:**
- Dicionários
- `max()` com `key=`
- Iteração com `for`
- Listas
- Condicionais
- Impressão com `f-strings`

### Desafio 9: Lista de Nomes Únicos em Ordem Alfabética 🔤


Neste desafio, o foco foi trabalhar com listas que possuem elementos duplicados. A missão era criar uma função que removesse os nomes repetidos e retornasse o resultado em ordem alfabética.

**Principais características:**
- Uso da função `set()` para eliminar duplicatas da lista original.
- Ordenação da nova lista com a função `sorted()`.
- A função retorna uma nova lista limpa e ordenada.

**Resposta para a tarefa:**  
A função transforma a lista original em um conjunto, eliminando nomes repetidos. Em seguida, a função `sorted()` organiza os elementos em ordem alfabética. O resultado é uma lista nova com os nomes únicos e organizados.

**Tecnologias/Conceitos usados:**
- Listas  
- Conjuntos (`set`)  
- Função `sorted()`  
- Definição de função personalizada  
- Impressão com `print()`

### Desafio 10: Lista de Presença Inteligente 🧠

Neste desafio, simulamos a organização de um evento com duas listas:
- `convidados`: pessoas que foram oficialmente convidadas.
- `presentes`: pessoas que realmente compareceram.

O objetivo foi criar um programa que:
1. Mostrasse quem compareceu e era realmente convidado.
2. Apontasse quem apareceu sem ter sido convidado.
3. Verificasse se todos os convidados compareceram ao evento.

**Principais características:**
- Uso de **conjuntos (`set`)** para facilitar comparações entre listas.
- Uso das operações `intersection()`, `difference()` e `issubset()` para lógica de presença.
- Condicional simples para checar cobertura total dos convidados.

**Tecnologias/Conceitos usados:**
- Conjuntos (`set`)
- Operações de conjuntos: interseção, diferença, subconjunto
- Condicionais (`if`)
- Impressão com `print()`
