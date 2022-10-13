# https://www.youtube.com/watch?v=tapTa6KVG-A&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=60

from random import randint
from time import sleep

# Entrada de dados:
print('{:=^40}'.format('\033[35m Jokenpô \033[m'))
print('[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
valPlayer = int(input('Você escolhe PEDRA, PAPEL ou TESOURA?'))

# Processamento de dados:
jogada = ('PEDRA', 'PAPEL', 'TESOURA')
valPC = randint(0, 2)

# Saída de dados:
print('\033[35mJo...\033[m', end='')
sleep(1)
print('\033[35mken...\033[m', end='')
sleep(1)
print('\033[35mpô!\033[m')
sleep(1)
print('\nO PC escolheu \033[35m{}\033[m '.format(jogada[valPC]))
print('VOCÊ escolheu \033[35m{}\033[m \n'.format(jogada[valPlayer]))

if valPC == 0 and valPlayer == 1:
    print('PAPEL embrulha PEDRA, você \033[32mGANHOU!\033[m')
elif valPC == 0 and valPlayer == 2:
    print('PEDRA quebra TESOURA, você \033[31mPERDEU!\033[m')
elif valPC == 1 and valPlayer == 0:
    print('PAPEL embrulha PEDRA, você \033[31mPERDEU!\033[m')
elif valPC == 1 and valPlayer == 2:
    print('TESOURA corta PAPEL, você \033[32mGANHOU!\033[m')
elif valPC == 2 and valPlayer == 0:
    print('PEDRA quebra TESOURA, você \033[32mGANHOU!\033[m')
elif valPC == 2 and valPlayer == 1:
    print('TESOURA corta PAPEL, você \033[31mPERDEU!\033[m')
elif valPC == valPlayer:
    print('Deu \033[33mEMPATE!\033[m')
else:
    print('Opção inválida! Tente novamente!')
