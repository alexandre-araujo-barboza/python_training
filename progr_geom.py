# Criar uma progressão geométrica com razão q=2 (recursivamente)

import sys

try:
  steps = int(input("Limit of steps: "))
except ValueError:
  print("Limit of steps must be integer!")
  sys.exit()

def grow(count, value, steps, results):
  if (count > steps):
    return results
  
  value *= 2
  results.append({
    'count' : str(count),
    'value' : str(value),
    'message' : None
  })
  count += 1
  
  try:
    return grow(count, value, steps, results)
  except RecursionError:
    results.append({
      'message': 'Maximum recursion depth exceeded!'
    })
    return results
    
results = grow(1, 1, steps, list())

for result in results:
  if result['message'] is None:
    print('Step:', result['count'], 'Value:', result['value'])
  else:
    print('Error:', result['message'])
  
