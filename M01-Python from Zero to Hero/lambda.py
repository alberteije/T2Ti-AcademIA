def soma(a, b):
    return a + b

print(soma(10, 40))

retorno = lambda a, b: a + b
print(retorno(35, 56))

#funções de ordem superior????
# funções que podem receber outras funções como parâmetros e podem retornar funções

# map - aplica uma função a cada item de uma lista
# def quadrado(numero):
#     return numero ** 2

lista = [1, 2, 3, 4, 5]

lista_ao_quadrado = list(map(lambda numero: numero ** 2, lista)) 
print(lista_ao_quadrado)

# sorted - orderna uma lista com base numa função de chave
def obter_idade(aluno):
    return aluno[1]

alunos = [("albert", 33), ("pedro", 56), ("maria", 12)]

alunos_ordenados_por_idade = sorted(alunos, key=obter_idade)
print(alunos_ordenados_por_idade)

alunos_ordenados_por_nome = sorted(alunos, key=lambda aluno: aluno[0])
print(alunos_ordenados_por_nome)


# filter - filtrar elementos de uma lista com base em uma condição
numeros = [5, 10, 15, 20, 25, 30]
numero_maiores_que_10 = list(filter(lambda numero: numero > 10, numeros))
print(numero_maiores_que_10)