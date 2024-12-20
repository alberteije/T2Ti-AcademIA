# from flask import Flask, request, jsonify
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, field_validator
from bd.mysql import Pessoa, Session as DatabaseSession

app = FastAPI()

def get_session():
  sessao = DatabaseSession()  
  try:
    yield sessao
  finally:
    sessao.close()

class PessoaInput(BaseModel):
  nome: str
  idade: int

  @field_validator('nome')
  def nome_nao_branco(cls, v):
    # python - a string vazia é igual a False
    # o método strip() remove os espaços em branco de uma string
    # v = "   joao " -- v.strip() -->>> "joao"
    # "joao" em booleano é igual a True
    # "" em booleano é igual a False
    # "    " em booleano é igual true
    if not v.strip(): 
      raise ValueError('O nome não pode estar em branco.')
    return v    

# GET
@app.get('/pessoas', response_model=list[dict])
def listar_pessoas(db=Depends(get_session)):
  """
    Esse endpoint vai devolver as pessoas que estão armazenadas na aplicação
  """
  lista_pessoas = db.query(Pessoa).all()
  return [{'id': p.id, 'nome': p.nome, 'idade': p.idade} for p in lista_pessoas]

# POST
@app.post('/pessoas', response_model=dict, status_code=201)
def adicionar_pessoa(pessoa_que_veio_na_requisicao: PessoaInput, db=Depends(get_session)):
  pessoa = Pessoa()
  pessoa.nome = pessoa_que_veio_na_requisicao.nome
  pessoa.idade = pessoa_que_veio_na_requisicao.idade
  db.add(pessoa)
  db.commit()  
  return {'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}

# PUT
@app.put('/pessoas/{id}', response_model=dict)
def atualizar_pessoa(id: int, pessoa_que_veio_na_requisicao: PessoaInput, db=Depends(get_session)):
    pessoa_no_banco_de_dados = db.query(Pessoa).filter(Pessoa.id == id).first()
    if pessoa_no_banco_de_dados:
        pessoa_no_banco_de_dados.nome = pessoa_que_veio_na_requisicao.nome
        pessoa_no_banco_de_dados.idade = pessoa_que_veio_na_requisicao.idade
        db.commit()
        return {'id': pessoa_no_banco_de_dados.id, 'nome': pessoa_no_banco_de_dados.nome, 'idade': pessoa_no_banco_de_dados.idade}
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")

# DELETE 
@app.delete('/pessoas/{id}', response_model=dict)
def remover_pessoa(id: int, db=Depends(get_session)):
    pessoa = db.query(Pessoa).filter(Pessoa.id == id).first()
    if pessoa:
        db.delete(pessoa)
        db.commit()
        return {'mensagem': 'Pessoa removida com sucesso'}
    raise HTTPException(status_code=404, detail="Pessoa não encontrada")