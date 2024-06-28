from package import module_01 as m01

print('Este módulo (interno) se chama', __name__)
print('Função do módulo externo: Soma 2 + 3 = ' + str(m01.soma(2, 3)))
