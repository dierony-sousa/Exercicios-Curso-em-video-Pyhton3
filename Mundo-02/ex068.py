# https://www.youtube.com/watch?v=EIzgKCCDdc0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=86

from random import randint
cont = 0
print('\033[35m VAMOS JOGAR PAR ou ÍMPAR!\033[m ')
while True:
    num = int(input('Digite um número: '))
    numpc = randint(1, 10)
    jogador = str(input('PAR ou ÍMPAR? [P/I]').upper()).strip()[0]
    print(f'O PC escolheu {numpc} e o JOGADOR escolheu {num}')
    soma = num + numpc
    print('Deu \033[35mPAR!\033[m' if soma % 2 == 0 else 'Deu \033[35mIMPAR!\033[m')
    if soma % 2 == 0:
        if jogador == 'P':
            print('\033[32mVocê VENCEU!\033[m Vamos JOGAR novamente! \n')
            cont += 1
        elif jogador == 'I':
            break
    else:
        if jogador == 'I':
            print('\033[32mVocê VENCEU!\033[m Vamos JOGAR novamente! \n')
            cont += 1
        elif jogador == 'P':
            break
if cont == 0:
    print('\033[31mGAME OVER! PATO!\033[m Não consegue ganhar uma? ')
elif cont == 1:
    print(f'\033[31mGAME OVER!\033[m Você consegiu vencer o PC {cont} vez!')
else:
    print(f'\033[31mGAME OVER!\033[m Você conseguiu vencer o PC {cont} vezes!!!')
