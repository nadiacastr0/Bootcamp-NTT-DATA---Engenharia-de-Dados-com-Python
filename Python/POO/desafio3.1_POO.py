# Exemplos de como usar propriedades em python #
## Estes exemplos foram gerados polo copilot para testes didaticos ##

"""
    - Exemplo 1: Usando o Decorator @property
"""
class Circulo:
    def __init__(self, raio):
        self._raio = raio

    @property
    def raio(self):
        return self._raio

    @raio.setter
    def raio(self, valor):
        if valor < 0:
            raise ValueError("O raio não pode ser negativo")
        self._raio = valor

    @property
    def area(self):
        return 3.14159 * (self._raio ** 2)

# Uso
c = Circulo(5)
print(c.area)  # Saída: 78.53975
c.raio = 10
print(c.area)  # Saída: 314.159

#============================================================================

"""
    - Exemplo 2: Propriedades para Controle de Acesso
"""
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, valor):
        if valor < 0:
            raise ValueError("O salário não pode ser negativo")
        self._salario = valor

# Uso
f = Funcionario("Ana", 5000)
print(f.salario)  # Saída: 5000
f.salario = 6000
print(f.salario)  # Saída: 6000

#================================================================================

"""
    - Exemplo 3: Propriedades Somente Leitura
"""
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    @property
    def area(self):
        return self.largura * self.altura

# Uso
r = Retangulo(4, 5)
print(r.area)  # Saída: 20
