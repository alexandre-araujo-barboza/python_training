# (Parte 3) Threads - Executando processamentos em paralelo

from threading import Lock, Thread
from time import sleep

class Ingressos:
  
  def __init__(self, estoque: int): # param estoque: quantidade de ingressos em estoque
    self.estoque = estoque
    self.lock = Lock()     # Nosso cadeado
  
  def comprar(self, quantidade: int):  # param quantidade: A quantidade de ingressos que deseja comprar
      self.lock.acquire()  # Tranca o método
      
      if self.estoque < quantidade:
        print('Não temos ingressos suficientes.')
        self.lock.release() # Libera o método
        return

      sleep(1)

      self.estoque -= quantidade
      print(f'Você comprou {quantidade} ingresso(s). '
            f'Ainda temos {self.estoque} em estoque.')
        
      self.lock.release() # Libera o método

if __name__ == '__main__':
  ingressos = Ingressos(10)

  for i in range(1, 20):
    t = Thread(target=ingressos.comprar, args=(i,))
    t.start()

  print(ingressos.estoque)