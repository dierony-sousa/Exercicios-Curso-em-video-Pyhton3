# https://www.youtube.com/watch?v=mlwt2CRQkTQ&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=93

from random import randint
val = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10),
       randint(0, 10))
print(f'Os {len(val)} VALORES sorteados foram: ', end='')
for n in val:
    print(f'{n} ', end='')
print(f'\nO MAIOR valor sorteado foi: {max(val)}.')
print(f'O MENOR valor sorteado foi: {min(val)}.')
