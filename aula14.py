primeirovalor = input('digite um valor: ')
segundovalor = input('digite outro valor: ')

if primeirovalor > segundovalor:
    print(f'{primeirovalor=} é maior que {segundovalor=}')
elif segundovalor > primeirovalor:
    print(f'{segundovalor=} é maior que {primeirovalor=}')
else:
    print('Valores iguais')