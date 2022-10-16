# https://www.youtube.com/watch?v=-QkOIHJ1Chw&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=75

from random import randint

print('-\033[33m=\033[35m-'*18)
print('\033[mVou pensar em um número entre \033[34m0 \033[me \033[34m10\033[m. \033[35mTente adivinhar!\033[m')
print('-\033[33m=\033[35m-'*18)
numpc = randint(0, 10)
num = int(input('\033[mQual número eu pensei? '))

tentat = 1
while numpc != num:
    print('\n\033[m{}ª Tentativa! \033[31mVocê ERROU! \033[mNão pensei no {}!'.format(tentat, num))
    if numpc > num:
        print('\033[33mDica!\033[m É um número MAIOR que {}'.format(num))
    elif numpc < num:
        print('\033[33mDica!\033[m É um número MENOR que {}'.format(num))
    num = int(input('Mais uma chance! Qual número eu pensei? '))
    tentat += 1
print('\n\033[32mParabéns! Você ACERTOU na {}ª Tentativa!\033[m Eu pensei no nº {}.'.format(tentat, numpc))
