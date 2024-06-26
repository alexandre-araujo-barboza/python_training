# Criar uma progressão exponencial

import sys

try:
  steps = int(input("Limit of steps: "))
except ValueError:
  print("Limit of steps must be integer!")
  sys.exit()

value = count = 1 
results = list()
while (count <= steps):
  value *= 2
  results.append({
    'count' : str(count),
    'value' : str(value),
  })
  count += 1
for result in results:
  print('Step:', result['count'], 'Value:', result['value'])
