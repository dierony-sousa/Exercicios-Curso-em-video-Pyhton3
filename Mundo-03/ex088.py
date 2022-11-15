# https://www.youtube.com/watch?v=Hd7Ycaj61xE&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=109

from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
print('-'*15, 'JOGUE NA MEGA SENA!', '-'*15)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont == 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'Sorteando {quant} JOGOS')
for i, l in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('Boa Sorte!')
