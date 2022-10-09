# https://www.youtube.com/watch?v=9l_Gay8BuAw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=23

# Entrada de dados:
tempC = float(input('Informe a temperatura em ºC:'))

# Processamento de dados:
tempF = (tempC * (9/5)) + 32

# Saída de dados:
print('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF !'.format(tempC, tempF))
