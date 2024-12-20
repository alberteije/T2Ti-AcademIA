import os
import shutil

def organizar_arquivos(pasta):
  lista_arquivos = os.listdir(pasta)
  # print(lista_arquivos)

  for arquivo in lista_arquivos:
    caminho_completo = os.path.join(pasta, arquivo)
    # print(pasta)
    # print(arquivo)
    # print(caminho_completo)
    if os.path.isfile(caminho_completo):
      _, extensao_arquivo = os.path.splitext(arquivo)
      # print(_, extensao_arquivo)

      # print("antes: ", extensao_arquivo)
      extensao_arquivo = extensao_arquivo.lstrip(".").lower()
      # print("depois: ", extensao_arquivo)

      # criar subpasta
      subpasta = os.path.join(pasta, extensao_arquivo)
      os.makedirs(subpasta, exist_ok=True)

      # mover os arquivos para dentro das subpastas
      novo_caminho = os.path.join(subpasta, arquivo)
      shutil.move(caminho_completo, novo_caminho)

pasta_alvo = "automacao"
organizar_arquivos(pasta_alvo)