import numpy as np

precos = np.random.rand(1_000_000) * 100
media_precos = np.mean(precos)
# print(precos[:50])
print(f"a media de precos eh {media_precos:.2f}")
print(f"a soma de precos eh {np.sum(precos):.2f}")

# criando array
## array unidimensional - vetor
vendas = np.array([100, 200, 500, 234, 567, 789, 123, 456, 876, 345])
print(f"valor total das vendas: {np.sum(vendas)}")

## array bidimensional - matriz
vendas_por_regiao = np.array(
  [
    [100, 200, 300], # regiao 01
    [400, 500, 600], # regiao 02
    [100, 400, 200], # regiao 03
    [500, 400, 100], # regiao 04
  ])
print(f"vendas por regiao: {np.sum(vendas_por_regiao, axis=1)}")

## arrays multidimensionais
vendas_semanal = np.random.randint(50, 500, (3, 7, 4))
print(vendas_semanal)
print(f"media mensal por produto: {np.mean(vendas_semanal, axis=(1, 2))}")

vendas_semanal_por_semana = np.sum(vendas_semanal, axis=1)
print(vendas_semanal_por_semana)
media_semanal_por_produto = np.mean(vendas_semanal_por_semana, axis=1)
print(f"media semanal por produto: {media_semanal_por_produto}")


"""
DIMENSÃO 0 = PRODUTOS
DIMENSÃO 1 = DIAS
DIMENSÃO 2 = SEMANAS

[
  [ PRODUTO 01
    [387 148 436 383] # Vendas do dia 1 para as quatro semanas
    [305 222 462 223] # Vendas do dia 2 para as quatro semanas
    [384 346 174 103] # Vendas do dia 3 para as quatro semanas
    [151 308 493  93]
    [498 116 277  51]
    [ 96 128 305 117]
    [314 467 129 391]
  ]

  [ PRODUTO 02
    [422 415 357 106]
    [379 390 195  96]
    [239  95 128 108]
    [369 413 419 400]
    [261 440 269 438]
    [212  70 312 484]
    [328 490 182  56]
  ]

  [ PRODUTO 03
    [ 63 165 489 206]
    [479 221 273 415]
    [343  86 310 260]
    [415  80 170 305]
    [189 430 106 384]
    [ 75 411  77 285]
    [267 286 459 430]
  ]
]
"""

# operações matemáticas básicas
vendas = np.array([100, 200, 500, 234, 567, 789, 123, 456, 876, 345])
quantidades = np.array([10, 2, 5, 23, 15, 12, 15, 10, 1, 9])
lucro = vendas * quantidades
print("lucro:", lucro)

vendas_atualizadas = vendas * 1.1
print("vendas atualizadas: ", vendas_atualizadas)