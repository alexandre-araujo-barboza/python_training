# Cálculo dos dígitos verificadores do CPF em Python

cpf = '74682489070'

multi = 10
result = 0
slice_1 = cpf[:9] # cálculo do primeiro dígito verificador
for piece in slice_1:
  result += int(piece) * multi
  multi -= 1
digit_1 = (result * 10) % 11 # 
digit_1 = digit_1 if digit_1 <= 9 else 0

multi = 11
result = 0
slice_2 = slice_1 + str(digit_1)  # cálculo do segundo dígito verificador
for piece in slice_2:
  result += int(piece) * multi
  multi -= 1
digit_2 = (result * 10) % 11
digit_2 = digit_2 if digit_2 <= 9 else 0

confirm = f'{slice_1}{digit_1}{digit_2}' # validação do CPF
if confirm == cpf:
  print(f'CPF: {confirm} válido!')
else:
  print(f'CPF: {confirm} inválido!')

