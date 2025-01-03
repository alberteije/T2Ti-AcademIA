import pandas as pd

# DataFrame
dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'Thor', 'Tony Stark', 'Bruce Wayne', 'Arthur Fleck', None, 'Bob', 'Carol'],
    'Idade': [12, 17, 18, 2000, 65, '90', 51, None, 30, 120],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Asgard', 'Nova Iorque', 'Gotham City', 'Gotham City', 'Sao Paulo', 'Rio de Janeiro', None]
}
df = pd.DataFrame(dados)

print(df)

print("=====================================================")
print("Identificacao de Problemas nos Dados")
print("=====================================================")
# detectar valores ausentes
print(df.isnull())
print(df.isnull().sum())

# identificar duplicatas
print(df.duplicated())

print("=====================================================")

print(df.info())
print(df['Idade'].unique())

print("=====================================================")
print("Tecnicas de Limpeza")
print("=====================================================")
# remover valores ausentes
df.dropna(inplace=True)
# print(df)

# preencher as colunas que tem dados ausentes
# df.fillna("AUSENTE", inplace=True)
# df['Idade'].fillna(999, inplace=True)
# print(df)

# removendo duplicatas
df.drop_duplicates(inplace=True)
print(df)

# Corrigindo Tipos de Dados
df['Idade'] = df['Idade'].astype(int)
print(df.info())

print("-------------------------")
# tratamento de dados inválidos - outliers
filtro_idades_irreais = df['Idade'] <= 120
print(filtro_idades_irreais)
print("-------------------------")
df_sem_idades_estranhas = df[filtro_idades_irreais]
print(df_sem_idades_estranhas)

print("=====================================================")
print("Transformacao de Dados")
print("=====================================================")
# renomeando colunas
df_sem_idades_estranhas.rename(columns={'Cidade': 'Municipio'}, inplace=True)
print(df_sem_idades_estranhas)

print("====================================")

""" 
FAIXA ETARIA  
0 a 18 (incluido) - Jovem
18 a 65 (incluido) - Adulto
65 a 120 (incluido) - Idoso
"""

retorno_do_corte = pd.cut(df_sem_idades_estranhas['Idade'], bins=[0, 18, 65, 120], labels=['Jovem', 'Adulto', 'Idoso'])
print(retorno_do_corte)

print("----------------------------------------------")

df_sem_idades_estranhas['Faixa Etaria'] = retorno_do_corte
print(df_sem_idades_estranhas)