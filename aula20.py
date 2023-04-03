# Exercício

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

tam = len(nome)

nome_invertido = nome[::-1]

if ' ' in nome:
    contemounao = 'contém'
else:
    contemounao = 'não contém'

if not nome or not idade:
    print('desculpe, você deixou campo(s) vazio(s).')
else:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome_invertido}')
    print(f'Seu nome {contemounao} espaços')
    print(f'Seu nome tem {tam} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[tam-1]}')