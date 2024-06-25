product = 'table'
price = 99.85
interpolation = 'produto: %s, o preço é R$ %.2f' % (product, price)
print(interpolation)

# hexadecimal

print('hexadecimal de %d é %08x' % (15, 15))
print('hexadecimal de %d é %08X' % (4096, 4096))

# padding com f-string

var = 'alexandre'

print(f'{var: >32}') #left space 32
print(f'{var: <32}') #right space 32
print(f'{var: ^32}') #center space 32
print(f'{var: >48}_') #left underscore 40
print(f'{var: <48}0') #right zeros 40

# number format
print(f'{1000.486587320983:0=+10,.2f}')

# slices (fatiamento)
# string[inicio:fim:passo]

var = 'Olá mundo'
#      012345678 (índices)   
print(var[4:7]) 
print(var[4:])
print(var[:7])
print('tamanho: ' + str(len(var)))

# inverte a string
print(var[::-1])
