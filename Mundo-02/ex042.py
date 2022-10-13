# https://www.youtube.com/watch?v=ZX7sCPjcHA0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=57

# Entrada de dados:
r1 = float(input('Digite o comprimento da primeira reta r: '))
r2 = float(input('Digite o comprimento da segunda reta r: '))
r3 = float(input('Digite o comprimento da terceira reta r: '))

# Processamento e Saída de dados:
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É possível formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('\033[34mEQUILÁTERO\033[m!')
    elif r1 != r2 != r3 and r3 != r1:
        print('\033[34mESCALENO\033[m!')
    else:
        print('\033[34mISÓSCELES\033[m')
else:
    print('\033[31mImpossível formar triângulo\033[m')
