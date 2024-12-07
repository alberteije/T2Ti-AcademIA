import json

# json.load = carrega de um arquivo JSON
# json.loads = converte de uma string json
# json.dump = salva para um arquivo json
# json.dumps = converte para uma string

with open("nfe-emissao.json", "r") as arquivo_json:
  dados = json.load(arquivo_json)
  # print(dados)
  # print(dados.keys())
  nfeDestinatario = dados['nfeDestinatario']
  print(nfeDestinatario)
  valorTotalDaNota = dados['valorTotal']
  print(f"valor total da nota = R$ {valorTotalDaNota:.2f}")
  dados['valorTotal'] = 50000

with open("nfe-destinatario.json", "w") as arquivo_destinatario:
  json.dump(nfeDestinatario, arquivo_destinatario, indent=2)

with open("nfe-emissao.json", "w") as arquivo_alterado:
  json.dump(dados, arquivo_alterado, indent=2)


"""
Exercicio

01-Crie um arquivo JSON com uma lista de produtos (nome, preço e estoque).
02-Leia os dados do arquivo e exiba apenas os produtos que têm estoque maior que 10.
03-Adicione um novo produto ao arquivo JSON.
"""
