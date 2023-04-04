'''
CONSTANTE = "variáveis" que não vão mudar
muitas condições no mesmo if - ruim
    <- contagem de complexidade - ruim
'''

velocidade = 61     # velocidade atual do carro
local_carro = 90    # local onde o carro está

RADAR_1 = 60        # velocidade máxima do radarw
LOCAL_1 = 100       # local onde o radar1 está
RADAR_RANGE = 1     # a distancia onde o radar pega 

if velocidade > RADAR_1:
    print("acima da velocidade.")