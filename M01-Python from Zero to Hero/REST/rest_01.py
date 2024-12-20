import requests

url = "https://jsonplaceholder.typicode.com/posts/"

resposta = requests.get(url)

print(resposta)

if resposta.status_code == 200:
  print("deu certo")
  dados = resposta.json()
  # print(dados)

  # for postagem in dados:
  #   print(f"o id do post eh {postagem['id']}, o titulo da postagem eh '{postagem['title']}'")

  for postagem in dados:
    print(f"o body do post eh {postagem['body']}")

  # for postagem in dados:
  #   print(postagem)


""" 
EXERCICIO:

Implemente os métodos POST, PUT e DELETE para a mesma API REST utilizada aqui
"""