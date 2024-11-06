def saudacao(nome="um nome qualquer é um nome qualquer"):
    print(f"ola {nome}, tudo bem?");

def operacoes(a, b):
    soma = a + b # soma -> local
    diferenca = a - b # diferenca -> local
    return soma, diferenca
    

saudacao()
saudacao("EIJE")

x = 6 # global
y = 7 # global
resultado_soma, resultado_diferenca = operacoes(x, y)
print(f"A soma de {x} e {y} eh: {resultado_soma}")
print(f"A diferenca entre {x} e {y} eh: {resultado_diferenca}")


# funcao para calcular a media
def calcular_media(nota_a, nota_b, nota_c):
    media = (nota_a + nota_b + nota_c) / 3 # media -> local
    return media

media_aluno = calcular_media(5, 7, 9)
print(f"A media do aluno ficou em: {media_aluno}")