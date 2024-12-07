import os
import pathlib

print("---------------------------------")
print("Usando o modulo os")
print("---------------------------------")
print(os.getcwd())
print("Listando os arquivos do diretorio atual", os.listdir())
# os.mkdir("eije")
# os.rmdir("eije")
caminho_os = os.path.join(os.getcwd(), "conjuntos.py")
print("o caminho eh = ", caminho_os)
print("eh arquivo?", os.path.isfile("conjuntos.py"))
print("eh diretorio?", os.path.isdir("erp"))

print("---------------------------------")
print("Usando o modulo pathlib")
print("---------------------------------")
print(pathlib.Path.cwd())
print("Listando os arquivos do diretorio atual", list(pathlib.Path(".").iterdir()))
# pathlib.Path("eije").mkdir()
# pathlib.Path("eije").rmdir()
caminho_path = pathlib.Path(pathlib.Path.cwd()) / "conjuntos.py"
print("o caminho eh = ", caminho_path)

print("eh arquivo?", caminho_path.is_file())
print("eh diretorio?", caminho_path.is_dir())

"""
1. Navegar e listar arquivos
Liste os arquivos e pastas no diretório atual.
Identifique quais são arquivos e quais são pastas.
2. Criar e remover diretórios
Crie uma pasta chamada teste.
Dentro dela, crie outra pasta chamada subteste.
Remova as duas pastas.
3. Trabalhar com caminhos
Combine o caminho atual com o nome de um arquivo fictício, meuarquivo.txt, e exiba o caminho resultante.
"""




