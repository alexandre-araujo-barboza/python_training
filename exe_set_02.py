# Exercício com set, tuple, dict e list. Com base no exercício da aula 132,
# encontre e liste todos os números que se repetem em cada linha da matriz,
# mostrando quantas vezes eles se repetem.

from pprint import pformat

matrix = [
  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
  [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
  [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
  [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
  [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
  [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
  [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
  [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
  [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
  [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
]
for vector in matrix:
  print(vector)

result = list()
def matrix_scanner(index, vector):
  string = f'line {str(index +1).zfill(2)}'
  line = dict()
  row = list()
  tmp = tuple()
  found = set(vector)
  
  for k1 in found:
    count = 0
    
    for k2 in vector:
      if k1 == k2:
        count += 1
    
    if count > 1:
      tmp = {
        'repeat' : str(count), 
        'value' : str(k1),
      }
      row.append(tmp)
   
  if len(row) == 0:
    row.append('No repetitions found!')
  
  line.update({string : row})
  return line 

for index, vector in enumerate(matrix):
  result.append(matrix_scanner(index, vector))

print('\n')

for value in result:
  layout = pformat(value, width=60)
  removed = ["{", "}", "'", "]"]
  changed = "["
  
  for char in removed:
    layout = layout.replace(char, "")
  
  for char in changed:
    layout = layout.replace(char, "    ")  
  print(layout)  
  