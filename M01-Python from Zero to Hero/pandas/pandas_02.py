import pandas as pd

# DataFrame
dados = {
  'Nome': ['Alice', 'Bob', 'Carol', 'Thor', 'Tony Stark', 'Bruce Wayne', 'Arthur Fleck'],
  'Idade': [25, 30, 35, 2000, 45, 42, 51],
  'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Asgard', 'Nova Iorque', 'Gotham City', 'Gotham City']
}
df = pd.DataFrame(dados)

# Seleção de Dados
print("--------------------------------------")
print("selecao de colunas")
print("--------------------------------------")
print(df['Nome'])
print(df[['Nome', 'Cidade', 'Idade']])

print("--------------------------------------")
print("selecao de linhas")
print("--------------------------------------")
# -- por rótulo
print(df.loc[0])
# -- por posicao
print(df.iloc[0])

print("--------------------------------------")
print("alterando os rotulos")
print("--------------------------------------")
indices = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
df = pd.DataFrame(dados, index=indices)
print(df)

print("--------------------------------------")
print("selecao de linhas com rotulos alterados")
print("--------------------------------------")
# -- por rótulo
print(df.loc['A1'])
# -- por posicao
print(df.iloc[0])

print("--------------------------------------")
print("selecao de linhas com coluna especifica")
print("--------------------------------------")
# -- por rótulo
print(df.loc['A1', 'Nome'])

print("--------------------------------------")
print("selecao de multiplas linhas")
print("--------------------------------------")
# -- por rótulo
print(df.loc[['A3', 'A4', 'A5']])
print(df.loc['A3':'A5'])
print("--------------------------------------")
print("concatenacao")
print("--------------------------------------")
intervalo = pd.concat([df.loc['A1':'A3'], df.loc['A5':'A7']])
print(intervalo)

## FILTROS
print("--------------------------------------")
print("filtrando pela idade")
print("--------------------------------------")
print(df['Idade'] > 30)
dataframe_filtrado = df[df['Idade'] > 30]
# máscara booleana
print("--------------------------------------")
print("dataframe_filtrado")
print("--------------------------------------")
print(dataframe_filtrado)

print("--------------------------------------")
print("filtro com combinacoes")
print("--------------------------------------")
filtro = (df['Idade'] > 30) & (df['Cidade'] == 'Gotham City')
outro_df_filtrado = df[filtro]
print(outro_df_filtrado)

filtro = (df['Idade'] > 30) | (df['Cidade'] == 'Sao Paulo')
outro_df_filtrado2 = df[filtro]
print(outro_df_filtrado2)

## Agregação de Dados
print("--------------------------------------")
print("Agregacao de Dados")
print("--------------------------------------")
print(f" media de idades: {df['Idade'].mean()}")
print(f" soma de idades: {df['Idade'].sum()}")
print(f" maximo das idades: {df['Idade'].max()}")
print(f" minimo das idades: {df['Idade'].min()}")

print("--------------------------------------")
print("media de idades por cidade")
print("--------------------------------------")
media_de_idade_por_cidade = df.groupby('Cidade')['Idade'].mean()
print(media_de_idade_por_cidade)
