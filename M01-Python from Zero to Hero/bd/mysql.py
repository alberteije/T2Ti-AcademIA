from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Conexão ao banco de dados SQLite - conexão local
conexao = create_engine("mysql+pymysql://root:root@localhost/python", echo=True)

# Base para os mapeamentos
Base = declarative_base()

# Definindo a tabela pessoa
class Pessoa(Base):
  __tablename__ = 'pessoa'
  id = Column(Integer, primary_key=True, autoincrement=True)
  nome = Column(String(100), nullable=True) 
  idade = Column(Integer) 

# Criar o banco de dados e a tabela
Base.metadata.create_all(conexao)

# inserindo dados na tabela pessoa
# pessoa = Pessoa()
# pessoa.nome = "Amaury"
# pessoa.idade = 52
# pessoa.nome = "Jesuino"
# pessoa.idade = 29

# Criando a sessão com o banco de dados
Session = sessionmaker(bind=conexao)
sessao = Session()

# inserindo pessoas
# sessao.add(pessoa)
# sessao.commit()

# consultando pessoas
# lista_pessoas = sessao.query(Pessoa).all()
# for pessoa in lista_pessoas:
#   print(f"nome da pessoa = {pessoa.nome} e idade da pessoa = {pessoa.idade}")