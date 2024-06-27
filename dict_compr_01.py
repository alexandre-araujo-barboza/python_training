# Dictinonary Comprehension e Set Comprehension

produto = {
  'nome': 'Caneta',
  'categoria': 'Escritório',
  'preco': 2.5, 
}

for key, value in produto.items():
  print(key, value)

dictionary = {
  key: value
  if isinstance(value, (int, float)) else value.upper()
  for key, value
  in produto.items()
  if key != 'categoria' 
}
print(dictionary)

my_list = [
  ('key_a', 'value_a'),
  ('key_b', 'value_b'),
  ('key_c', 'value_c'),
]

dictionary = {
  key: value
  for key, value in my_list
}
print(dictionary)
print(dict(my_list))

my_set = {i * 2 for i in range(10)}
print(my_set)

# isinstance - para saber o tipo do objeto
lista = [
  'a', 1, 1.5, False, [0, 1, 2], (1,2),
  {0, 1}, {'nome': 'Alexandre'}, None,
]
for item in lista:
  if isinstance(item, str):
    item = item.upper()
    print('Type: STR', item, isinstance(item, str))
  elif isinstance(item, set):
    item.add(5)
    print('Type: SET', item, isinstance(item, set))
  elif isinstance(item, bool):
    print('Type: BOOL', item, isinstance(item, bool))
  elif isinstance(item, (int, float)):
    print('Type: NUMBER', item, isinstance(item, int) or isinstance(item, float))
  else:
    print('Type: OUTRO', item, type(item))
           