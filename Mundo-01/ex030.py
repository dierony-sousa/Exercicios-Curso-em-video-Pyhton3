# https://www.youtube.com/watch?v=4vFCzKuHOn4&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=42

# Entrada de dados:
num = int(input('Digite um número inteiro: '))

# Processamento e Saída de dados:
par = num % 2
if par == 0:
    print('O número que você digitou foi {}, é PAR.'.format(num))
else:
    print('O número que você digitou foi {}, é ÍMPAR.'.format(num))
