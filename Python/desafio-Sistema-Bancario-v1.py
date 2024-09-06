# 27/08/2024 -- Sistema Bancário com operações: sacar, depositar e visualizar extrato

# Menu de operações disponíveis para o usuário

MENU = """
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair

    """

# Definir limite e limite_saque como constantes pois esses valores não devem mudar durante a execução do programa.
LIMITE = 500
LIMITE_SAQUES = 3

""" 
    - Função para Depositar
    - Recebe o saldo atual e o extrato das movimentações
    - Solicita o valor do depósito ao usúario e atualiza o saldo e o extrato
"""
def depositar(saldo, extrato):

    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.") 
    return saldo, extrato

"""
    - Função para Sacar
    - Recebe o saldo atual, o extrato e o número de saques realizados
    - Solicita o valor do saque ao usuário e atualiza o saldo, extrato e o npumero de saques
"""
def sacar(saldo, extrato, numero_saques):

    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > LIMITE
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Saldo suficiente para realizar este saque.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque desejado excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques

"""
    - Função para Visualizar o Extrato
    - Caso não haja movimentações, informa ao usuário
"""   
def exibir_extrato(saldo, extrato):
    print("\n----------------- EXTRATO -----------------")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n-------------------------------------------")

"""
    - Função para executar o menu e gerenciar as operações
    - Loop princial que exibe o menu e processa a escola do usuário
"""
def main():
    saldo = 0
    extrato = ""
    numero_saques = 0

    while True:
        opcao = input(MENU)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "x":
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

if __name__ == "__main__":
    main()