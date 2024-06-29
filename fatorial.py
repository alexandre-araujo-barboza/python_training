# Fatorial (Recursividade)

def fatorial(step):
  
  def fato_recursive(n):
    if n < 2: 
      return n
    return fato_recursive(n - 1) * n
  
  acum = 0
  while acum <= step:
    print('Step: ', acum, '\t| Value: ', fato_recursive(acum))      
    acum +=1

step = input('Type the maximum value of steps: ')
fatorial(int(step)) 