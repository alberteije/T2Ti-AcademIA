class Pessoa:
  # atributos de classe
  populacao = 0 # atributo estático
  contador = 0 # atributo estático

  # método construtor
  def __init__(self, nome, idade): 
    self.__nome = nome    #self.nome = atributo de instancia
    self.__idade = idade  #self.idade = atributo de instancia
    self.contatos = []
    self.enderecos = []
    Pessoa.populacao = Pessoa.populacao + 1;
  
  def __str__(self):
    return f"{self.__nome}, {self.__idade} anos, possui {len(self.contatos)} contatos"
  
  def adicionar_contato(self, contato):
    self.contatos.append(contato)

  def __add__(self, outro):
    nova_pessoa = Pessoa(self.get_nome(), self.get_idade())
    nova_pessoa.contatos = self.contatos + outro.contatos
    return nova_pessoa
  
  def __mul__(self, outro):
    pass
  
  def get_nome(self):
    return self.__nome;

  def set_nome(self, novo_nome):
    print("tamanho do novo_nome", len(novo_nome))
    if len(novo_nome) > 20:
      self.__nome = novo_nome;
    else:
      print("novo nome invalido")

  def get_idade(self):
    return self.__idade;

  def set_idade(self, nova_idade):
    self.__idade = nova_idade;

  def apresentar(self):
    return f"ola, meu nome eh {self.__nome}"
  
  # método de classe
  # definição: Métodos que recebem como primeiro parâmetro a classe em si (cls), 
  # permitindo manipular atributos estáticos ou criar instâncias de maneira alternativa.
  @classmethod
  def criar_anonimo(cls):
    return cls("Mario", 45)
  
  @classmethod
  def incrementar_contador(cls):
    cls.contador += 1;

  # método estático
  # definição: Métodos que não dependem de self ou cls. 
  # Funcionam como funções normais dentro de uma classe, mas estão logicamente relacionados a ela.
  @staticmethod
  def validar_cpf(cpf):
    if len(cpf) < 11:
      print("CPF inválido")
    else:
      print("CPF válido")

# --------------------------------------------------------
# Diferenças entre métodos de classe, instância, etc
# --------------------------------------------------------
# Métodos de instância: operam em dados específicos de um objeto (usam self).
# Métodos de classe: operam no contexto da classe (usam cls).
# Métodos estáticos: não dependem de nenhum estado (nem self nem cls).
# Atributos estáticos: variáveis compartilhadas por todos os objetos da classe.