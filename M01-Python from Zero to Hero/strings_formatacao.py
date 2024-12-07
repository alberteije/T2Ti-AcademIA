nome = "Albert"
idade  = 37
valor = 123.4567

print("Meu nome eh", nome, "e minha idade eh", idade)

# f-strings
# interpolação - interpolar
print("----------------------")
print("usando o f-strings")
print("----------------------")

print(f"Meu nome eh {nome} e minha idade eh {idade}")
print(f"o dobro da minha idade eh {idade * 2}")

print(f"o valor eh {valor:.2f}")

# .format
print("----------------------")
print("usando o .format")
print("----------------------")
print("Meu nome eh {nn} e minha idade eh {ii}".format(nn=nome, ii=idade))

print("o valor eh {:.2f}".format(valor))

# usando o % - desencorajado
print("----------------------")
print("usando o %")
print("----------------------")
print("Meu nome eh %s e minha idade eh %d" % (nome, idade))

"""
Exercício 1:
Crie uma mensagem que exiba o nome de uma pessoa, sua idade e a cidade onde mora, utilizando:

f-strings
.format()

Exercício 2:
Formate um número decimal com 3 casas decimais usando f-strings e .format().

Exercício 3:
Crie uma tabela de produtos com nome, quantidade e preço formatados em colunas alinhadas.
"""
