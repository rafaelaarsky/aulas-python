#como coletar dados do usuário (função input - sempre em string)

nome = input('Qual o seu nome? ')
print(f'O seu nome é {nome}')

numero1 = input('digite um numero: ')
numero2 = input('digite outro numero: ')

soma = int(numero1)+int(numero2) #conversão da string em int

print(f'A soma dos numeros é:{soma}')