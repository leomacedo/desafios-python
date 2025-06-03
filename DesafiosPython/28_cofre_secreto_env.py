import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env
load_dotenv()

# Busca o valor da variável
segredo = os.getenv("SEGREDO_DO_LEO")

if segredo == "42vidasvalem":
    print("✅ Acesso autorizado ao cofre secreto do Leo!")
    print("🔐 Mensagem: Você é mais forte do que pensa. A vida ainda vale muito a pena.")
else:
    print("❌ Acesso negado. Chave incorreta ou .env não configurado.")
