'''
Fatiamento de strings
 012345678
 Olá Mundo
-987654321
Fatiamento [i:f:p] [::]
Obs.: a função len retorna a qtd de carateres da str
'''

variavel = "olá mundo"

print(len(variavel))
print(len(variavel[3]))
print(variavel[-4]) 
print(variavel[-4:])
print(variavel[4:7])
print(variavel[0:4])
print(variavel[:6])
print(variavel[0:9:2]) #pula 1 caractere
print(variavel[-1:-10:-1]) #invertido
print(variavel[2:len(variavel):3])#pula 2 caracteres e inicia a parit do 2o


