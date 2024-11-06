meu_conjunto = {1, "dois", 3, "quatro", 5, 5.5, "seis", 1, 1, 1}
print(meu_conjunto) 

conjunto01 = {1, 2, 3, 4, 5}
conjunto02 = {4, 5, 6, 7, 8}

# uniao
# uniao = conjunto01.union(conjunto02)
uniao = conjunto01 | conjunto02
print(uniao)

# interseção
# intersecao = conjunto01.intersection(conjunto02)
intersecao = conjunto01 & conjunto02
print(intersecao)

# diferença
# diferenca = conjunto01.difference(conjunto02)
diferenca = conjunto01 - conjunto02
print(diferenca)

# diferença simétrica
# diferenca_simetrica = conjunto01.symmetric_difference(conjunto02)
diferenca_simetrica = conjunto01 ^ conjunto02
print(diferenca_simetrica)