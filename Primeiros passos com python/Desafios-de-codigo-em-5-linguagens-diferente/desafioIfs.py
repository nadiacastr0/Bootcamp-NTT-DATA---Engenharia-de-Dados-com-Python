"""
Para ler e escrever dados em Python, utilizamos as seguintes funções:
    - input: lê UMA linha com dado(s) de Entrada do usúario;
    - print: imprime um texto de Saída (Output), pulando linha.
"""

#Função útil para o calculo do imposto (baseado nas aliquotas).
def calcular_imposto(salario):
    aliquota = 0.00
    if (salario >= 0 and salario <= 1100):
        aliquota = 0.05
    elif (salario >= 1100.01 and salario <= 2500):
        aliquota = 0.10
    else:
        aliquota = 0.15
    return aliquota * salario

#Lê os valores de Entrada:
valor_salario = float(input())
valor_baneficios = float(input())

#Calcula o imposto através da dunção "calcular_imposto":
valor_imposto = calcular_imposto(valor_salario)
#Calcula e imprime a Saída (com 2 casas decimais):
saida = valor_salario - valor_imposto + valor_baneficios
print(f'{saida:.2f}')
