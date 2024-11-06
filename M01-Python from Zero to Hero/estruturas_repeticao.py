import random

for i in range(1, 10, 1):
    if i == 5:
        continue
    print(i)

# for i=0, i<10, i++

print("------------------------------------------")

contador = 1
while contador < 10:
    if contador == 3:
        contador += 2
        continue
    print(contador)
    contador = contador + 2



numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break  # Sai do laço quando o número é adivinhado
    elif palpite < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")


# resposta = ""
# while resposta != "sim":
#   resposta = input("voce esta gostando do video?")


# print(resposta)