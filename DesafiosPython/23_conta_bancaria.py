# 29/05/2025
# Desafio 23 – Controle Bancário com Encapsulamento

# Definição da classe que representa uma conta bancária
class ContaBancaria:
    
    # Método construtor: define os atributos iniciais da conta
    def __init__(self, titular, saldo):
        self.titular = titular               # Atributo público: nome do titular da conta
        self.__saldo = saldo                 # Atributo privado: saldo da conta (protegido com encapsulamento)
    
    # Método para consultar o saldo da conta
    def consultar_saldo(self):
        return self.__saldo                  # Retorna o saldo atual, sem permitir modificação direta

    # Método para realizar depósitos na conta
    def depositar(self, valor):
        if valor > 0:                        # Verifica se o valor é positivo
            self.__saldo += valor           # Adiciona o valor ao saldo
            print(f"Deposito de R$ {valor} foi inserido com sucesso. Valor atual: R$ {self.consultar_saldo()}")
        else:
            print("Não é possível depositar valor negativo")  # Mensagem de erro para valores inválidos
    
    # Método para realizar saques da conta
    def sacar(self, valor):
        if valor > 0:                        # Verifica se o valor é positivo
            if self.__saldo > valor:        # Verifica se há saldo suficiente
                self.__saldo -= valor       # Subtrai o valor do saldo
                print(f"Saque realizado com sucesso no valor de R$ {valor} . Valor atual: R$ {self.consultar_saldo()}")
            else:
                print("Saldo insuficiente para sacar o valor desejado para sacar")  # Erro: saldo insuficiente
        else:
            print("Não é possível sacar valor negativo")  # Erro: valor inválido
    
    # Método para exibir as informações da conta
    def exibir_dados(self):
        print(f"Titular: {self.titular}")                      # Mostra o nome do titular
        print(f"Saldo: R$ {self.consultar_saldo()}")           # Mostra o saldo, utilizando o método protegido

# Criação de uma conta para o usuário "Leonardo" com saldo inicial de R$ 1000
leoconta = ContaBancaria("Leonardo", 1000)

# Abaixo, são feitas operações e exibições do saldo a cada passo:

# Mostra o saldo inicial
print(f"Saldo atual de {leoconta.titular}: R$ {leoconta.consultar_saldo()}")

# Realiza um depósito de R$ 500
leoconta.depositar(500)

# Mostra o saldo após o depósito
print(f"Saldo atual de {leoconta.titular}: R$ {leoconta.consultar_saldo()}")

# Realiza um saque de R$ 300
leoconta.sacar(300)

# Mostra o saldo após o saque
print(f"Saldo atual de {leoconta.titular}: R$ {leoconta.consultar_saldo()}")

# Exibe os dados finais da conta
leoconta.exibir_dados()
      
