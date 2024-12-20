import requests
from bs4 import BeautifulSoup

url = "https://t2ti.com"
cabecalhos = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

resposta = requests.get(url, headers=cabecalhos)
# print(resposta)

if resposta.status_code == 200:
  # print("requisição bem sucedida!")
  conteudo_html = resposta.text
  # print(conteudo_html)
  soup = BeautifulSoup(conteudo_html, 'html.parser')
  # print(soup.head)
  # print(soup.title)

  print(f"O titulo da pagina eh: {soup.title.string}")