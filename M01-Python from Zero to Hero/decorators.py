import functools

def meu_decorator(funcao):
  @functools.wraps(funcao)
  def wrapper(*args, **kwargs):
    print("fazendo algo antes de executar funcao")
    retorno = funcao(*args, **kwargs) # chamando a funcao original
    print(retorno)
    print("fazendo algo depois de executar a funcao")
    return retorno
  return wrapper

@meu_decorator
def minha_funcao():
  """exemplo de funcao com decorator
  """
  print("executando a minha funcao")

@meu_decorator
def somar(a, b, c=6):
  if c != 6:
    return a+b+c
  return a+b

# minha_funcao()
somar(30, b=15, c=20)

print(minha_funcao.__name__)
print(minha_funcao.__doc__)


def funcao_arg_posicionais(*args):
  print(args)

funcao_arg_posicionais(1, 2, 3, 4, 6, "albert", ["pera", "maca", "uva"])

def funcao_arg_nomeados(**kwargs):
  print(kwargs)

funcao_arg_nomeados(a="albert", b=2, c=35, d="joao")

def funcao_ambos_argumentos(*args, **kwargs):
  print(args, kwargs)

funcao_ambos_argumentos(1, 2, 3, 4, 6, "albert", ["pera", "maca", "uva"], a="albert", b=2, c=35, d="joao")