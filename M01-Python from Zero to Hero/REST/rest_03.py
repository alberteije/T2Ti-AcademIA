from flask import Flask, request, jsonify
from bd.mysql import Pessoa, Session

app = Flask(__name__)

@app.before_request
def berore_request():
  app.sessao = Session()

@app.teardown_request
def teardown_request(exception):
  app.sessao.close()

# GET
@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
  lista_pessoas = app.sessao.query(Pessoa).all()
  return jsonify([{'id': p.id, 'nome': p.nome, 'idade': p.idade} for p in lista_pessoas]), 200

# POST
@app.route('/pessoas', methods=['POST'])
def adicionar_pessoa():
  nova_pessoa_json = request.json  # Recebe os dados no formato JSON
  pessoa = Pessoa()
  pessoa.nome = nova_pessoa_json['nome']
  pessoa.idade = nova_pessoa_json['idade']
  app.sessao.add(pessoa)
  app.sessao.commit()  
  return jsonify({'id': pessoa.id, 'nome': pessoa.nome, 'idade': pessoa.idade}), 201

# PUT
@app.route('/pessoas/<int:id>', methods=['PUT'])
def atualizar_pessoa(id):
    pessoa_no_banco_de_dados = app.sessao.query(Pessoa).filter(Pessoa.id == id).first()
    if pessoa_no_banco_de_dados:
        pessoa_para_alteracao_json = request.json
        pessoa_no_banco_de_dados.nome = pessoa_para_alteracao_json['nome']
        pessoa_no_banco_de_dados.idade = pessoa_para_alteracao_json['idade']
        app.sessao.commit()
        return jsonify({'id': pessoa_no_banco_de_dados.id, 'nome': pessoa_no_banco_de_dados.nome, 'idade': pessoa_no_banco_de_dados.idade}), 200
    return jsonify({'erro': 'Pessoa não encontrada'}), 404

# DELETE 
@app.route('/pessoas/<int:id>', methods=['DELETE'])
def remover_pessoa(id):
    pessoa = app.sessao.query(Pessoa).filter(Pessoa.id == id).first()
    if pessoa:
        app.sessao.delete(pessoa)
        app.sessao.commit()
        return jsonify({'mensagem': 'Pessoa removida com sucesso'}), 200
    return jsonify({'erro': 'Pessoa não encontrada'}), 404