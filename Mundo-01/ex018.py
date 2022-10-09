# https://www.youtube.com/watch?v=9GvsphwW26k&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=28

from math import sin, cos, tan, radians

# Entrada de dados:
ang = float(input('Digite o ângulo que você deseja: '))

# Saída de dados:
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sin(radians(ang))))
print('O ângulo de {} tem o COSENO de {:.2f}'.format(ang, cos(radians(ang))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan(radians(ang))))
