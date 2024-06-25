index = 0
string = "Alexandre Araujo Barbosa"
new_str = ''
while index < len(string):
  char = string[index]
  new_str += f'-{char}'
  index += 1
print(new_str)   