import re

arquivo = open("script-dados-modulo-agenda.txt", "r")
conteudo_atual = arquivo.read()
arquivo.close()
# arquivo = open("script-dados-modulo-agenda.txt", "w")
# linhas = ["mais conteudo 1 \n", "mais conteudo 2 \n", "mais conteudo 3 \n"]
# arquivo.writelines(linhas)
# arquivo.writelines(conteudo_atual)
# arquivo.close()

# contar as palavras do arquivo
# palavras = conteudo_atual.split("\n")

palavras = re.split(r"[ \n]", conteudo_atual)

print("total de palavras = ", len(palavras))
# print("conteudo da lista palavras = ", palavras)
print("Numero de vezes que aparece a palavra INSERT = ", palavras.count("INSERT"))

"""
DESAFIO

Crie um programa que copie o conteúdo de um arquivo para outro, 
mas substitua todas as ocorrências de uma palavra específica por outra 
(exemplo: trocar "Python" por "programação").
"""
