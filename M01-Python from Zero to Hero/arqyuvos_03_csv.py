import csv


# LEITURA DE ARQUIVOS

# lendo com listas
# with open("produto.csv", "r") as arquivo_csv:
#   # leitor = csv.reader(arquivo_csv)
#   leitor = csv.DictReader(arquivo_csv)
#   for linha in leitor:
#     print(linha)

# lendo com dicionários
# with open("birthplace-2018-census-csv.csv", "r") as censo_csv:
#   # leitor = csv.reader(censo_csv)
#   leitor = csv.DictReader(censo_csv)
#   for linha in leitor:
#     print(linha)    

# ESCRITA DE ARQUIVOS
# escrevendo com listas
# with open("produto2.csv", "w", newline="") as arquivo_csv:
#   escritor = csv.writer(arquivo_csv)
#   escritor.writerow(['PRODUTO', 'QUANTIDADE', 'PRECO']) # cabeçalho
#   escritor.writerow(['ARROZ', 12, 7.25])
#   escritor.writerow(['FEIJAO', 5, 8.50])
#   escritor.writerow(['CUZCUZ', 20, 2.25])
#   escritor.writerow(['TAPIOCA', 3, 9.00])

# escrevendo com dicionários
# with open("produto3.csv", "w", newline="") as arquivo_csv:
#   campos = ['PRODUTO', 'QUANTIDADE', 'PRECO']
#   escritor = csv.DictWriter(arquivo_csv, campos)
#   escritor.writeheader()
#   escritor.writerow({'PRODUTO': 'PASTEL', 'QUANTIDADE': 5, 'PRECO': 12.00})
#   escritor.writerow({'PRODUTO': 'CALDO DE CANA 500ML', 'QUANTIDADE': 5, 'PRECO': 8.00})
#   escritor.writerow({'PRODUTO': 'COXINHA', 'QUANTIDADE': 1, 'PRECO': 7.00})
#   escritor.writerow({'PRODUTO': 'EMPADA', 'QUANTIDADE': 2, 'PRECO': 6.00})

# MANIPULANDO DADOS
# with open("birthplace-2018-census-csv.csv", "r") as censo_csv:
#   leitor = csv.DictReader(censo_csv)
#   for linha in leitor:
#     if(int(linha['Census_night_population_count']) < 100):
#       print(f"Populacao de {linha['Birthplace']} tem menos de 100 pessoas")    

# Adicionando dados no final do arquivo
# escrevendo com listas
# with open("produto2.csv", "a", newline="") as arquivo_csv:
#   escritor = csv.writer(arquivo_csv)
#   escritor.writerow(['BANANA', 100, 50.00])

"""
EXERCICIOS

Leia o arquivo do censo e mostre apenas os lugares que no censo atual tem mais de 50.000 pessoas.
Crie um arquivo carros.csv com as colunas ano, modelo, preço. Adicione 8 carros ao arquivo.
Leia o arquivo produtos.csv e calcule o valor total de cada produto (preço x quantidade).
Adicione um novo produto ao arquivo produtos.csv sem apagar os dados existentes.
"""