# https://www.youtube.com/watch?v=wD2aerLMBWA&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=34

# Entrada de dados:
num = int(input('Digite um número de 0 a 9999: '))

# Processamento de dados:
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10

# Saída de dados:
print('Analisando o número {}'.format(num))
print('unidade: {}'.format(uni))
print('dezena: {}'.format(dez))
print('centena: {}'.format(cen))
print('milhar: {}'.format(mil))
