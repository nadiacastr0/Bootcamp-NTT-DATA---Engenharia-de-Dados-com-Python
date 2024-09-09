################ ENCAPSULAMENTO ################
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular  # Atributo privado
        self.__saldo = saldo      # Atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def __calcular_juros(self):  # Método privado
        return self.__saldo * 0.01

    def exibir_saldo(self):
        juros = self.__calcular_juros()
        saldo_total = self.__saldo + juros
        print(f"Saldo atual: R${self.__saldo:.2f}")
        print(f"Saldo com juros: R${saldo_total:.2f}")

# Exemplo de uso
conta = ContaBancaria("João", 1000)
conta.depositar(500)
conta.exibir_saldo()

# Tentativas de acessar atributos e métodos privados diretamente
# resultarão em erro:
# print(conta.__saldo)  # AttributeError
# conta.__calcular_juros()  # AttributeError

"""
    Neste exemplo, `__titular` e `__saldo` são atributos privados, e `__calcular_juros` é um método privado.
    Eles não podem ser acessados diretamente fora da classe, o que ajuda a proteger os dados internos da classe.
"""