# operadores in e not in
# strings sao iteráveis (pode navegar item por item)

#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1

# nome = 'Otávio'
# print(nome[2])
# print(nome[-4])
# print('á' in nome)
# print(10 * '-')
# print('e' in nome)
# print('e' not in nome)

nome = input("Digite seu nome: ")
encontrar = input(f"Digite o que deseja encontrar em {nome}: ")

if encontrar in nome:
    print(f'{encontrar} está em {nome}.')
else:
    print(f'{encontrar} não está em {nome}')