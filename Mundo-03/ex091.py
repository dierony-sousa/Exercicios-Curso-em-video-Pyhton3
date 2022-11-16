# https://www.youtube.com/watch?v=cwrqIztaAwk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=113

from random import randint
from time import sleep
from operator import itemgetter

jogo = {'Jogador 1': randint(1, 6),
        'Jogador 2': randint(1, 6),
        'Jogador 3': randint(1, 6),
        'Jogador 4': randint(1, 6)}
print('Valores SORTEADOS: ')
sleep(1)
ranking = list()
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
print('-'*32)
print('== Ranking dos Jogadores ==')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]} pontos. ')
    sleep(1)
