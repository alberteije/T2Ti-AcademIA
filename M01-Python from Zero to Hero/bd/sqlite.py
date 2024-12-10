from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# C - Create (Inserção)
# R - Read (Consulta / Listagem)
# U - Update (Atualização / Alteração)
# D - Delete (Exclusão)

# Conexão ao banco de dados SQLite - conexão local
conexao = create_engine("sqlite:///t2ti.db", echo=True)

# Base para os mapeamentos
Base = declarative_base()

# Definindo a tabela pessoa
class Pessoa(Base):
  __tablename__ = 'pessoa'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String, nullable=True) 
  idade = Column(Integer) 

  def __init__(self, nome, idade): 
    self.nome = nome   
    self.idade = idade 

# Criar o banco de dados e a tabela
Base.metadata.create_all(conexao)

# Criando a sessão com o banco de dados
Session = sessionmaker(bind=conexao)
sessao = Session()


# ----------------------------------------------------
# CRUD
# ----------------------------------------------------

# inserção (C)
def criar_pessoas():
  pessoas = [
    Pessoa("Paulo", 29),
    Pessoa("Carlos", 34),
    Pessoa("Maria", 73)
  ]
  sessao.add_all(pessoas)
  sessao.commit()
  print("Pessoas inseridas com sucesso!")

# consulta (R)
def consultar_pessoas():
  lista_pessoas = sessao.query(Pessoa).all()
  for pessoa in lista_pessoas:
    print(f"id da pessoa = {pessoa.id} nome da pessoa = {pessoa.nome} e idade da pessoa = {pessoa.idade}") 

# alteração (U)
def alterar_pessoa(id_pessoa, novo_nome, nova_idade):
  pessoa_consultada_no_banco_de_dados = sessao.query(Pessoa).filter_by(id=id_pessoa).first()
  if pessoa_consultada_no_banco_de_dados:
    pessoa_consultada_no_banco_de_dados.nome = novo_nome
    pessoa_consultada_no_banco_de_dados.idade = nova_idade
    sessao.commit()
    print(f"Pessoa {novo_nome} alterada com sucesso!")
  else:
    print(f"Pessoa {novo_nome} nao encontrada no banco de dados!")

# exclusão (D)
def excluir_pessoa(id_pessoa):
  pessoa_consultada_no_banco_de_dados = sessao.query(Pessoa).filter_by(id=id_pessoa).first()
  if pessoa_consultada_no_banco_de_dados:
    nome = pessoa_consultada_no_banco_de_dados.nome
    sessao.delete(pessoa_consultada_no_banco_de_dados)
    sessao.commit()
    print(f"Pessoa {nome} excluida com sucesso!")
  else:
    print(f"Id {id_pessoa} nao encontrado no banco de dados!")

criar_pessoas()
consultar_pessoas()
alterar_pessoa(1, "Jose", 52)
consultar_pessoas()
excluir_pessoa(2)
consultar_pessoas()



# ----------------------------------------------------
# Aulas 01 e 02
# ----------------------------------------------------
# inserindo dados na tabela pessoa
# pessoa = Pessoa()
# pessoa.nome = "Jesuino"
# pessoa.idade = 29

# inserindo pessoas
# sessao.add(pessoa)
# sessao.commit()

# consultando pessoas
# lista_pessoas = sessao.query(Pessoa).all()
# for pessoa in lista_pessoas:
#   print(f"nome da pessoa = {pessoa.nome} e idade da pessoa = {pessoa.idade}")