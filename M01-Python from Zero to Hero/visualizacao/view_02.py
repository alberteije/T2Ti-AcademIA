import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

dados = {
    'Categoria': ['A', 'B', 'C', 'D'],
    'Valores': [23, 45, 56, 78]
}
df = pd.DataFrame(dados)

# ==================================================
# Gráfico de Barras
# ==================================================

# quando usar: comparar categorias

# --  usando apenas o matplotlib
# plt.bar(df['Categoria'], df['Valores'], color='skyblue')
# plt.title("Exemplo de Gráfico de Barras")
# plt.xlabel("Categoria")
# plt.ylabel("Valores")
# plt.show()

# --  usando o Seaborn
# sns.barplot(x='Categoria', y='Valores', data=df, palette='pastel')
# plt.title("Exemplo de Gráfico de Barras com Seaborn")
# plt.show()

"""
EXERCICIO:
Criar um gráfico de barras mostrando o número de bolsas por região usando o dataset do Prouni.
"""

# ==================================================
# Gráfico de Linhas
# ==================================================

# quando usar: visualizar tendências ao longo do tempo. Ex: concessão de bolsas por ano

# --  usando apenas o matplotlib
tempo = ['2020', '2021', '2022', '2023']
valores = [150, 200, 250, 300]

# plt.plot(tempo, valores, marker='D', color='green')
# plt.title("Exemplo de Gráfico de Linhas")
# plt.xlabel("Ano")
# plt.ylabel("Quantidade")
# plt.grid(True)
# plt.show()

# --  usando o Seaborn
data = {
  'Ano': tempo,
  'Quantidade': valores
}
df_linhas = pd.DataFrame(data)

# sns.lineplot(x='Ano', y='Quantidade', data=df_linhas, marker='o')
# plt.title("Exemplo de Gráfico de Linhas com Seaborn")
# plt.grid(True)
# plt.show()

"""
EXERCICIO
Criar um gráfico de linhas mostrando a distribuição de bolsas por ano.
"""

# ==================================================
# Gráfico de Dispersão
# ==================================================

# quando usar: explorar a relação entre duas variáveis. Ex: idade do beneficiário e quantidade de bolsas

idade = [18, 22, 25, 30, 35, 40, 45, 50]
quantidade = [5, 15, 30, 45, 50, 65, 70, 90]

# --  usando apenas o matplotlib
plt.scatter(idade, quantidade, color='purple')
plt.title("Exemplo de Gráfico de Dispersão")
plt.xlabel("Idade")
plt.ylabel("Quantidade")
plt.show()

# --  usando o Seaborn
data_disp = {
  'Idade': idade,
  'Quantidade': quantidade
}
df_disp = pd.DataFrame(data_disp)

sns.scatterplot(x='Idade', y='Quantidade', data=df_disp, color='purple')
plt.title("Exemplo de Gráfico de Dispersão com Seaborn")
plt.show()

"""
EXERCICIO
Criar um gráfico de dispersão para analisar a relação entre a idade dos beneficiários e a concessão de bolsas.
"""