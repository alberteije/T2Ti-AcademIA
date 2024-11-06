minha_lista = [1, "dois", 3, "quatro", 5, 5.5, "seis", ['outra lista?'], 3, 3, 3]
print(minha_lista)

outra_lista = list(range(5))
print(outra_lista)

print(minha_lista[3])
minha_lista[3] = "outro valor qualquer"
print(minha_lista[3])


print(minha_lista[-2])

minha_lista.append("ultimo")

print(minha_lista[8])

minha_lista.insert(3, 3.5)
print("1=", minha_lista)

# minha_lista.extend([1,2,3,2,4,2,5,2])
# minha_lista.extend(outra_lista)
# print(minha_lista)
if 2 in minha_lista:
  minha_lista.remove(2)

print("2=",minha_lista)

# retorno = minha_lista.pop(8)
del minha_lista[8]

print("3=",minha_lista)
# print(f"o valor removido da lista = {retorno}")

for item in minha_lista:
    print(item)

print("=======================================")

i=0
while i < len(minha_lista):
   print(f"o valor que se encontra na posicao {i} eh o {minha_lista[i]}")
   i = i + 1