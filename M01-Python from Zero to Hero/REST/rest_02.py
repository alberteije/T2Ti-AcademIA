from flask import Flask, request

app = Flask(__name__)

pessoas = [
  {"id": 1, "nome": "Amaury", "idade": 52},
  {"id": 2, "nome": "Jesuino", "idade": 29}
]

# GET
@app.route('/pessoas', methods=['GET'])
def listar_pessoas():
  return pessoas, 200

# POST
@app.route('/pessoas', methods=['POST'])
def adicionar_pessoa():
  nova_pessoa = request.json  # Recebe os dados no formato JSON
  nova_pessoa['id'] = len(pessoas) + 1  # Gera um ID automaticamente
  pessoas.append(nova_pessoa)
  return nova_pessoa, 201

# PUT
@app.route('/pessoas/<int:id>', methods=['PUT'])
def atualizar_pessoa(id):
  pessoa = next((p for p in pessoas if p['id'] == id), None)
  if pessoa:
    dados_atualizados = request.json
    pessoa.update(dados_atualizados)
    return pessoa, 200
  return {"erro": "Pessoa não encontrada"}, 404

# DELETE 
@app.route('/pessoas/<int:id>', methods=['DELETE'])
def remover_pessoa(id):
  global pessoas
  pessoas = [p for p in pessoas if p['id'] != id]
  return {"mensagem": "Pessoa removida com sucesso"}, 200


#-----------------------------------------------------#

@app.route("/", methods=['GET'])
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/albert", methods=['GET'])
def albert():
  return "<p>Albert Eije</p>"