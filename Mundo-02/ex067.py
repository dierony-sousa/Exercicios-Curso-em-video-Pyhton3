# https://www.youtube.com/watch?v=X0a5aZg93Uc&list=PLvE-ZAFRgX8hnECDn1v9HNTI71veL3oW0&index=85

while True:
    print('=-='*6, 'TABUADA', '=-='*6)
    print('Para SAIR informe um número negativo.')
    num = int(input('Digite um número para saber a sua TABUADA: '))
    if num < 0:
        break
    print(f'TABUADA de {num}:')
    for t in range(1, 11):
        prod = num * t
        print(f'{num} x {t} = {prod} ')

print('Você SAIU.')
