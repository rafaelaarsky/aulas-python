# formatando com a função/método format()
a = 'A'
b = 'B'
c = 1.1

string = 'a={0} b={1} c={nome3:.2f}'
formato = string.format(
    a, b, nome3=c #parametro = nome de variavel / argumento = valor
    )

print(formato)