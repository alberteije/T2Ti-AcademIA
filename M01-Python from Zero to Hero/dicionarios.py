dic = { 
  "nome": "albert",
  "idade": 29,
  "altura": 1.75,
  "brasileiro": True,
}

print(dic)
print(f"o valor da chave 'nome' eh {dic["nome"]}")
dic["nomi"] = "pedro"
print(dic)
# print(dic["noma"])

print(dic.get("noma", "nao existe a chave noma"))

retorno = dic.pop("nomi")
print(retorno)
print(dic)
retorno = dic.pop("nomi", "a chave nomi nao existe")
print(retorno)

# del dic["idade"]
# print(dic)

for chave in dic:
  print(chave, dic[chave])
print("-----------------------------")
for chave, valor in dic.items():
  print(chave, valor)
print("-----------------------------")
for chave in dic.keys():
  print(chave, "=", dic[chave])
print("-----------------------------")
for valor in dic.values():
  print(valor)

#Criar um dicionário para representar uma biblioteca, onde as chaves são títulos de livros e os valores são autores.
#Implementar funções para adicionar, remover e listar livros.