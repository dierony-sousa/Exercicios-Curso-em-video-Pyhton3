# https://www.youtube.com/watch?v=LkAzRnc_GPk&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=99

listaNum = []
while True:
    n = int(input('Digite um número: '))
    if n not in listaNum:
        listaNum.append(n)
        print('Valor adicionado!')
    else:
        print('Valor duplicado! Não foi adicionado!')
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar in 'N':
        break
listaNum.sort()
print(f'Você digitou os valores {listaNum}')
