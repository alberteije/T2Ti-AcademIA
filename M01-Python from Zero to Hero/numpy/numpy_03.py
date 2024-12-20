import numpy as np

"""
TRANSFORMAÇÕES

Reshape: Alterar a estrutura de arrays sem modificar os dados.
Slicing: Selecionar subconjuntos de dados para análise.
Filtros: Aplicar condições lógicas para extrair informações específicas.
"""

array = np.arange(12)
print("Array original:\n", array)

matriz = array.reshape(4, 3)
print("\nMatriz 4x3:\n", matriz)

matriz_2 = array.reshape(2, -1)
print("\nMatriz 2x6 (dimensao calculada automaticamente):\n", matriz_2)

vendas = np.random.randint(100, 500, size=(12, 3))
print("Matriz vendas:\n", vendas)

vendas_array = vendas.reshape(-1)
print("Array 1D:\n", vendas_array)

compras = np.array(
  [
    [100, 200, 300],  # Compras no dia 1 (produto 1, produto 2, produto 3)
    [110, 210, 310],  # Compras no dia 2
    [120, 220, 320],  # Compras no dia 3
  ]
)

compras_produto1 = compras[:, 0]
print("Compras do produto 1:\n", compras_produto1)

compras_acima_de_300 = np.where(compras > 300)
print("Compras acima de 300:\n", compras_acima_de_300)

valores_acima_de_300 = compras[compras_acima_de_300]
print("Valores acima de 300:\n", valores_acima_de_300)

marcara_valores_acima_de_300 = compras[compras > 300]
print("Mascara acima de 300:\n", marcara_valores_acima_de_300)

extract_acima_de_300 = np.extract(compras > 300, compras)
print("Extract acima de 300:\n", extract_acima_de_300)

# Agregações
total_vendas = vendas.sum()
media_vendas = vendas.mean()
max_venda = vendas.max()

print(f"Total de vendas no ano: {total_vendas}")
print(f"Media de vendas mensais: {media_vendas:.2f}")
print(f"Maior venda registrada: {max_venda}")

# Broadcasting
# Operações em arrays de tamanhos diferentes sem a necessidade de loops.
fator_crescimento = np.array([1.05, 1.10, 1.08])

vendas_ajustadas = vendas * fator_crescimento
print("Vendas ajustadas com fator de crescimento:\n", vendas_ajustadas)

"""
[
 [210 158 249]
 [308 179 147]
 [123 467 243]
 [199 112 386]
 [194 487 353]
 [152 438 411]
 [291 387 412]
 [146 347 139]
 [465 124 170]
 [386 207 460]
 [381 105 284]
 [120 429 437]
]

[
 [220.5  173.8  268.92]
 [323.4  196.9  158.76]
 [129.15 513.7  262.44]
 [208.95 123.2  416.88]
 [203.7  535.7  381.24]
 [159.6  481.8  443.88]
 [305.55 425.7  444.96]
 [153.3  381.7  150.12]
 [488.25 136.4  183.6 ]
 [405.3  227.7  496.8 ]
 [400.05 115.5  306.72]
 [126.   471.9  471.96]
]
"""