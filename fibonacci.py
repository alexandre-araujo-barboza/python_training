# Sequência de Fibonnaci (Recursividade)

def fibonacci(step):
  
  def fibo_recursive(n):
    if n < 2: 
      return n
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
  
  acum = 0
  while acum <= step:
    print('Step: ', acum, '\t| Value: ', fibo_recursive(acum))      
    acum +=1

step = input('Type the maximum value of steps: ')
fibonacci(int(step))
