# exemplo: variável livre e não local

def concatenate(string):
  free = string

  def nested(concatenated = ''):
        
    nonlocal free
    free += concatenated
    return free
    
  return nested

def truncate(string):
  free = string

  def nested(truncated = len(free)):
    
    nonlocal free
    free = free[0:truncated]
    return free
  
  return nested
    
print('\nConcatenando:\n')

conca = concatenate('Alexandre')
print('1)', conca('Araujo'))
print('2)', conca('Barbosa'))

concatened = conca()
print('Concatenado: ', concatened)

print('\nTruncando:\n')

trunca = truncate(concatened)
print('1)', trunca(15))
print('2)', trunca(9))

truncated = trunca()
print('Truncado: ', truncated)

print()