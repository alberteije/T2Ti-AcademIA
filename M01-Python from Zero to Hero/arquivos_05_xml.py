# import xml.etree.ElementTree as ET
from lxml import etree

# carregar um arquivo xml
arvore = etree.parse("nfe.xml")
raiz = arvore.getroot()
print(raiz)

# definindo o namespace
NS = {"nfe": "http://www.portalfiscal.inf.br/nfe"}

# listar valor do elemento cUF na tag <ide>
ide = arvore.find(".//nfe:ide", NS)
print(ide)

if ide is not None:
  cUf = ide.find("nfe:cUF", NS)
  print(f"valor da tag cUF = {cUf.text}")

# alterar o nome do emitente
emitente = arvore.find(".//nfe:emit", NS)
print(emitente)

if emitente is not None:
  xNome = emitente.find("nfe:xNome", NS)
  print(f"valor da tag xNome = {xNome.text}")
  xNome.text = "Outra Empresa"
  print(f"valor da tag xNome = {xNome.text}")

# adicionando novas informações no xml
info_adicional = etree.Element("{http://www.portalfiscal.inf.br/nfe}InfoAdicionalT2Ti")
info_adicional.text = "Informação Adicionada pela Aplicação"
ide.append(info_adicional)

arvore.write("nfe2.xml", encoding="utf-8")

"""
EXERCICIO

Carregue um arquivo XML de nota fiscal (você pode usar um arquivo de exemplo que 
foi fornecido).

Extraia e exiba as seguintes informações:

O número da nota fiscal (<nNF>) dentro da tag <ide>.
A data de emissão (<dhEmi>) dentro da tag <ide>.
O nome do emitente (<xNome>) dentro da tag <emit>.

Salve as informações extraídas em um novo arquivo de texto 
(notas_fiscais.txt) no seguinte formato:

Nota Fiscal: [nNF]
Data de Emissão: [dhEmi]
Emitente: [xNome]
"""
