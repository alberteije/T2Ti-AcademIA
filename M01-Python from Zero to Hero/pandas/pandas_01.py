import pandas as pd

# Series
dados = [10, 20, 30, 40, 50, 60]
serie = pd.Series(dados, index=['a', 'b', 'c', 'd', 'e', 'f'])
print(serie)
print(serie['a'])
print(serie.iloc[0])
print(serie + 10)

# DataFrame
dados = {
  'Nome': ['Alice', 'Bob', 'Carol', 'Thor', 'Tony Stark', 'Bruce Wayne', 'Arthur Flak'],
  'Idade': [25, 30, 35, 2000, 45, 42, 51],
  'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Asgard', 'Nova Iorque', 'Gothan City', 'Gothan City']
}
df = pd.DataFrame(dados)
print(df)
print(df.head(2))
print(df.tail(2))
print("==========================================")
print(df['Nome'])
print("----------------------------------------")
print(df.loc[0])
print("==========================================")
df['Loucura'] = [12, 15, 45, 60, 70, 80, 100]
print(df)
print("----------------------------------------")
df = df.drop('Loucura', axis=1)
print(df)