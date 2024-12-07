with open("script-dados-modulo-agenda.txt", "r") as arquivo:
  conteudo_atual = arquivo.read()
  print(conteudo_atual)

with open("script-dados-modulo-agenda1.txt", "a") as arquivo:
  arquivo.write("adicionado no final do arquivo")