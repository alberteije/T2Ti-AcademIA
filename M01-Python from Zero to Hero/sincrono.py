import time

def tarefa_sincrona(nome, tempo):
  print(f"iniciando a tarefa {nome}")
  time.sleep(tempo)
  print(f"a tarefa {nome} foi finalizada")

inicio = time.time()
tarefa_sincrona("tarefa 01", 3)
tarefa_sincrona("tarefa 02", 2)
tarefa_sincrona("tarefa 03", 1)
fim = time.time()

print(f"tempo total para executar as tarefas = {fim-inicio:.2f} segundos")