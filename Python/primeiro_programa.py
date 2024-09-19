# print("Hello world!")

#### Testando classe String ####

# nome = "Python"

# print(nome.upper())
# print(nome.lower())
# print(nome.title())
# print(nome.strip())
# print(nome.lstrip())
# print(nome.rstrip())
# print(nome.center(10, "-"))
# print(" ".join(nome))

# minha_lista = ["maçã Verde", "BAnana", "maçã", "laranja", "banana"]
# minha_lista_sem_duplicatas = []
# [minha_lista_sem_duplicatas.append(item.title()) for item in minha_lista if item.title() not in minha_lista_sem_duplicatas]
# print(minha_lista_sem_duplicatas)

# def filtrar_visuais(lista_visuais):
#     # Converter a string de entrada em uma lista
#     visuais = lista_visuais.split(", ")
    
#     # Normalize e remova duplicatas usando um conjunto
#     visuais_normalizados = {visual.title() for visual in visuais}
    
#     # Converta o conjunto de volta para uma lista ordenada
#     lista_final = sorted(visuais_normalizados)
    
#     # Unir a lista em uma string, separada por vírgulas
#     return ", ".join(lista_final)

# # Capturar a entrada do usuário
# entrada_usuario = input()

# # Processar a entrada e obter a saída
# saida = filtrar_visuais(entrada_usuario)
# print(saida)

from datetime import datetime

def extrair_anos(datas):
    # Divide a string de datas em uma lista
    lista_datas = datas.split(", ")
    # Extraia o ano de cada data e cria uma nova lista com os anos
    anos = [str(datetime.strptime(data, "%Y-%m-%d").year) for data in lista_datas]
    # Junta os anos em uma string separada por vírgula e retorna
    return ", ".join(anos)

entrada = input()

# Chame a função para imprimir o resultado:
saida = extrair_anos(entrada)
print(saida)

