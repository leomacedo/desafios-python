# 03/06/2025

"""
Desafio 28 - Cofre Secreto com Variáveis de Ambiente

Este script simula um sistema de acesso a um "cofre de mensagens motivacionais",
utilizando boas práticas para proteger informações com variáveis de ambiente.

Requisitos:
- Um arquivo .env contendo a variável SEGREDO_DO_LEO com o valor correto.
- A biblioteca 'python-dotenv' instalada (pip install python-dotenv).

Objetivo:
Mostrar como acessar dados sensíveis de forma segura sem expor no código.
"""

import os
from dotenv import load_dotenv  # Biblioteca para carregar variáveis de ambiente de um arquivo .env

# 🔄 Carrega as variáveis definidas no arquivo .env para o ambiente do sistema
load_dotenv()

# 🔍 Recupera o valor da variável chamada 'SEGREDO_DO_LEO'
segredo = os.getenv("SEGREDO_DO_LEO")

# 🔐 Verifica se a variável contém a senha correta
if segredo == "42vidasvalem":
    print("✅ Acesso autorizado ao cofre secreto do Leo!")
    print("🔐 Mensagem: Você é mais forte do que pensa. A vida ainda vale muito a pena.")
else:
    print("❌ Acesso negado. Chave incorreta ou .env não configurado.")

