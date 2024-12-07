import re

# O que são Expressões Regulares?
# Expressões Regulares (Regex) são padrões usados para buscar 
# ou manipular texto de forma eficiente. 
# No Python, o módulo re fornece suporte a regex.

texto = "Python é divertido"
vogais = re.findall(r"[aeioué]", texto)
print(vogais)

resultado = re.search(r"Joao", texto)
print(resultado)
if resultado:
  print("encontrou")
else:
  print("nao encontrou")


outro_texto = "minha string eh 79827943872947-aeiou"
modificado = re.sub(r"[0-9]", "*", outro_texto)
print(modificado)


"""
EXERCICIOS

1. Encontre todas as palavras começando com "P"
Texto: "Python é poderoso, prático e popular."

2. Substitua todas as vogais em uma frase por *
Texto: "Eu amo programação."

3. Verifique se uma string contém apenas números
Exemplo: "12345"
"""
