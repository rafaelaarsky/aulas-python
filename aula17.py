'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - hexadecimal (ABCDEF0123456879)
'''

nome = 'luiz'
preco = 1005.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

print(variavel)
print("o hexadecimal de %d é %04x ou %04X" % (1500,1500,1500))