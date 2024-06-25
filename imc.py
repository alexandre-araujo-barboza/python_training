nome = 'Alexandre Araujo'
altura = 1.64
peso = 68
imc = peso / altura ** 2

# f-strings

l1 = f'{nome} tem {altura:.2f} de altura, '
l2 = f'pesa {peso:.2f} e seu IMC é {imc:.2f}'

tupla = l1 + l2
print(tupla)

# format

string = 'nome = {}\npeso = {:.2f}\naltura = {:.2f}\nIMC = {:.2f}\n'
form   =  string.format(nome, peso, altura, imc) 

print(form)
