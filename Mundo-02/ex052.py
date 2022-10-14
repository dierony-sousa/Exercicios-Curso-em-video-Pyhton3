# https://www.youtube.com/watch?v=Er5Hyd4LyVw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=68

# Entrada de dados:
num = int(input('Digite um número inteiro: '))

# Processamento e Saída de dados:
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[m0 número {} foi divisível {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso ele é PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
