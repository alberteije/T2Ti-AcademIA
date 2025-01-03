import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# cofigurar estilo do Seaborn
sns.set_theme(style="whitegrid")

# Leitura do arquivo do PROUNI
file_path = 'pandas/ProuniRelatorioDadosAbertos2020.csv'
df = pd.read_csv(file_path, sep=';', encoding='latin1')

# Distribuição por Sexo
distribuicao_por_sexo = df['SEXO_BENEFICIARIO'].value_counts()
distribuicao_por_sexo_proporcao = df['SEXO_BENEFICIARIO'].value_counts(normalize=True) * 100
print("-------------------------------------------------------------------------")
print("Distribuição por Sexo")
print("-------------------------------------------------------------------------")
print(distribuicao_por_sexo)
print(distribuicao_por_sexo_proporcao)

print("index")
print(distribuicao_por_sexo.index)
print("values")
print(distribuicao_por_sexo.values)

# Criar gráfico de barras usando apenas o matplotlib
# plt.bar(distribuicao_por_sexo.index, distribuicao_por_sexo.values, color=['skyblue', 'salmon'])
# plt.title("Distribuição de bolsas por Sexo")
# plt.xlabel("Sexo")
# plt.ylabel("Quantidade")
# plt.show()

# Criar gráfico de barras usando o Seaborn
# sns.barplot(x=distribuicao_por_sexo.index, y=distribuicao_por_sexo.values, palette='pastel')
# plt.title("Distribuição de bolsas por Sexo")
# plt.xlabel("Sexo")
# plt.ylabel("Quantidade")
# plt.show()

# Criar gráfico de barras usando o Seaborn - Personalizado
# plt.figure(figsize=(10, 4))
# sns.barplot(x=distribuicao_por_sexo.index, y=distribuicao_por_sexo.values, palette='coolwarm')
# plt.title("Distribuição de bolsas por Sexo", fontsize=18)
# plt.xlabel("Sexo", fontsize=12)
# plt.ylabel("Quantidade", fontsize=12)
# plt.xticks(fontsize=8)
# plt.yticks(fontsize=8)
# plt.show()

#Criar gráfico de pizza usando apenas o matplotlib
plt.pie(distribuicao_por_sexo.values, 
        labels=distribuicao_por_sexo.index, 
        colors=['skyblue', 'salmon'],
        autopct="%1.2f%%"
      )
plt.title("Distribuição de bolsas por Sexo - Pizza")
plt.show()

"""
EXERCICIO

1-Criar gráficos básicos com Matplotlib e Seaborn para os seguintes campos do dataset:
-- TIPO_BOLSA (Gráfico de barras).
-- MODALIDADE_ENSINO_BOLSA (Gráfico de pizza).
2-Experimentar customizações como alteração de cores, títulos e tamanhos.
"""