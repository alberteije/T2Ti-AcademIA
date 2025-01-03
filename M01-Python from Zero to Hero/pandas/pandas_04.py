import pandas as pd

# Leitura do arquivo
file_path = 'pandas/ProuniRelatorioDadosAbertos2020.csv'
df = pd.read_csv(file_path, sep=';', encoding='latin1')

print(df.head())
print(df.info())

print("------------------------------------------")
print("Limpeza Inicial e Preparacao dos Dados")
print("------------------------------------------")

# remover colunas irrelevantes
df = df.drop(columns=['CPF_BENEFICIARIO'])
print(df.info())

# conversão de dados - objeto (string) para data
df['DATA_NASCIMENTO'] = pd.to_datetime(df['DATA_NASCIMENTO'], format="%d/%m/%Y")
print(df.info())
print(df.dtypes)

print("------------------------------------------")
print("Analise simples - selecao e filtragem")
print("------------------------------------------")
# Quantas bolsas foram concedidas para cada região em 2020?
bolsas_por_regiao = df['REGIAO_BENEFICIARIO'].value_counts()
print("-------------------------------------------------------------------------")
print("quantas bolsas foram concedidas para cada regiao?")
print("-------------------------------------------------------------------------")
print(bolsas_por_regiao)

# Quantas bolsas integrais e parciais existem no dataset?
tipos_bolsa = df['TIPO_BOLSA'].value_counts()
print("-------------------------------------------------------------------------")
print("Quantas bolsas integrais e parciais existem no dataset?")
print("-------------------------------------------------------------------------")
print(tipos_bolsa)

# Proporcao da modalidade de ensino
proporcao_modalidade = df['MODALIDADE_ENSINO_BOLSA'].value_counts(normalize=True) * 100
print("-------------------------------------------------------------------------")
print("Qual a proporcao da modalidade de ensino?")
print("-------------------------------------------------------------------------")
print(proporcao_modalidade)


print("------------------------------------------")
print("Agrupamentos e estatisticas descritivas")
print("------------------------------------------")
# Idade média por região
df['IDADE'] = 2024 - df["DATA_NASCIMENTO"].dt.year
# print(df.head())
media_de_idade_por_regiao = df.groupby('REGIAO_BENEFICIARIO')['IDADE'].mean()
print("-------------------------------------------------------------------------")
print("Idade media por regiao")
print("-------------------------------------------------------------------------")
print(media_de_idade_por_regiao)

# Cursos mais populares
cursos_populares = df['NOME_CURSO_BOLSA'].value_counts().head(10)
print("-------------------------------------------------------------------------")
print("Quais os cursos mais populares? [Top 10]")
print("-------------------------------------------------------------------------")
print(cursos_populares)

# Distribuição por Sexo
distribuicao_por_sexo = df['SEXO_BENEFICIARIO'].value_counts()
distribuicao_por_sexo_proporcao = df['SEXO_BENEFICIARIO'].value_counts(normalize=True) * 100
print("-------------------------------------------------------------------------")
print("Distribuição por Sexo")
print("-------------------------------------------------------------------------")
print(distribuicao_por_sexo)
print(distribuicao_por_sexo_proporcao)

# Distribuicao por sexo com duas colunas
print("-------------------------------------------------------------------------")
print("Distribuicao por Sexo com duas colunas")
print("-------------------------------------------------------------------------")
distribuicao = pd.DataFrame(
  {
    'Quantidade': df['SEXO_BENEFICIARIO'].value_counts(),
    'Proporcao (%)': df['SEXO_BENEFICIARIO'].value_counts(normalize=True) * 100
  }
)
print(distribuicao)

# Distribuicao por raça com duas colunas
print("-------------------------------------------------------------------------")
print("Distribuicao por Raca com duas colunas")
print("-------------------------------------------------------------------------")
distribuicao = pd.DataFrame(
  {
    'Quantidade': df['RACA_BENEFICIARIO'].value_counts(),
    'Proporcao (%)': df['RACA_BENEFICIARIO'].value_counts(normalize=True) * 100
  }
)
print(distribuicao)

"""
- Filtrar o dataframe para mostrar apenas beneficiários de Marketing em Fortaleza.
- Encontrar a porcentagem de beneficiários por UF (estado).
- Criar uma nova coluna que classifica os beneficiários por faixa etária:
	- Jovens: até 25 anos
	- Adultos: entre 26 e 50 anos
	- Idosos: acima de 50 anos
"""