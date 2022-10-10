# https://www.youtube.com/watch?v=NZiNphKkxhg&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=47

# Entrada de dados:
r1 = float(input('Digite o comprimento da primeira reta r: '))
r2 = float(input('Digite o comprimento da segunda reta r: '))
r3 = float(input('Digite o comprimento da terceira reta r: '))

# Processamento e Saída de dados:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar triângulo')
else:
    print('Impossível formar triângulo')
