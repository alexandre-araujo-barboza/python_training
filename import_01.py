from packages import module

print('Este módulo (interno) se chama', __name__)
print('Função do módulo externo: Soma 2 + 3 =' + str(module.soma(2, 3)))
