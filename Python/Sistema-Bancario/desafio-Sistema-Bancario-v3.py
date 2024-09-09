# 06/09/2024 -- Sistema Bancário com operações: sacar, depositar e visualizar extrato, criar conta, criar usuário
#            -- Classes Transacao, Deposito, Saque, Historio, Cliente, Pessoa Fisica, Conta e Conta corrente

# Acrescentando Novos conhecimentos de POO ao sistema bancario

from abc import ABC, abstractmethod

# Interface Transacao
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# Classe Deposito que implementa a interface Transacao
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        conta.depositar(self.valor)
        conta.historico.adicionar_transacao(f'Depósito de {self.valor:.2f}')
        print(f'Depósito de {self.valor:.2f} registrado com sucesso.')

# Classe Saque que implementa a interface Transacao
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(f'Saque de {self.valor:.2f}')
            print(f'Saque de {self.valor:.2f} registrado com sucesso.')
        else:
            print(f'Saque de {self.valor:.2f} falhou. Saldo insuficiente.')

# Classe Historico
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, descricao):
        self.transacoes.append(descricao)

# Classe Pai Cliente
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

# Classe PessoaFisica que herda de Cliente
class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

# Classe Pai Conta
class Conta:
    def __init__(self, numero, agencia, cliente):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()
        self.cliente.adicionar_conta(self)

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        return False

    def depositar(self, valor):
        self.saldo += valor

    def exibir_extrato(self):
        print("\n----------------- EXTRATO -----------------")
        print(f"Extrato da Conta {self.numero}:")
        for transacao in self.historico.transacoes:
            print(transacao)
        print(f"Saldo Atual: {self.saldo:.2f}")
        print("\n-------------------------------------------")

# Classe ContaCorrente que herda de Conta
class ContaCorrente(Conta):
    def __init__(self, numero, agencia, cliente, limite, limite_saques):
        super().__init__(numero, agencia, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

# Constantes e Menu iterativo
LIMITE = 500
LIMITE_SAQUES = 3
AGENCIA_PADRAO = "0001"

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar conta
[u] Criar usuário
[x] Sair
Selecione uma operação: """

# Funções de Operações para armaenamento dos dados
def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço: ")
    usuario = PessoaFisica(endereco, cpf, nome, data_nascimento)
    usuarios[cpf] = usuario
    print("Usuário criado com sucesso!")

def criar_conta(contas, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = usuarios.get(cpf)
    if not usuario:
        print("Usuário não encontrado!")
        return
    numero = len(contas) + 1
    conta = ContaCorrente(numero, AGENCIA_PADRAO, usuario, LIMITE, LIMITE_SAQUES)
    contas[numero] = conta
    print(f"Conta {numero} criada com sucesso!")

def depositar(contas):
    numero = int(input("Informe o número da conta: "))
    conta = contas.get(numero)
    if not conta:
        print("Conta não encontrada!")
        return
    valor = float(input("Informe o valor para depósito: "))
    deposito = Deposito(valor)
    conta.cliente.realizar_transacao(conta, deposito)

def sacar(contas):
    numero = int(input("Informe o número da conta: "))
    conta = contas.get(numero)
    if not conta:
        print("Conta não encontrada!")
        return
    valor = float(input("Informe o valor para saque: "))
    saque = Saque(valor)
    conta.cliente.realizar_transacao(conta, saque)

def exibir_extrato(contas):
    numero = int(input("Informe o número da conta: "))
    conta = contas.get(numero)
    if not conta:
        print("Conta não encontrada!")
        return
    conta.exibir_extrato()

# Main - Loop principal para execução do sistema
def main():
    usuarios = {}
    contas = {}
    
    while True:
        operacao = input(MENU).lower()

        if operacao == 'd':
            depositar(contas)
        elif operacao == 's':
            sacar(contas)
        elif operacao == 'e':
            exibir_extrato(contas)
        elif operacao == 'c':
            criar_conta(contas, usuarios)
        elif operacao == 'u':
            criar_usuario(usuarios)
        elif operacao == 'x':
            print("Saindo do sistema...")
            break
        else:
            print("Operação inválida, por favor selecione novamente.")

if __name__ == "__main__":
    main()
