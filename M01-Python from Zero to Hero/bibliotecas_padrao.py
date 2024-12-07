import math
from datetime import datetime, timedelta
import os
import sys
import random

print("Pi:", math.pi)
print("Raiz quadrada de 16:", math.sqrt(16))
print("Seno de 30 graus:", math.sin(math.radians(30)))

agora = datetime.now()
print("Data e hora atual:", agora)
print("Data formatada:", agora.strftime("%d/%m/%Y %H:%M:%S"))
print("Data daqui a 7 dias:", agora + timedelta(days=7))

print("Diretório atual:", os.getcwd())
print("Listar arquivos no diretório:", os.listdir())
# os.mkdir("nova_pasta")
print("Pasta 'nova_pasta' criada com sucesso!")

print("Versão do Python:", sys.version)
print("Argumentos de linha de comando:", sys.argv)
# sys.exit("Encerrando o programa")

print("Número aleatório entre 1 e 10:", random.randint(1, 10))
lista = ["pera", "banana", "laranja"]
print("Escolha aleatória de lista:", random.choice(lista))

"""
- Exercícios Práticos

=== Criar um programa que:

Gera um número aleatório entre 1 e 100.
Pergunta ao usuário um número.
Informa se o número está acima ou abaixo do número gerado.
Permite que o usuário continue tentando até acertar, e imprime quantas tentativas ele fez.

=== Crie um script que:

Pede ao usuário um nome de arquivo.
Usa 'os' para verificar se o arquivo existe.
Usa 'datetime' para registrar a data e hora de execução do programa.

"""




