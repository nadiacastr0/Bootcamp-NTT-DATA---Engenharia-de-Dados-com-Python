# 04/09/2024 -- Sistema Bancário com operações: sacar, depositar e visualizar extrato, criar conta, criar usuário

# Acrescentando Novos conhecimentos ao sistema bancario
# - Lista
# - Data
# - Decorador de log

import random
import string
from datetime import datetime

# Menu de operações disponíveis para o usuário
MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar conta
[u] Criar usuário
[x] Sair
Selecione uma operação: """

# Definir limite, limite_saque e agência como constantes
LIMITE = 500
LIMITE_SAQUES = 3
AGENCIA_PADRAO = "0001"  

# Estruturas para armazenar usuários e contas
usuarios = {}
contas = {}

def gerar_numero_conta():
    """
        - Gera um número de conta aleatório de 6 dígitos.
    """
    return ''.join(random.choices(string.digits, k=6))

def log_transacao(func):
    """
        - Decorador para registrar data e hora das transações.
    """
    def wrapper(conta, *args, **kwargs):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        resultado = func(conta, *args, **kwargs)
        valor = args[0] if args else kwargs.get('valor', 0)
        tipo_transacao = func.__name__.capitalize()
        conta['extrato'] += f"{data_hora} - {tipo_transacao}: R$ {valor:.2f}\n"
        return resultado
    """
        - wrapper é a função interna que será executada no lugar da função original func.
        - Ela aceita os mesmos argumentos que func.
    """
    return wrapper    

def calcular_idade(data_nascimento):
    """
        - Calcula a idade a partir da data de nascimento.
    """
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    hoje = datetime.today()
    idade = hoje.year - data_nascimento.year - ((hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day))
    return idade

def criar_usuario():
    """
        - Cria um novo usuário e adiciona à lista de usuários.
    """
    nome = input("Nome: ")
    cpf = input("CPF: ")
    data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")

    # Verifica se o usuário é maior de 18 anos
    if calcular_idade(data_nascimento) < 18:
        print(">>>Usuário deve ser maior de 18 anos para criar uma conta.")
        return

    logradouro = input("Logradouro: ")
    nro = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")

    usuario_id = len(usuarios) + 1
    usuarios[usuario_id] = {
        'nome': nome,
        'cpf': cpf,
        'data_nascimento': data_nascimento,
        'endereco': f"{logradouro}, {nro} - {bairro} - {cidade}/{estado}"
    }
    print(f"\nUsuário criado com sucesso!")
    print(f"ID do usuário: {usuario_id}")
    print(f"Nome: {nome}")
    print(f"CPF: {cpf}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Endereço: {usuarios[usuario_id]['endereco']}")
    print("\nAgora você pode criar uma conta usando o ID acima.")
    return usuario_id

def criar_conta(usuario_id):
    """
        - Cria uma nova conta para um usuário e adiciona à lista de contas.
    """
    if usuario_id not in usuarios:
        print(">>>Usuário não encontrado. Por favor, crie um usuário primeiro.")
        return

    numero_conta = gerar_numero_conta()
    conta = {
        'usuario_id': usuario_id,
        'numero_conta': numero_conta,
        'agencia': AGENCIA_PADRAO,
        'saldo': 0,
        'extrato': "",
        'numero_saques': 0
    }
    contas[numero_conta] = conta

    usuario = usuarios[usuario_id]
    print(f"\nConta criada com sucesso!")
    print(f"Número da conta: {numero_conta}")
    print(f"Agência:\t{conta['agencia']}")
    print(f"Titular:\t{usuario['nome']}")
    print(f"Saldo:\t\tR$ {conta['saldo']:.2f}")
    print(f"\nPara gerenciar sua conta, use o número da conta acima.")
    return numero_conta

@log_transacao
def depositar(conta, valor):
    """
        - Função para Depositar
        - Recebe o saldo atual e o extrato das movimentações
        - Solicita o valor do depósito ao usúario e atualiza o saldo e o extrato
    """
    if valor > 0:
        conta['saldo'] += valor
    else:
        print(">>>Operação falhou! O valor informado é inválido.")
    return conta

@log_transacao
def sacar(conta, valor):
    """
        - Função para Sacar
        - Recebe o saldo atual, o extrato e o número de saques realizados
        - Solicita o valor do saque ao usuário e atualiza o saldo, extrato e o npumero de saques
    """
    excedeu_saldo = valor > conta['saldo']
    excedeu_limite = valor > LIMITE
    excedeu_saques = conta['numero_saques'] >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print(">>>Operação falhou! Saldo insuficiente para realizar este saque.")
    elif excedeu_limite:
        print(">>>Operação falhou! O valor do saque desejado excede o limite.")
    elif excedeu_saques:
        print(">>>Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        conta['saldo'] -= valor
        conta['numero_saques'] += 1
    else:
        print(">>>Operação falhou! O valor informado é inválido.")
    
    return conta

def exibir_extrato(conta):
    """
        - Função para Visualizar o Extrato
        - Caso não haja movimentações, informa ao usuário
    """  
    print("\n----------------- EXTRATO -----------------")
    print("Não foram realizadas movimentações." if not conta['extrato'] else conta['extrato'])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("\n-------------------------------------------")

def main():
    """
        - Função para executar o menu e gerenciar as operações
        - Loop princial que exibe o menu e processa a escola do usuário
    """
    while True:
        opcao = input(MENU)

        if opcao == "u":
            criar_usuario()
        elif opcao == "c":
            usuario_id = int(input("Informe o ID do usuário: "))
            criar_conta(usuario_id)
        elif opcao == "d":
            numero_conta = input("Informe o número da conta: ")
            if numero_conta in contas:
                valor = float(input("Informe o valor do depósito: "))
                contas[numero_conta] = depositar(contas[numero_conta], valor)
            else:
                print(">>>Número da conta não encontrado.")
        elif opcao == "s":
            numero_conta = input("Informe o número da conta: ")
            if numero_conta in contas:
                valor = float(input("Informe o valor do saque: "))
                contas[numero_conta] = sacar(contas[numero_conta], valor)
            else:
                print(">>>Número da conta não encontrado.")
        elif opcao == "e":
            numero_conta = input("Informe o número da conta: ")
            if numero_conta in contas:
                exibir_extrato(contas[numero_conta])
            else:
                print(">>>Número da conta não encontrado.")
        elif opcao == "x":
            print("Saindo do sistema. Até mais!")
            break
        else:
            print(">>>Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()
