from package import module_01 as m01, module_02 as m02

print('Este módulo (interno) se chama', __name__)
print('Função do módulo externo: Soma 2 + 3 = ' + str(m01.soma(2, 3)))
print('Função do módulo externo: Multiplica 2 * 3 = ' + str(m02.multiplica(2, 3)))

