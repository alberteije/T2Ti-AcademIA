nome = "Albert"
idade = 67
altura = 1.75
eh_estudante = True

if idade != altura:
    print("idade diferente de altura")
else:
    print("idade igual a altura")

if idade < 16:
    print("nao pode votar")
elif idade < 18 or idade >= 65:
    print("voto facultativo") 
else:
    print("voto obrigatorio")
       
if not idade >= 18:
    print("adulto")


# print("esse sera sempre impresso")

# ==: Igual a
# !=: Diferente de
# > e <: Maior que, menor que
# >= e <=: Maior ou igual a, menor ou igual a