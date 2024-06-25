# dicionário (mutável)

exemplo = dict(nome='Alexandre', sobrenome='Araujo')
print(exemplo, type(exemplo))
print("Is a Dictionary?", type(exemplo) == dict)      

person = {
  'name': 'Alexandre',
  'surname': 'Araujo Barbosa',
  'age': 54,
  'email': 'alexandre.araujo.barboza@gmail.com',
  'address': [
    {
      'street': 'Rua Major Rolinda da Silva',
      'number': 27,
      'neighborhood': 'Barra da Tijuca',
      'zip code': '22611-260',
      'city': 'Rio de janeiro',
      'state': 'RJ',
      'country': 'Brazil',
     },
     {
      'street': 'Victor Konder',
      'number': 100,
      'neighborhood': 'Barra da Tijuca',
      'zip code': '22611-450',
      'city': 'Rio de janeiro',
      'state': 'RJ',
      'country': 'Brazil',
     },
  ],
}

print('\n')

for key in person:
  if type(person[key]) == list:
    address = person[key] 
    
    for i in address:
      print('\n')

      for j in i:
        print (f'{j} = {i[j]}')

  else:  
    print (f'{key} = {person[key]}')

del person['address'] # Apaga os endereços"
if person.get('address') is None:
  print('\nAddress NOT FOUND! (was deleted)\n')

for ks in person.keys():
  print(ks)

print('\n')

for vs in person.values():
  print(vs)


