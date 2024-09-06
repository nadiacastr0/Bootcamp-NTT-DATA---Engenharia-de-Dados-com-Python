################ Primeiros Conceitos de POO em Python ################
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor): # __init__ é um método construtor
        print("Inicializando a classe...")
        # self é a instancia do objeto, uma referencia explicita
        self.cor = cor #ATRIBUTO
        self.modelo = modelo #ATRIBUTO
        self.ano = ano #ATRIBUTO
        self.valor = valor #ATRIBUTO

    def __del__(self): # __del__ é um método destrutor
        print("Removendo a instância da classe.")    

    def buzinar(self):
        print("Plin Plin...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vruuuuuuuuu...")

    def freiar(self):
        print("Phiiiiix...")

    # def __str__(self):
    #     return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

# b1 = Bicicleta("vermelha", "caloi", 2022, 600)
# b1.buzinar()
# b1.correr()
# b1.parar()
# print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("verde", "monak", 2011, 360)
print(b2)