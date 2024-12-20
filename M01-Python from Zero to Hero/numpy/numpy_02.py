import numpy as np
import locale

def converter_com_virgula(valor):
  return float(valor.replace(',', '.'))

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

dados = np.genfromtxt(
  'numpy/RemuneracaoAtivos.csv', 
  delimiter=';', 
  dtype=None, 
  encoding='latin1',
  names=True,
  converters={
    3: converter_com_virgula,
    5: converter_com_virgula,
    6: converter_com_virgula,
  }
)

dados.dtype.names = tuple(name.replace(' ', '_') for name in dados.dtype.names)

remuneracao_mes = dados['REMUNERAÇÃO_DO_MÊS']
pagamentos_eventuais = dados['PAGAMENTOS_EVENTUAIS']
licenca_premio = dados['LICENÇA_PRÊMIO_INDENIZADA']
salario_minimo = 1500

soma_salarios = np.sum(remuneracao_mes)
print(f"total de salarios de todos os servidores {locale.currency(soma_salarios, grouping=True)}")
media_salarios = np.mean(remuneracao_mes)
print(f"media do salarios de todos os servidores {locale.currency(media_salarios, grouping=True)}")

soma_eventuais = np.sum(pagamentos_eventuais)
print(f"total de pagamentos eventuais de todos os servidores {locale.currency(soma_eventuais, grouping=True)}")
media_eventuais = np.mean(pagamentos_eventuais)
print(f"media dos pagamentos eventuais de todos os servidores {locale.currency(media_eventuais, grouping=True)}")

soma_lp = np.sum(licenca_premio)
print(f"total de licencas premios de todos os servidores {locale.currency(soma_lp, grouping=True)}")
media_lp = np.mean(licenca_premio)
print(f"media das licencas premios de todos os servidores {locale.currency(media_lp, grouping=True)}")

total_salarios_minimos = soma_salarios / salario_minimo
print(f"total de salarios minimos pagos para os servidores {total_salarios_minimos:.2f}")