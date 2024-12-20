import asyncio
import httpx
import time

async def tarefa_assincrona(nome, tempo):
  print(f"iniciando a tarefa {nome}")
  await asyncio.sleep(tempo)
  print(f"a tarefa {nome} foi finalizada")

async def consumir_api(url):
  try:
    async with httpx.AsyncClient() as client:
      retorno = await client.get(url)
      print(f"retorno da url {url}: {retorno}")
  except Exception as e:
    print(f"ocorreu um problema ao tentar consumir a api {e}")

async def main():
  inicio = time.time()

  url = "https://jsonplaceholder.typicode.com/photos"

  await asyncio.gather(
    consumir_api(url),
    tarefa_assincrona("tarefa 01", 3),
    tarefa_assincrona("tarefa 02", 2),
    tarefa_assincrona("tarefa 03", 1)
  )

  fim = time.time()

  print(f"tempo total para executar as tarefas = {fim-inicio:.2f} segundos")

asyncio.run(main())