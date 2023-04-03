'''
Formatação básica de strings
s - string
d - int
f - float
.<numero de digitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - força o número a aparecer antes do 0
Sinal - + ou - 
Ex.: 0>-100, .1f
Conversion flags - !r !s !a
'''

variavel = 'ABC'
num = 1500

print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:$^10}')
print(f'{1000.5434562261:0=+10,.1f}')
print(f'o heaxadecimal de {num} é {num:08x}')

print(f'{num!r}')