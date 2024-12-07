from datetime import date, time, datetime, timedelta, timezone

# criar uma data especifica
data_nascimento = date(1982, 12, 25)
print("data de nascimento", data_nascimento)

# criar hora especifica
hora_inicio = time(18, 30)
print("hora de inicio", hora_inicio)

# hora atual
hora_atual = datetime.now()
print("hora atual", hora_atual)

# hora especifica
evento = datetime(2025, 1, 12, 18, 45, 30)
print("evento", evento)

# criando intervalo
intervalo = timedelta(days=5, hours=10)
print("intervalo", intervalo)
print(hora_atual+intervalo)
print(evento-hora_atual)

# criar uma data com fuso horario
timezone_brazil = timezone(timedelta(hours=-3))
date_utc = datetime.now(timezone_brazil)
print("date utc", date_utc)

# formatação das datas
print("hora atual formatada:", hora_atual.strftime("%d/%m/%Y %H:%M:%S"))
print("apenas a data:", hora_atual.strftime("%d/%b/%Y"))
print("apenas a hora:", hora_atual.strftime("%H:%M:%S"))

# Convertendo uma string para datetime
data_str = "12-11-2024 14:45"
data_convertida = datetime.strptime(data_str, "%d-%m-%Y %H:%M")
print("Data convertida:", data_convertida)

print(intervalo+data_convertida)

"""
== Exercício 1: Manipulação de Datas e Horários
Objetivo: Criar e manipular objetos datetime.

Instruções:

Crie um programa que peça ao usuário para informar sua data de nascimento no formato DD/MM/AAAA.
Converta essa data para um objeto datetime.
Exiba a data de nascimento do usuário no formato completo (ex.: "Dia: 25 de Dezembro de 1982").
Adicione 100 dias à data de nascimento e exiba a nova data.

== Exercício 2: Calculando a Diferença entre Datas
Objetivo: Calcular a diferença entre duas datas.

Instruções:

Crie um programa que peça ao usuário para informar duas datas no formato DD/MM/AAAA.
Converta as datas informadas em objetos datetime.
Calcule e exiba a diferença em dias entre as duas datas.

== Exercício 3: Trabalhando com Fusos Horários
Objetivo: Trabalhar com fusos horários usando a classe timezone e calcular horários em diferentes fusos.

Instruções:

Crie um programa que exiba a hora atual no fuso horário UTC (horário universal coordenado).
Crie variáveis para representar os fusos horários de alguns países (por exemplo, UTC-3, UTC+2, UTC+5).
Exiba a hora atual nos três fusos horários informados.
"""