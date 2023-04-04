'''
CONSTANTE = "variáveis" que não vão mudar
muitas condições no mesmo if - ruim
    <- contagem de complexidade - ruim
'''

velocidade = 61     # velocidade atual do carro
local_carro = 101   # local onde o carro está

RADAR_1 = 60        # velocidade máxima do radarw
LOCAL_1 = 100       # local onde o radar1 está
RADAR_RANGE = 1     # a distancia onde o radar pega 

verificacao_local = local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
velocidade_ult = velocidade > RADAR_1

if verificacao_local:
    print('carro passou no radar 1.') 

    if velocidade_ult:
        print("carro acima da velocidade.")
        print('carro multado no radar 1.')
    else:
        print("carro em velocidade permitida")

else:
    print('carro fora do range.')