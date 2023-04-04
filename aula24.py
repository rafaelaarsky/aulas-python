# EXERCICIO 1

numero_str = input("digite um número inteiro: ")

# if numero_str.isdigit():

try:
    numero_int = int(numero_str)
    if (numero_int % 2) != 0:
        print(f'{numero_str} é um número ímpar.')
    else:
        print(f'{numero_str} é um número par.')
except:
    print("o item digitado não foi um número inteiro.")

print('-' * 50)


# EXERCICIO 2

hora_str = input("digite o horário atual: ")

try:
    hora_int = int(hora_str)
    if (hora_int >= 0) and (hora_int <= 11):
        print(f'{hora_str}h - Bom dia.')
    elif (hora_int > 11) and (hora_int <= 17):
        print(f'{hora_str}h - Boa tarde.')    
    elif (hora_int > 17) and (hora_int <= 23):
        print(f'{hora_str}h - Boa noite.')
    else:
        print("esse horário não existe.")
except:
    print("Erro. Digite somente o valor da HORA no formato de 24h.")

print('-' * 50)


# EXERCICIO 3

nome_usuario = input("digite seu nome: ")
tam = len(nome_usuario)

nome_grande = tam > 6
nome_medio = 5 <= tam <= 6
nome_pequeno = 1 < tam < 5

if nome_grande:
    print("seu nome é grande")
elif nome_medio:
    print("seu nome tem tamanho médio")
elif nome_pequeno:
    print("seu nome é curto")
else: 
    print("Erro. Digite mais de uma letra.")