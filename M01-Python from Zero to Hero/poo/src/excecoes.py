class CpfInvalidoException(Exception):
  def __init__(self, mensagem="CPF Invalido! Deve conter 11 digitos numericos."):
    super().__init__(mensagem)

class CnpjInvalidoException(Exception):
  def __init__(self, mensagem="CNPJ Invalido! Deve conter 14 digitos numericos."):
    super().__init__(mensagem)    