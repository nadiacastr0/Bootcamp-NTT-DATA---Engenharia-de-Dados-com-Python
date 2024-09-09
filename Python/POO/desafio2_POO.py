############# HERANÇA #####################

# Herança fornece reutilização de código

""" 
    - Herança Simples quando uma classe herda somente de uma classe pai
    - Classe base Veiculo
"""
class Veiculo:
    def __init__(self, tipo, modelo, km):
        self.tipo = tipo
        self.modelo = modelo
        self.km = km

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# Classe derivada Carro
class Carro(Veiculo):
    def __init__(self, tipo, modelo, km, portas):
        super().__init__(tipo, modelo, km)
        self.portas = portas

# Criando um objeto da classe Carro
meu_carro = Carro("Carro", "Palio", 10000, 4)
print(meu_carro)


""" 
    - Herança Mútipla quando uma classe herda de várias classes pai
    - Classes pai Animal, Mamifero, Ave
"""
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def comer(self):
        print(f"{self.nome} está comendo.")

class Mamifero(Animal):
    def amamentar(self):
        print(f"{self.nome} está amamentando.")

class Ave(Animal):
    def voar(self):
        print(f"{self.nome} está voando.")

# Classe derivada Morcego
class Morcego(Mamifero, Ave):
    def __init__(self, nome):
        super().__init__(nome)

# Criando uma instância de Morcego
morcego = Morcego("Drak")

# Usando métodos herdados
morcego.comer()       
morcego.amamentar()   
morcego.voar()        
