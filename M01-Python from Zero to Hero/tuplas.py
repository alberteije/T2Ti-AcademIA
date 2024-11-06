minha_tupla = (1, "dois", 3, "quatro", 1, 5.5, "seis", ['outra lista?'], 3)
print(minha_tupla)

outra_tupla = list(range(5))
print(outra_tupla)

print(minha_tupla[3])
# minha_tupla[3] = "outro valor qualquer"
print(minha_tupla[3])

print(minha_tupla.count(90))

if 50 in minha_tupla:
  print(minha_tupla.index(50))