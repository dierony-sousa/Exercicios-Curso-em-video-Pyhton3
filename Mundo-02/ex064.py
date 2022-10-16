# https://www.youtube.com/watch?v=mYlbttiLHM0&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=81

# Entrada e Processamento de dados:
sair = False
num = soma = cont = 0
while not sair:
    print('Para \033[31mPARAR\033[m digite 999')
    num = int(input('OU digite um número para ser tratado: '))
    if num == 999:
        sair = True
    else:
        soma += num
        cont += 1

# Saída de dados:
print('\nVocê digitou {} números.'.format(cont))
print('A SOMA dos números que foram digitados é {}.'.format(soma))
