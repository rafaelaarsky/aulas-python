# and, or and not

entrada = input("[E]ntrar ou [S]air: ")
senha_d = input("Senha: ")

senha_p = '123456'

if not senha_d:
    print("voce nao digitou a senha")
elif (entrada == 'E' or entrada == 'e') and senha_d == senha_p:
    print("Entrada permitida")
elif entrada == 'S' and senha_d == senha_p:
    print("Logout Feito")
else:
    print("Erro. Tente Novamente.")