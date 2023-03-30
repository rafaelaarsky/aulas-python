# EXERCÍCIO CALCULO DE IMC

nome = 'Rafaela'
altura = 1.48
peso = 50
imc = peso / (altura**2)

print(nome, "tem", altura, "de altura, pesa", peso, "quilos e seu IMC é", imc)

linha_1 = f'{nome} tem {altura:.2f}m de altura,'
linha_2 = f'pesa {peso}kg e seu IMC é'
linha_3 = f'{imc:.2f}' # f = formatação

print('')
print(linha_1)
print(linha_2)
print(linha_3)