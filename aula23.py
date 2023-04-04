'''
Flag (bandeira) - marcar um local
none - "não valor"
is e is not - é ou não é (tipo, valor, identidade)
id - identidade

v1 = 'a'
v2 = 'a'
v3 = 'b'

print(id(v1))
print(id(v2))
print(id(v3))

'''

condicao = True
passou = None

if condicao:
    print('faça algo')
    passou = True
else:
    print('não faça algo')

if passou is None:
    print('não passou no if')
else:
    print('passou no if')