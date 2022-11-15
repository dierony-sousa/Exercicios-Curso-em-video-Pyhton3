# https://www.youtube.com/watch?v=SXJKAVVlvGA&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=101

listaNum = []
while True:
    listaNum.append(int(input('Digite um número: ')))
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break
listaNum.sort(reverse=True)
print('--'*30)
print(f'Foram digitados {len(listaNum)} números.')
print(f'Os números ordenados de forma decrescente são {listaNum}.')
if 5 in listaNum:
    print('O valor 5 está na sua lista.')
else:
    print('O valor 5 não está na sua lista.')
