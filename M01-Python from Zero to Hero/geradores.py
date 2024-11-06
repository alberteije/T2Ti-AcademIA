import time

def calcular_quadrados(n):
    return [i ** 2 for i in range(n)]

tempo_inicial = time.time()
resultado_normal = [] # calcular_quadrados(100000000)
tempo_final = time.time()
print("---------------------------")
print("tempo gasto na lista: ", tempo_final - tempo_inicial)
print("---------------------------")

def gerar_quadrados(n):
    for i in range(n):
        yield i ** 2

tempo_inicial = time.time()
retorno_gerador = gerar_quadrados(1000000000)
contador = 0
for item in retorno_gerador:
    contador += 1
tempo_final = time.time()
print("---------------------------")
print("tempo gasto no gerador: ", tempo_final - tempo_inicial)
print("quantidade de quadrados = ", contador)
print("---------------------------")

print("==========================================")
print("consumo de memória")
print("==========================================")

import sys

memoria_lista = sys.getsizeof(resultado_normal)
memoria_gerador = sys.getsizeof(retorno_gerador)

print("memoria usada pela lista = ", memoria_lista)
print("memoria usada pelo gerador = ", memoria_gerador)