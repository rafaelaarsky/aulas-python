'''
Introdução ao try/except
try -> tentar executar um código
except -> ocorreu algum erro ao tentar executar
'''
numero_str = input('digite um numero: ')

try:
    numero_float = float(numero_str)
    print('float: ', numero_float)
    print(f'o dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print( 'isso não é um número')